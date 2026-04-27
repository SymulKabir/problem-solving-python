# Exercise 1: Sales Performance Comparison

# Your task is to create a visualization comparing the sales performance of two different products over a 6-month period using a single figure.

# Requirements

# Data Preparation:
# Use NumPy to create a range for months (1 to 6) and two arrays for sales data:

# Product A: [20, 35, 30, 35, 27, 45]
# Product B: [25, 32, 34, 20, 25, 36]

# Plotting:

# Plot Product A as a solid line with circle markers.
# Plot Product B as a dashed line with square markers.

# Customization:

# Add a title: "Product Sales Comparison (Jan – June)"
# Add axis labels: "Month" and "Units Sold"
# Include a legend to distinguish between Product A and Product B.
# Use plt.grid(True) to show a grid for better readability.


import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 7)

product_A = [20, 35, 30, 35, 27, 45]
product_B = [25, 32, 34, 20, 25, 36]

plt.plot(months, product_A, 'o-', label='Product A')   
plt.plot(months, product_B, 's--', label='Product B') 

plt.title("Product Sales Comparison (Jan - June)")
plt.xlabel("Month")
plt.ylabel("Units Sold")

plt.legend()
plt.grid(True)

plt.show()