# Plot a simple line graph

import matplotlib.pyplot as plt;
import numpy as np;

x = np.array([1, 2, 6, 3, 4, 5]);
y = np.array([4, 3, 5, 7, 2, 4]);

plt.plot(x, y)
plt.title("Simple line graph with two lines")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.show();