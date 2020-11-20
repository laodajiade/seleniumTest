import requests
import re
# 根据url获取网页html内容
def getHtmlContent(url):
    page = requests.get(url)
    return page.text


# 从html中解析出所有jpg图片的url
# 百度贴吧html中jpg图片的url格式为：<img ... src="XXX.jpg" width=...>
def getJPGs(html):
    # 解析jpg图片url的正则
    jpgReg = re.compile(r'<img.+?src="(.+?\.jpg)" width')  # 注：这里最后加一个'width'是为了提高匹配精确度
    # 解析出jpg的url列表
    jpgs = re.findall(jpgReg, html)

    return jpgs


# 用图片url下载图片并保存成制定文件名
def downloadJPG(imgUrl, fileName):
    # 可自动关闭请求和响应的模块
    from contextlib import closing
    with closing(requests.get(imgUrl, stream=True)) as resp:
        with open(fileName, 'wb') as f:
            for chunk in resp.iter_content(128):
                f.write(chunk)


# 批量下载图片，默认保存到当前目录下
def batchDownloadJPGs(imgUrls, path='./'):
    # 用于给图片命名
    count = 1
    for url in imgUrls:
        downloadJPG(url, ''.join([path, '{0}.jpg'.format(count)]))
        print
        '下载完成第{0}张图片'.format(count)
        count = count + 1


# 封装：从百度贴吧网页下载图片
def download(url):
    html = getHtmlContent(url)
    jpgs = getJPGs(html)
    batchDownloadJPGs(jpgs)


def main():
    url = 'http://tieba.baidu.com/p/2256306796'
    download(url)


if __name__ == '__main__':
    main()