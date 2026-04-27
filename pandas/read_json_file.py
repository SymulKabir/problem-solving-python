import pandas as pd

df = pd.read_json('./files/sample_items.json')

print(df.to_string())