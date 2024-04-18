import pandas as pd
 
df = pd.read_csv('dataset/Automated_Traffic_Volume_Counts.csv', nrows=3)
# t = df.iloc[0]['WktGeom']
print(df.info())
