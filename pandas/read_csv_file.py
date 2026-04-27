import pandas as pd
FILE_PATH = './files/person-data.csv'

df = pd.read_csv(FILE_PATH)

print("df -->>", df.head(3))
print("df.to_string -->>", df.to_string())