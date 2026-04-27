# Plotting Without Line

import matplotlib.pyplot as plt;
import numpy as np;

x_points = np.array([1, 8])
y_points = np.array([3, 10])

plt.plot(x_points, y_points, ">")
plt.show()