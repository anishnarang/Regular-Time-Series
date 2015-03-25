import matplotlib.pyplot as plt
import numpy as np

#generate some data
x = np.array(range(20))
y = 3 + 0.5 * x + np.random.randn(20)

#plot the data
plt.plot(x, y, 'r')
plt.show()
