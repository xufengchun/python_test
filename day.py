import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)

# x轴标题
plt.xlabel('Smarts')
# y轴标题
plt.ylabel('Probability')
# 子图标题
plt.title('Histogram of IQ')
# 指定坐标处添加文本
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()