import math as m
from random import sample
import numpy as np 
#import scipy.integrate as integ
import matplotlib.pyplot as plt
from scipy import fftpack, signal
#from scipy import signal
import warnings

#Generate signal
np.random.seed(1234) #Random seed generator

time_step = 0.02
period = 5

time_vec = np.arange(0, 20, time_step)
sig = (np.sin(2 * np.pi / period * time_vec) + \
    0.5 * np.random.randn(time_vec.size))

plt.figure(figsize=(6, 5))
plt.plot(time_vec, sig, label='Original signal')
#plt.show()

# Compute and plot power
sig_fft = fftpack.fft(sig) # fft of the signal
#print(sig_fft)
power  = np.abs(sig_fft)**2 # power 
sample_freq = fftpack.fftfreq(sig.size, d=time_step) #corresponding frequency

# Plotting FFT power
plt.figure(figsize=(6, 5))
plt.plot(sample_freq, power)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Power')
#plt.show()

# Peak frequency: focus on only positive frequencies
pos_mask = np.where(sample_freq > 0)
freqs = sample_freq[pos_mask]
peak_freq = freqs[power[pos_mask].argmax()]

# Check that the peak correspond with signal
np.allclose(peak_freq, 1./period)

# Inner plot to show the preak frequency
axes = plt.axes([0.55, 0.3, 0.3, 0.5])
plt.title('Peak frequency')
plt.plot(freqs[:8], power[:8])
plt.setp(axes,yticks=[])
plt.show()
# Remove all high frequencies
warnings.filterwarnings('ignore')
#%matplotlib inline
high_freq_fft = sig_fft.copy()
high_freq_fft[np.abs(sample_freq) > peak_freq] = 0
filtered_sig = fftpack.ifft(high_freq_fft)

plt.figure(figsize=(6, 5))
plt.plot(time_vec, sig, label = 'Original signal')
plt.plot(time_vec, filtered_sig, linewidth=3, label = 'Original signal')
plt.xlabel('Time [Hz]')
plt.ylabel('Amplitude')

plt.legend(loc='best')
plt.show()
# Using scipy filter to remove high frequencies
t = time_vec
b, a = signal.butter(3, 0.05) # 3 order butterworth lowpass filter
zi = signal.lfilter_zi(b, a)   # Applying filter to sig
z,_ = signal.lfilter(b, a, sig, zi=zi*sig[0])
z2,_ = signal.lfilter(b, a, z, zi=zi*z[0])# Apply filter again, to have a result filtered at the same order
                                            # as filtfit
y = signal.filtfilt(b, a, sig) # filtfit to apply filter 
plt.figure
plt.plot(t, sig, 'b', alpha=0.75) # Plot the original signal
plt.plot(t, z, 'g', t, z2, 'r', t, y, 'k')
plt.legend(('noisy signal', 'lfilter, once', 'lfilter, twice', 'filtfilt'), loc='best')
plt.grid(True)
plt.show()

#print(freq)
# Read y column as a list
#for index in sound.iterrows():
#y = sound['M'].tolist()
#sound['M'] = sound['M'].astype(float)
#for index in sound.iterrows():
#    x = np.abs(sound.loc[index, 'M'])**2
#print(x)
#print(sound.dtypes)
#power = np.abs(y)**2
#y = sound['M']
#print(y)
#sign_fft = fftpack.fft(sound)
#print(sign_fft)
#power = np.abs(sign_fft)**2
#print(power)
#sample_freq = fftpack.fftfreq(sound['M'].size, d=0.05)
#print(sample_freq)
#print(sample_freq)
#print(sig_fft)

#print(freq)

#sound.plot(x='X',y='M') # figure.gca means "get current axis"
#plt.xlabel('Frequency [Hz]')
#plt.ylabel('Power')
#plt.title('audiocheck.net_sweep_10Hz_10000Hz_-3dBFS_1s_Output_mono.csv', color='black')
#plt.tight_layout()
#plt.show()

#Innter plot to show peak frequency
#axes = plt.axes([0.02, 0.01, 0.01, 0.02])
#plt.title('Peak Frequency')
#plt.plot(power[0][:8], power[1][:8])
#plt.setp(axes, yticks=[])
#plt.show()

