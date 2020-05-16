import os
from ftplib import FTP  # 引入ftp模块
import time

class MyFtp:

    ftp = FTP()

    def __init__(self,host,port=21):
        try:
            self.ftp.connect(host,port)
        except Exception as e:
            print(e)
        self.login('','')

    def login(self,username,pwd):
        self.ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
        self.ftp.login(username,pwd)
        print(self.ftp.welcome)

    def downloadversion(self,localpath = './',remotepath = './pub',filename = 'version'):
        self.ftp.cwd(remotepath)   # 要登录的ftp目录
        self.ftp.nlst()  # 获取目录下的文件
        file_handle = open(filename,"wb")   # 以写模式在本地打开文件
        self.ftp.retrbinary('RETR %s' % os.path.basename(filename),file_handle.write,blocksize=1024)  # 下载ftp文件
        file_handle.close()
        version = open('version', 'r')
        return version.read()[:-1]
        version.close()
        
    def downloadFile(self,filename,localpath = './',remotepath = '/pub'):
        buffer_size = 10240  # 默认是8192
        self.ftp.cwd(remotepath)   # 要登录的ftp目录
        self.ftp.nlst()  # 获取目录下的文件
        ftp = self.ftp
        ftp_file_path = remotepath+'/'+filename
        remote_file_size = ftp.size(remotepath+'/'+filename)  # 文件总大小
        print('remote filesize [{}]'.format(remote_file_size))
        ftp.voidcmd('TYPE I')
        #file_handle = open(filename,"wb").write   # 以写模式在本地打开文件
        cmpsize = 0  # 下载文件初始大小
        lsize = 0
        start = time.time()
        conn = ftp.transfercmd('RETR {0}'.format(ftp_file_path), lsize)

        f = open(filename, "wb")
        while True:
            data = conn.recv(buffer_size)
            if not data:
                break
            f.write(data)
            cmpsize += len(data)
            print(cmpsize, remote_file_size)

    def close(self):
        self.ftp.set_debuglevel(0)  # 关闭调试
        self.ftp.quit()

if __name__ == '__main__':
    ftp = MyFtp('unarvest.top')
    #ftp.downloadFile('./','/pub','串口调试器0.512.1.exe')
    version = ftp.downloadversion()
    ftp.downloadFile('串口调试器' + version + '.exe')
    ftp.close()