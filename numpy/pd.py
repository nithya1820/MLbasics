import pandas as pd
import numpy as np
# Pandas DataFrame
df = pd.DataFrame(data={'A': [3, 2, 1], 'B': [6,5,4], 'C': [9, 8, 7]}, 
                  index=['i', 'j', 'k'])
print("Pandas DataFrame: ")
print(df)

# Convert Pandas DataFrame to NumPy Array
np_arr = df.to_numpy()
print("Pandas DataFrame to NumPy array: ")
print(np_arr)


# Convert specific columns of Pandas DataFrame to NumPy array
arr = df[['B', 'C']].to_numpy()
print("Convert B and C columns of Pandas DataFrame to NumPy Array: ")
print (arr)