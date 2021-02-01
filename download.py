from ftplib import FTP  # 引入ftp模块
from re import search
import os
from time import time

class MyFtp():
    ftp = FTP()
    def __init__(self, host = '',port=21):
        super(MyFtp, self).__init__()
        self.state = None
        try:
            self.ftp.connect(host,port)
        except Exception as e:
            print(e)

    def login(self,username,pwd):
        try:
            self.ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
            self.ftp.login(username,pwd)
            print(self.ftp.welcome)
            return True
        except Exception:
            print('登陆失败')
            return False

    def downloadversion(self, text, data, localpath = './',remotepath = './pub',filename = 'version'):
        data.version = False
        self.login('','')
        lastVersion = text[search('-', text).span()[1]:]

        self.ftp.cwd(remotepath)   # 要登录的ftp目录
        self.ftp.nlst()  # 获取目录下的文件
        file_handle = open('./download/' + filename,"wb")   # 以写模式在本地打开文件
        self.ftp.retrbinary('RETR %s' % os.path.basename(filename),file_handle.write,blocksize=1024)  # 下载ftp文件
        file_handle.close()
        version = open('./download/version', 'r')
        versionOnline = version.read()[:-1]
        print(versionOnline)
        version.close()
        try:
            if lastVersion[0] == versionOnline[0]:
                if int(lastVersion[2:-2]) == int(versionOnline[2:-2]):
                    if lastVersion[-1] >= versionOnline[-1]:
                        data.version = None
                        return None
                    else:
                        data.version = versionOnline
                        return versionOnline
                elif int(lastVersion[2:-2]) > int(versionOnline[2:-2]):
                    data.version = None
                    return None
                else:
                    data.version = versionOnline
                    return versionOnline
            elif lastVersion[0] > versionOnline[0]:
                data.version = None
                return None
            else:
                data.version = versionOnline
                return versionOnline
        except Exception as e:
            print('错误:', e)
            data.version = None
            return None
        
    def downloadFile(self, filename, signal, speed, data, remotepath = '/pub'):
        data.version = False
        self.login('','')
        buffer_size = 10240  # 默认是8192
        self.ftp.cwd(remotepath)   # 要登录的ftp目录
        self.ftp.nlst()  # 获取目录下的文件
        ftp = self.ftp
        ftp_file_path = remotepath+'/'+filename
        try:
            remote_file_size = ftp.size(remotepath+'/'+filename)  # 文件总大小
            print('remote filesize [{}]'.format(remote_file_size))
            ftp.voidcmd('TYPE I')
            #file_handle = open('./download/' + filename,"wb").write   # 以写模式在本地打开文件
            cmpsize = 0  # 下载文件初始大小
            lsize = 0
            conn = ftp.transfercmd('RETR {0}'.format(ftp_file_path), lsize)

            f = open('./download/' + filename, "wb")
            start = time()-0.001
            while True:
                data2 = conn.recv(buffer_size)
                if not data2:
                    break
                f.write(data2)
                cmpsize += len(data2)
                signal.emit(int(cmpsize/remote_file_size*100)) 
                speed.emit('下载中 {:.2f}kb/s'.format(cmpsize/1000/(time()-start)))
                print(cmpsize, remote_file_size)
            data.version = None
            return True
        except Exception as e:
            print('错误', e)
            return False
            data.version = None
    

    def close(self):
        self.ftp.set_debuglevel(0)  # 关闭调试
        self.ftp.quit()