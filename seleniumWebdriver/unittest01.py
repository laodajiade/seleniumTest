import requests
import re

tolurl = 'https://www.ximalaya.com/revision/album/v1/getTracksList?albumId=18943952&pageNum=3'
myHeader = {
    'User-Agent':
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
}
content = requests.get(tolurl,headers = myHeader)
jsonContent = content.json()
myDatab = jsonContent['data']['tracks']
#print(myDatab)
urlList = []
for i in myDatab:
    urlList.append('https://www.ximalaya.com'+i['url'])

print(urlList)





