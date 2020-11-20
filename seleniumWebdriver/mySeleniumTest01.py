# 1、用selenium打开Firefox/chrome浏览器
# 2、打开一个页面链接
# 3、定位页面元素进行内容搜索
from selenium import webdriver
from time import sleep
class myTest:

    #打开浏览器
    driver = webdriver.Chrome()
    def __init__(self):
        baiduUrl = 'https://www.baidu.com/'
        self.baiduUrl = baiduUrl

    #打开链接
    def openUrl(self):
        self.driver.get(self.baiduUrl)

    #根据页面元素对页面进行操作
    def controlOption(self):
        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id('kw').send_keys("selenium")
        self.driver.find_element_by_id('su').click()
        print('搜索成功')

    #关闭浏览器
    def closeUrl(self):
        self.driver.quit()

if __name__ == '__main__':

    test = myTest()
    test.openUrl()
    test.controlOption()
    sleep(3)
    test.closeUrl()










