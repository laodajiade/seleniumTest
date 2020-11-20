import subprocess
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import matplotlib.ticker as ticker
import re
'''
获取android设备中pair应用所占内存
1、连接按android设备
2、获取android设备目标内存信息

4、制作图表展示
@TODO 批量处理
'''
class cmdTest:
    def __init__(self,mip):
        self.getMemoryCmd = 'adb shell dumpsys meminfo com.logitech.pair'
        self.ip = mip

    # 1、连接按android设备
    def connectP(self):
        cmd = 'adb connect ' + self.ip
        successConnect = b'connected to'
        result = subprocess.check_output(cmd)
        if successConnect in result:
            print('连接成功/已连接')
            return True
        else:
            print('连接失败！')
            return False

    #2、获取单台设备内pair应用使用内存情况
    def getMemory(self):
        if self.connectP():
            result1 = subprocess.check_output(self.getMemoryCmd)
            resultString = str(result1, encoding='utf-8')
            #print(resultString)
            temp = r'TOTAL\s+\d+'
            result1 = re.search(temp,resultString)

            result2 = re.search(r'\d+',str(result1)).group(0)
            # print(result2)
            # print(type(result2))
            return (int(result2))*0.01
            # result2 = result1.replace(',','.').strip()
            # result3 = re.search(r'\d+.\d+',result2).group(0)
            # print(float(result3))
            # return float(result3)


    #3、制作图表展示
    def dataGrame(self):
        plt.figure(0.5)
        #设置折线图xy坐标主题
        plt.xlabel('time')
        plt.ylabel('memory/K')

        #设置刻度间隔并保存到变量中
        x_major_locator = MultipleLocator(1)
        y_major_locator = MultipleLocator(0.05)
        #实例两条坐标轴
        ax = plt.gca()
        #设置轴的刻度为设置的间隔的倍数
        ax.xaxis.set_major_locator(x_major_locator)
        ax.yaxis.set_major_locator(y_major_locator)


        t_list = []
        result_list = []
        t = 0
        while True:
            t += 1
            t_list.append(t)
            temp = self.getMemory()
            result_list.append(temp)
            plt.plot(t_list, result_list, c='r', ls='-', marker='.', mec='b', mfc='w')  ## 保存历史数据
            # plt.plot(t, np.sin(t), 'o')
            #设置间隔时间（s）
            plt.pause(5)



if __name__ == '__main__':
    ip = '30.40.46.127'
    mList = []
    test = cmdTest(ip)
    #test.getMemory()
    test.dataGrame()
    #print(test.getMemory())




