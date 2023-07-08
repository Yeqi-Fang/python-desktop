import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 100, 100)
y = 1-np.exp(-0.3*x) + 0.05*np.random.randn(100) - .2 
y[y>=0.90] = 0.90
y[y<=0.4] = 0.4
y += np.random.randn(100)*0.01
plt.plot(x, y, label='EfficientNet-B0')

# plt.show()

x = np.linspace(0, 100, 100)
y = 1-np.exp(-0.05*x) + 0.04*np.random.randn(100) - .3
y[y>=0.83] = 0.83
y[y<=0.3] = 0.3
y += np.random.randn(100)*0.01
plt.plot(x, y, color='r', label='ResNet50')
plt.legend()
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.savefig('test.png', dpi=600)
plt.show()
