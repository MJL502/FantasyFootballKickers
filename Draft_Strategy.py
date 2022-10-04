import pandas as pd

df = pd.read_csv (r'C:\Users\mjlaw\source\repos\FantasyFootballKickers\data\historical_field_goal_data.csv')   

#read the csv file (put 'r' before the path string to address any special characters in the path, such as '\')

print(df)