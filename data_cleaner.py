import pandas as pd
import csv


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
# df.to_string(index=False)


# start to something
data = pd.read_csv('world_population.csv').to_string().strip()
print(data)




