# Basic Pie Chart

import matplotlib.pyplot as plt;
import numpy as np;

fruits = np.array(["Apple", "Banana", "Mango", "Orange"])
values = np.array([40, 30, 20, 10]);.0

plt.pie(values, labels = fruits, autopct='%0.0f%%')
plt.title("Pie chart of fruits")
plt.show()