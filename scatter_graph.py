# Create a scatter plot

import matplotlib.pyplot as plt;
import numpy as np;

x = np.array([1,2,3,4,5])
y = np.array([2,4,1,8,7])

plt.scatter(x, y, color = "blue")
plt.title("Scatter plot example")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.show()