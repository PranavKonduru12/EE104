import pandas as pd

#CSV file read here
#Need to add in filepath of csv file
df = pd.read_csv(
    r'/Users/pranavkonduru/Local_GIt_Repos/EE104_Projects/Lab6_EE104/lab_6_konduru_pranav/task1_riskFactor/ratings.csv')


df['Risk'] = ' '         # Add nenw column

#fills in the new column with the risk values
def risk_analysis():
    for index, row in df.iterrows():        # iterates through the rows of the csv file
        #Conditions that will be used to place risk value
        if float(df.loc[index, 'COSTTOINCOME']) <= 0.5:
            df.loc[index, 'Risk'] = 'Low'
        elif float(df.loc[index, 'COSTTOINCOME']) <= 1:
            df.loc[index, 'Risk'] = 'Medium'
        else:
            df.loc[index, 'Risk'] = 'High'
        #print((row['Risk']))

#All functions called here
def main():
    risk_analysis()
    #Column written onto new csv file
    df.to_csv(
        r'/Users/pranavkonduru/Local_GIt_Repos/EE104_Projects/Lab6_EE104/lab_6_konduru_pranav/task1_riskFactor/ratings_updated.csv', index=False)

main()