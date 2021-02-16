from ftplib import FTP  # 引入ftp模块
from re import search
import os
from time import time
import hashlib
import requests
import json

url = ""
hosturl = ""
ftpPath = ""
httpPath = ""
downloadPath = ""
HOST = ''
ignoreList = ['update.exe', 'version', 'config.json', 'download.py', 'update.py', 'updateList.json', 'versionInfo.json']

def getVersionInfo(lastVersion):
    try:
        InfoFile = requests.get(url)
        with open('./download/versionInfo.json', 'wb') as f:
            f.write(InfoFile.content)
        Info = json.loads(InfoFile.text)
        version = Info['version']
    except:
        return None
    print(version)
    dotV = version.index('.')
    dotLV = lastVersion.index('.')
    headV = int(version[:dotV])
    headLV = int(lastVersion[:dotLV])
    tailV = float(version[dotV + 1:])
    tailLV = float(lastVersion[dotLV + 1:])
    if headLV < headV:
        return Info
    elif headLV == headV:
        if tailLV < tailV:
            return Info
        else:
            return None
    else:
        return None

def diff_files(versionInfo):
    diff = {}
    fileNum = versionInfo['fileNum']
    md5 = versionInfo['fileMD5']
    fileExist = True
    if os.path.exists('versionInfo.json'):
        try:
            with open('versionInfo.json') as f:
                file_md5 = json.load(f)['fileMD5']
        except:
            file_md5 = {}
            fileExist = False
    else:
        file_md5 = {}
        fileExist = False
    fileCount = 0
    import time
    t = time.time()
    for key in md5.keys():
        fileCount += 1
        # print(fileCount)
        path = './' + key
        if fileExist == False:
            try:
                with open(path, 'rb') as f:
                    file_md5[key] = hashlib.md5(f.read()).hexdigest()
            except Exception as e:
                print(e)
        if key in file_md5:
            if file_md5[key] != md5[key]:
                diff[key] = md5[key]
            else:
                continue
        else:
            diff[key] = md5[key]
    print(t - time.time())
    if fileCount == fileNum:
        print('>>> 共需下载{}个文件'.format(len(diff)))
        return diff
    else:
        return False

def httpDownloadFile(filePath, savePath):
    filePath = filePath.replace('\\', '/')
    print('>>> 开始接收文件' + filePath, end='\t\t')
    if filePath[0] == '/':
        filePath = filePath[1:]
    r = requests.get(hosturl + filePath)
    with open(savePath, "wb+") as f:
        f.write(r.content)
        print('成功')
        return 

def initDir(path):
    dirPath = '.'
    for Dir in path.split('\\')[:-1]:
        dirPath = dirPath + '\\' + Dir
        if os.path.exists(dirPath):
            pass
        else:
            os.mkdir(dirPath)


def downloadDiffFile(diffDict, signal = None):
    global httpPath
    failDict = {}
    fileCount = 0
    allFileNum = len(diffDict)
    for item in diffDict.keys():
        if signal != None:
            signal.emit(int(fileCount/allFileNum*100)) 
        # filename = item.split('\\')[-1]
        savePath = os.path.join(downloadPath, item)
        initDir(savePath)
        if os.path.exists(savePath):
            with open(savePath, 'rb') as f:
                file_md5 = hashlib.md5(f.read()).hexdigest()
            if file_md5 == diffDict[item]:
                print('>>> 本地文件{}\t\t校验成功'.format(savePath))
                fileCount += 1
                continue
            else:
                print('>>> 本地文件{} 校验失败'.format(savePath))
        httpFilePath = os.path.join(httpPath, item)
        httpFilePath = httpFilePath.replace('\\', '/')
        # ftpPath = ftpPath.replace('\\', '/')
        # print(httpFilePath, downloadPath + filename)
        httpDownloadFile(httpFilePath, savePath)
        print('>>> 校验文件' + savePath, end='\t\t')
        with open(savePath, 'rb') as f:
            file_md5 = hashlib.md5(f.read()).hexdigest()
        if file_md5 == diffDict[item]:
            fileCount += 1
            print('成功')
        else:
            print('失败')
            print(file_md5, diffDict[item])
            failDict[item] = diffDict[item]
        
    print('>>> {}个文件下载成功, {}个文件下载失败'.format(fileCount, len(failDict)))
    return failDict

