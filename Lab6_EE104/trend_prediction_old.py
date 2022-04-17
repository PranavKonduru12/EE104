import pandas as pd
import matplotlib.pyplot as plt

#plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True



#df = pd.read_csv('student.csv', names=headers)
#CSV file reading

headers = ['Date', 'Total_cases', 'New_cases']
df = pd.read_csv(
    '/Users/pranavkonduru/Local_GIt_Repos/EE104_Projects/Lab6_EE104/lab_6_konduru_pranav/task2_trendPrediction/COVID-19_case_counts_by_date.csv',parse_dates=     {"Dt" : [0]},names=headers)

#df['Date'] = pd.to_datetime(df['Date'])

#df['Date'] = df['Date'].astype(float)

#df['Total_cases'] = int(df['Total_cases'])
#df['Total_cases']=df.Total_cases.astype(float)

#df['New_cases'] = int(df['New_cases'])
df['New_cases'] = df.New_cases.astype(float)

t=df.dtypes

print(t)

#f = plt.figure(figsize=(10, 10))
#df.plot(x='Dt',y='Total_cases') # figure.gca means "get current axis"
#plt.title('Title here!', color='black')
#plt.tight_layout()
#plt._show()




#def risk_analysis():
#    for row in df.iterrows():        # iterates through the rows of the csv file
#        #Conditions that will be used to place risk value
#        print(row['Total_cases'])
        #print((row['Risk']))
#float(df.set_index('Total_cases')).plot()

#plt.show()
