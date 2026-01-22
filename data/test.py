
import pandas

df = pandas.read_csv("weapons_list.csv")

# print(df.head())

# print(list(df.to_dict("records")[0].values()))

# print(type(df.to_dict("records")[0]["range_km"]))

print(df.info())

print(df.head())