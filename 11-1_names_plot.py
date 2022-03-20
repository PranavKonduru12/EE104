#######################################################################
# This program finds and plot the statistics of given names 
# using a database of names and numbers of their occurrences. 
#######################################################################
#!/usr/bin/python3

import os
import matplotlib.pyplot as plt


BoysFromAllYears={}     # boy list
GirlsFromAllYears= {}   # girl list

def ObtainDataForEachYearInTheRange(YearNumber):  #read every single year
    FileName = "yob"+str(YearNumber)+".txt" # yob = year of birth
    DirName = "names_baby/"
    path=DirName+FileName
    GirlData={}
    GirlsFromAllYears[YearNumber]=GirlData
    BoyData={}
    BoysFromAllYears[YearNumber]=BoyData
#    print(DirName,FileName,path)  # this line is for debug
    with open(path,"r") as file:
        for line in file:
            line.strip()
            LineColumn=line.split(",")
            if LineColumn[1]=="F":
                GirlData[LineColumn[0]]=int(LineColumn[2])
            else:
                BoyData[LineColumn[0]]=int(LineColumn[2])

# build the list
def FindOneName(Gender,YearStart,YearEnd,Name):
    FoundResult=[]
    for YearNumber in range(YearStart,YearEnd+1):
        NameDictionary = Gender[YearNumber]
        if Name in NameDictionary:
            FoundResult.append(NameDictionary[Name])
        else:
            FoundResult.append(0)
    return FoundResult


                               

for EachYear in range(1882,2015):
    ObtainDataForEachYearInTheRange(EachYear)

#First way to plot by defining an intermediate result
FoundThisName=FindOneName(BoysFromAllYears,1882,2014,"Joseph")
plt.plot([x for x in range(1882,2015)],FoundThisName,color='green',  label='Joseph') # add marker='o' to see it

#Second way to plot
plt.plot([x for x in range(1882,2015)],FindOneName(GirlsFromAllYears,1882,2014,"Brittney") ,'r--', label='Brittney') 
plt.plot([x for x in range(1882,2015)],FindOneName(GirlsFromAllYears,1882,2014,"Stephanie") ,'b-', label='Stephanie')  

plt.ylabel('#')
plt.xlabel('Year')


legend = plt.legend(loc='upper left', shadow=True, fontsize='large')

#show all
plt.show()











