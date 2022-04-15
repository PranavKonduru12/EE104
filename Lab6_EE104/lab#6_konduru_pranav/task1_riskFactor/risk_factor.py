#from tkinter import *
from collections import UserString
from tkinter import W
#from openpyxl import *
import pandas as pd

df = pd.read_csv('/Users/pranavkonduru/Local_GIt_Repos/EE104_Projects/Lab6_EE104/lab#6_konduru_pranav/task1_riskFactor/ratings.csv')

df["new_column"] = " "
df.to_csv('/Users/pranavkonduru/Local_GIt_Repos/EE104_Projects/Lab6_EE104/lab#6_konduru_pranav/task1_riskFactor/ratings.csv', index=False)