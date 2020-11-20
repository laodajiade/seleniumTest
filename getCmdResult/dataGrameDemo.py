import matplotlib.pyplot as plt

'''
动态折线图演示示例
'''

import numpy as np
import matplotlib.pyplot as plt

plt.ion()
plt.figure(1)
t_list = []
result_list = []
t = 0

while True:
    if t >= 10 * np.pi:
        plt.clf()
        t = 0
        t_list.clear()
        result_list.clear()
    else:
        t += np.pi / 4
        t_list.append(t)
        result_list.append(np.sin(t))
        plt.plot(t_list, result_list, c='r', ls='-', marker='o', mec='b', mfc='w')  ## 保存历史数据
        # plt.plot(t, np.sin(t), 'o')
        plt.pause(0.1)

# x_data = [1]
# y_data = [1]
# for i in range(2,50):
#     x_data.append(i)
#     y_data.append(i)
# plt.plot(x_data, y_data)
# plt.show()
# print('绘制成功'+i)
#
# print('结束--------------------')