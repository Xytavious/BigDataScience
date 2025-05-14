import pandas as pd
import csv


#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', None)
# df.to_string(index=False)


# start to something

data = df = pd.read_csv('world_population.csv')
#print(data)
df = df.dropna()                                                                                                                  
print(df.head())
print(df.info())
print(df.describe())

print()



