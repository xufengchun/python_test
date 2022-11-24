import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 100)
y = np.sin(x)

plt.subplot(211)
plt.plot(x, y, 'r')
plt. xlabel('wendu')
plt. ylabel('shijian')
plt.grid(True)

plt.subplot(212)
plt.plot(x, y, 'b')
plt. xlabel('wendu')
plt. ylabel('shijian')
plt.grid(True)
plt.show()


