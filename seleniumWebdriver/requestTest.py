import requests
import re

class downLoadTest():

    def __init__(self):
        myHeaders = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
        }
        self.myHeaders = myHeaders

    '''
    1、获取单页中的音频链接list
    '''
    def getContent(self,myUrl):
        myTemp = requests.get(myUrl,headers=self.myHeaders)
        myJson = myTemp.json()
        myData = myJson['data']['trackDetailInfos']
        urlList = []
        for i in range(len(myData)):
            temp = myData[i]
            urlList.append(temp['trackInfo']['playPath'])
        return urlList

    '''
    1、根据单个url下载音频文件
    '''
    def downFile(self,url,filePath):

        contentItem = requests.get(url,headers=self.myHeaders)
        with open(filePath, 'wb') as f:
            f.write(contentItem.content)

    '''
    3、批量下载音频文件
    '''
    def downFiles(self,urllist):
        n = 0
        for itemUrl in urllist:
            filePath = r'E:\saveFileTest\第%d章节.m4a' % n
            self.downFile(itemUrl,filePath)
            n=n+1


if __name__ == '__main__':
    myUrl = 'https://m.ximalaya.com/m-revision/common/album/queryAlbumTrackRecordsByPage?albumId=42267227&page=1&pageSize=7&asc=true&countKeys=play,comment&v=1602743316770'
    myTest = downLoadTest()
    myRestult = myTest.getContent(myUrl)
    myTest.downFiles(myRestult)





