import pandas as pd

#create dataframes by two dimensional list
data = [["mayank", 20, "delhi"], ["sachin", 21, "mumbai"], ["sahil", 22, "bangalore"]]
df= pd.DataFrame(data, columns=["name", "age", "city"])
print(df)

#CREATE A DATAFRAME FROM A DICTIONARY
data = {"name": "mayank", "age": 20, "city": "delhi"}
df = pd.DataFrame([data])
print(df)

#CREATE A DATAFRAME FROM LISTS OF LISTS
data = [["mayank", 20, "delhi"], ["sachin", 21, "mumbai"], ["sahil", 22, "bangalore"]]
df = pd.DataFrame(data, columns=["name", "age", "city"])
print(df)

#CREATE A DATAFRAME FROM A LISTS OF DICTIONARIES
data = [{"name": "mayank", "age": 20, "city": "delhi"}, {"name": "sachin", "age": 21, "city": "mumbai"}, {"name": "sahil", "age": 22, "city": "bangalore"}]
df = pd.DataFrame(data)
print(df)

#CREATE A DATAFRAME FROM A LISTS OF TUPLES
data = [("mayank", 20, "delhi"), ("sachin", 21, "mumbai"), ("sahil", 22, "bangalore")]
df = pd.DataFrame(data, columns=["name", "age", "city"])
print(df)

