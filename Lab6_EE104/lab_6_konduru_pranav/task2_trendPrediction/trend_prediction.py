import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

#headers = ['Date', Total_cases', 'New_cases']



#df = pd.read_csv('student.csv', names=headers)
#CSV file reading
df = pd.read_csv(
    r'C:\Users\pskon\workBenchRepo\EE104\Lab6_EE104\lab_6_konduru_pranav\task2_trendPrediction\COVID-19_case_counts_by_date.csv')

def risk_analysis():
    for row in df.iterrows():        # iterates through the rows of the csv file
        #Conditions that will be used to place risk value
        print(row['Total_cases'])
        #print((row['Risk']))
#float(df.set_index('Total_cases')).plot()

#plt.show()
