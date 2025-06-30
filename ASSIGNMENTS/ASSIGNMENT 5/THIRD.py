import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 28],
    "Score": [85, 90, 95, 88]
})

print("Original DataFrame:\n", df)

# Different ways to iterate over rows
print("\nUsing iterrows():")
for idx, row in df.iterrows():
    print(f"Index {idx} - Name: {row['Name']}, Age: {row['Age']}")

print("\nUsing itertuples():")
for row in df.itertuples():
    print(f"Index {row.Index} - Name: {row.Name}, Age: {row.Age}")

# Selecting rows based on condition
adults = df[df["Age"] >= 30]
print("\nRows where Age >= 30:\n", adults)

# Select any row using iloc[]
third_row = df.iloc[2]
print("\nThird row using iloc[]:\n", third_row)

# Limited rows selection with given column
limited = df.loc[1:3, ["Name", "Score"]]
print("\nRows 1 to 3 with only 'Name' and 'Score' columns:\n", limited)

# Drop rows based on condition
df_dropped = df[df["Age"] != 30]
print("\nDataFrame after dropping rows where Age == 30:\n", df_dropped)

# Insert a row at a given position
new_row = pd.DataFrame({"Name": ["Eve"], "Age": [27], "Score": [92]})
df_inserted = pd.concat([df.iloc[:2], new_row, df.iloc[2:]]).reset_index(drop=True)
print("\nDataFrame after inserting a new row after index 1:\n", df_inserted)

# Create a list from rows
list_of_rows = df.to_dict("records")
print("\nList of rows as dictionaries:\n", list_of_rows)
