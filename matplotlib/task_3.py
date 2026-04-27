import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4]
y1 = [10, 20, 25, 30]
y2 = [5, 15, 20, 25]

# Create subplots (1 row, 2 columns)
fig, ax = plt.subplots(2, 3)

# Select subplot Position
ax[0][2].plot(x, y1)
ax[0][2].set_title("Plot 1")

# Second subplot
# ax[1].plot(x, y2)
# ax[1].set_title("Plot 2")

plt.show()