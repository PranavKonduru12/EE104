import pandas as pd
import matplotlib.pyplot as plt

#plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True



#df = pd.read_csv('student.csv', names=headers)
#CSV file reading

#headers = ['Date', 'Total_cases', 'New_cases']
df = pd.read_csv('/Users/pranavkonduru/Local_GIt_Repos/EE104_Projects/Lab6_EE104/lab_6_konduru_pranav/task2_trendPrediction/COVID-19_case_counts_by_date.csv',parse_dates = ['Date'])

#print(df)

df['Total_cases'] = df['Total_cases'].astype(int)

#print(df)

df['New_cases'] = df.New_cases.astype(int)

#f = plt.figure(figsize=(10, 10))
df.plot(x='Date',y='Total_cases') # figure.gca means "get current axis"
plt.title('Covid19 Totals cases', color='black')
plt.tight_layout()
plt.show()

df.plot(x='Date',y='New_cases') # figure.gca means "get current axis"
#plt.title('Covid19 New Cases', color='black')
plt.tight_layout()
plt.show()

