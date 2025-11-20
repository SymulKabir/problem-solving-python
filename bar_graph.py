# Bar chart of marks

import matplotlib.pyplot as plt;
import numpy as np;

subjects = np.array(["Math", "English", "Science"])
marks = np.array([80, 70, 90])

plt.bar(subjects, marks, color = "blue")
plt.title("Bar graph of marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()