import pandas as pd 

data = pd.read_csv("wages_hours.csv", sep = "\t")

print(data.head(10))