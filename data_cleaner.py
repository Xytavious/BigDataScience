import pandas as pd
import csv
import statistics


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
#op= statistics.stdev(df,1)
#print(op)
#std_dev = statistics.stdev(df)
#print(std_dev)
print()
