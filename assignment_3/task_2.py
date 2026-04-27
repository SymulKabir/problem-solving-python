# Exercise 2: Create a Line Plot Comparing the Growth of Two Companies Over 5 Years
# Requirements

# Create two lists of data, for example:

# Company A: [10, 20, 25, 40, 60]
# Company B: [15, 18, 30, 35, 55]
# representing revenue over 5 years.
# Layout:

# Use plt.subplots() to create a single figure (fig, ax).

# Plotting:

# Plot both lines on the same axes:

# Company A: Red line, dashed ('--'), marker 'o'
# Company B: Blue line, solid ('-'), marker 's'
# Styling:
# Add a title: "Company Revenue Growth"
# Label the x-axis "Year" and the y-axis "Revenue (Millions)"
# Add a legend identifying "Company A" and "Company B"
# Add a grid (ax.grid(True))



import matplotlib.pyplot as plt

years = [1, 2, 3, 4, 5]

company_A = [10, 20, 25, 40, 60]
company_B = [15, 18, 30, 35, 55]

fig, ax = plt.subplots()

ax.plot(years, company_A, 'o--', color='red', label='Company A')
ax.plot(years, company_B, 's-', color='blue', label='Company B')

ax.set_title("Company Revenue Growth")
ax.set_xlabel("Year")
ax.set_ylabel("Revenue (Millions)")

ax.legend()
ax.grid(True)

plt.savefig("company_growth.png")

plt.show()