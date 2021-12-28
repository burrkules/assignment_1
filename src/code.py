import pandas as pd

original_data = pd.read_csv("../data/raw/SCiBER.txt", sep="	")
original_data.head()
print(original_data.to_string())