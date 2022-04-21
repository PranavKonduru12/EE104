#import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy import fftpack

#Need to figure out how to remove absolute path
sound = pd.read_csv('/Users/pranavkonduru/Local_GIt_Repos/EE104_Projects/lab7_konduru_pranav/task1/audiocheck.net_sweep_10Hz_10000Hz_-3dBFS_1s_Output_mono.csv')
#sound = pd.read_csv(r'Path where csv file is stored\audiocheck.net_sweep_10Hz_10000Hz_-3dBFS_1s_Output_mono.csv')

#print(sound)

#Frequencies
freq = fftpack.fftfreq(sound.size, d=0.01)

print(freq)
# Read y column as a list
#for index in sound.iterrows():
y = sound['M'].tolist()

#print(y)

#print(freq)

#sound.plot(x='X',y='M') # figure.gca means "get current axis"
#plt.plot(freq, y)
#plt.title('audiocheck.net_sweep_10Hz_10000Hz_-3dBFS_1s_Output_mono.csv', color='black')
#plt.tight_layout()
#plt.show()