def checkFile(versionInfo = None, signal = None):
    try:
        with open('versionInfo.json') as f:
            currentVersion = json.load(f)['version']
    except Exception as e:
        print('检查当前版本错误')
        return False
    if type(versionInfo) != dict:
        versionInfo = getVersionInfo(currentVersion)
    updateList = diff = diff_files(versionInfo)
    # input()
    MaxTry = 3
    while MaxTry > 0:
        failDict = downloadDiffFile(diff, signal)
        if len(failDict) == 0:
            break
        else:
            MaxTry -= 1
            diff = failDict
    if MaxTry > 0:
        with open('./download/updateList.json', 'w') as f:
            json.dump(updateList, f, sort_keys=True,indent=2, separators=(',', ': '))
        return True
    else:
        return False

# checkFile()

# httpDownloadFile('\\versionInfo.json', './versionInfo.json')

class MyFtp():
    ftp = FTP()
    def __init__(self, host = HOST,port=21):
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
        #data.version = False
        # lastVersion = text[search('-', text).span()[1]:]
        lastVersion = text

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
                        #data.version = None
                        return None
                    else:
                        #data.version = versionOnline
                        return versionOnline
                elif int(lastVersion[2:-2]) > int(versionOnline[2:-2]):
                    #data.version = None
                    return None
                else:
                    #data.version = versionOnline
                    return versionOnline
            elif lastVersion[0] > versionOnline[0]:
                #data.version = None
                return None
            else:
                #data.version = versionOnline
                return versionOnline
        except Exception as e:
            print('错误:', e)
            #data.version = None
            return None
        
    def downloadFile(self, filename, signal = None, speed = None, filePath = '/pub', remotepath='/pub'):
        buffer_size = 10240  # 默认是8192
        self.ftp.cwd(remotepath)   # 要登录的ftp目录
        # self.ftp.nlst()  # 获取目录下的文件
        ftp = self.ftp
        if filename[0] != '/':
            filename = '/' + filename
        ftp_file_path = filePath + filename

        try:
            remote_file_size = ftp.size(ftp_file_path)  # 文件总大小
            print('remote filesize [{}]'.format(remote_file_size))
            ftp.voidcmd('TYPE I')
            #file_handle = open('./download/' + filename,"wb").write   # 以写模式在本地打开文件
            cmpsize = 0  # 下载文件初始大小
            lsize = 0
            conn = ftp.transfercmd('RETR {0}'.format(ftp_file_path), lsize)

            f = open('./download/' + filename, "wb")
            start = time()-0.001
            while True:
                data = conn.recv(buffer_size)
                if not data:
                    break
                f.write(data)
                cmpsize += len(data)
                if signal != None:
                    signal.emit(int(cmpsize/remote_file_size*100)) 
                if speed != None:
                    speed.emit('下载中 {:.2f}kb/s'.format(cmpsize/1000/(time()-start)))
                print(cmpsize, remote_file_size)
            return True
        except Exception as e:
            print('错误', e)
            return False

    def downloadDiffFile(self, diffDict):
        global ftpPath
        for item in diffDict:
            filename = item.split('\\')[-1]
            filePath = item[:item.index(filename) - 1]
            ftpPath = os.path.join(ftpPath, filePath)
            filename = filename.replace('\\', '/')
            ftpPath = ftpPath.replace('\\', '/')
            # print(filePath, filename)
            self.downloadFile(filename, filePath=ftpPath)
            print('>>> 开始接收文件'+filename, end=' ')
            print('成功')

    def close(self):
        self.ftp.set_debuglevel(0)  # 关闭调试
        self.ftp.quit()

# diff = diff_files(getVersionInfo('1.1.1'))
# print(diff)
# input()
# f = MyFtp()
# f.login('', '')
# f.downloadDiffFile(diff)
# f.close()
