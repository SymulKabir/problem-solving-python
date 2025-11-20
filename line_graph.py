# Plot a simple line graph

import matplotlib.pyplot as plt;
import numpy as np;

x = np.array([1, 2, 6, 3, 4, 5]);

plt.plot(x)
plt.title("Simple line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.show();

