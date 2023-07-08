import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mu, sigma):
    return 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-(x-mu)**2/(2*sigma**2))

def gaussian_derivative(x, mu, sigma):
    return -(x-mu)/(sigma**2)*gaussian(x, mu, sigma)

x = np.linspace(-1, 1, 1000)
y = gaussian_derivative(x, 0, 0.001)

plt.plot(x, y)
plt.title('Derivative of the delta function')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
