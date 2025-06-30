import pandas as pd

# DataFrames with common column 'ID'
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Value1': ['A', 'B', 'C']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Value2': ['X', 'Y', 'Z']
})

# Inner merge on 'ID'
inner_merge = pd.merge(df1, df2, on='ID', how='inner')
print("Inner Merge:\n", inner_merge)

# Left join on 'ID'
left_join = pd.merge(df1, df2, on='ID', how='left')
print("\nLeft Join:\n", left_join)

# Right join using merge()
right_merge = pd.merge(df1, df2, on='ID', how='right')
print("\nRight Join (merge):\n", right_merge)

# Join based on index
df1_indexed = df1.set_index('ID')
df2_indexed = df2.set_index('ID')
index_join = df1_indexed.join(df2_indexed, how='right')
print("\nRight Join (index-based join):\n", index_join)
