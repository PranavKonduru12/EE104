#from tkinter import *
#from collections import UserString
from tkinter import W
#from openpyxl import *
import pandas as pd

df = pd.read_csv(
    '/Users/pranavkonduru/Local_GIt_Repos/EE104_Projects/Lab6_EE104/lab#6_konduru_pranav/task1_riskFactor/ratings.csv')

#df['Risk'] = ' '         # Add nenw column
# To remove column
#df.drop('new_column', inplace=True, axis=1)
df['Risk'] = ' '         # Add nenw column
def risk_analysis():
    for index, row in df.iterrows():
        #print(float(row['COSTTOINCOME']), float(row['ROE']))
        if float(df.loc[index, 'COSTTOINCOME']) <= 0.5:
            df.loc[index, 'Risk'] = 'Low'
        elif float(df.loc[index, 'COSTTOINCOME']) <= 1:
            df.loc[index, 'Risk'] = 'Medium'
        else:
            df.loc[index, 'Risk'] = 'High'
        #print((row['Risk']))

def main():
    risk_analysis()
    df.to_csv(
        '/Users/pranavkonduru/Local_GIt_Repos/EE104_Projects/Lab6_EE104/lab#6_konduru_pranav/task1_riskFactor/ratings_updated.csv', index=False)

main()