#import os
from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
from scipy import fftpack
import numpy as np

#Need to figure out how to remove absolute path
#sound = pd.read_csv(r'C:\Users\pskon\workBenchRepo\EE104\lab7_konduru_pranav\task1\audiocheck.net_sweep_10Hz_10000Hz_Negative3dBFS_1s_Output_mono.csv')
sound = pd.read_csv(r'C:\Users\pskon\workBenchRepo\EE104\lab7_konduru_pranav\task1\audiocheck.net_sweep_10Hz_10000Hz_Negative3dBFS_1s_Output_mono.csv')
#sound_y = pd.read_csv('C:\Users\pskon\workBenchRepo\EE104\lab7_konduru_pranav\task1\audiocheck.net_sweep_10Hz_10000Hz_Negative3dBFS_1s_Output_mono.csv'. usecols=[1])


#sound = pd.read_csv('/Users/pranavkonduru/Local_GIt_Repos/EE104_Projects/lab7_konduru_pranav/task1/audiocheck.net_sweep_10Hz_10000Hz_-3dBFS_1s_Output_mono.csv')
#sound = pd.read_csv(r'Path where csv file is stored\audiocheck.net_sweep_10Hz_10000Hz_-3dBFS_1s_Output_mono.csv')

#print(sound)

#print(freq)
# Read y column as a list
#for index in sound.iterrows():
#y = sound['M'].tolist()
sound['M'] = sound['M'].astype(float)
#for index in sound.iterrows():
#    x = np.abs(sound.loc[index, 'M'])**2
#print(x)
#print(sound.dtypes)
#power = np.abs(y)**2
#y = sound['M']
#print(y)
sign_fft = fftpack.fft(sound)
#print(sign_fft)
power = np.abs(sign_fft)**2
#print(power)
sample_freq = fftpack.fftfreq(sound['M'].size, d=0.05)
#print(sample_freq)
#print(sample_freq)
#print(sig_fft)

#print(freq)

#sound.plot(x='X',y='M') # figure.gca means "get current axis"
plt.figure(figsize=(6, 5))
plt.plot(sample_freq, power, label='signal')
#plt.xlabel('Frequency [Hz]')
#plt.ylabel('Power')
#plt.title('audiocheck.net_sweep_10Hz_10000Hz_-3dBFS_1s_Output_mono.csv', color='black')
plt.tight_layout()
plt.show()

#Innter plot to show peak frequency
#axes = plt.axes([0.02, 0.01, 0.01, 0.02])
#plt.title('Peak Frequency')
#plt.plot(power[0][:8], power[1][:8])
#plt.setp(axes, yticks=[])
#plt.show()

