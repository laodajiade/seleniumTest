import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(1000)
y = np.random.standard_normal(20)

plt.figure(figsize=(7, 4))  # 画布大小
plt.plot(y.cumsum(), 'b', lw=1.5)  # 蓝色的线
plt.plot(y.cumsum(), 'ro')  # 离散的点
plt.grid(True)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('A simple Plot')
plt.show()