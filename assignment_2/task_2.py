import pandas as pd
import numpy as np

data = {
    'Transaction_ID': [101, 102, 102, 103, 104, 105, 106, 107, 108],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-02', '01/03/2023', '2023-01-04', np.nan, '2023-01-06', '2023-01-07', '2023-01-08'],
    'Customer': [' alice smith ', 'Bob Jones', 'Bob Jones', 'Charlie Brown', '  david lee', 'Eve White', 'Frank Miller', 'Grace Ho', 'Hank Hill'],
    'Product': ['Laptop', 'Mouse', 'Mouse', 'Tablet', 'Laptop', 'Tablet', 'Monitor', 'Mouse', 'Laptop'],
    'Price': [1200, 25, 25, 300, 1200, np.nan, 200, 25, 50000],
    'Quantity': [1, 2, 2, 1, 1, 2, 1, 3, 1]
}

df = pd.DataFrame(data)
print(df)

df['Customer'] = df['Customer'].str.strip().str.title()
print("=========================")
print(df)
