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