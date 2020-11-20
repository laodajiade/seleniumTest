import numpy as np
import matplotlib.pyplot as plt
import random

plt.figure(1)
t_list = []
result_list = []
t = 0
while True:
    t += 1
    t_list.append(t)
    temp = random.randint(1,10)
    result_list.append(temp)
    plt.plot(t_list, result_list, c='r', ls='-', marker='o', mec='b', mfc='w')  ## 保存历史数据
    # plt.plot(t, np.sin(t), 'o')
    plt.pause(0.1)