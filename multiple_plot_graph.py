# Plot multiple lines on same graph

import matplotlib.pyplot as plt;
import numpy as np;

y1 = np.array([1,2,3,4,5])
y2 = np.array([5,4,3,2,1])

plt.plot(y1, label= "Increasing line")
plt.plot(y2, label="Decreasing line")
plt.legend()
plt.title("Two Lines on Same Graph")
plt.show()
