import pandas as pd
import csv
import statistics


#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', None)
# df.to_string(index=False)


# start to something

df = pd.read_csv('world_population.csv')
#print(data)
df = df.dropna()                                                                                                                  
print(df.head())
print(df.info())
print(df.describe())
we = statistics.median(df)
print(we)
#op= df.std()
#print(op)
#print(op)
#std_dev = statistics.stdev(df)
#print(std_dev)
#print(df.mode())

#std_col6 = df['col6'].std()
#print("\nStandard deviation for col1:\n", std_col6)
