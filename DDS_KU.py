import numpy as np
import matplotlib.pyplot as plt

# DDS Parameters
fs = 1e3 # Sampling rate (Hz)
f_out = 123 # Desired uoutput frequency (Hz)
N = 1024 # Number of samples
acc_width = 32 # Phase accumulator bits
lut_size = 1024 # LUT length

# Build LUT
lut = np.sin(2*np.pi*np.arange(lut_size)/lut_size)

# Integer phase increment
phase_inc = int(round(f_out/fs * 2**acc_width))
phase_acc = 0
mask = 2**acc_width - 1
shift = acc_width - int(np.log2(lut_size))

output = np.zeros(N)
for i in range(N):
    phase_acc = (phase_acc + phase_inc) & mask
    idx = phase_acc >> shift
    output[i] = lut[idx]

# Plot
t = np.arange(N)/fs
plt.plot(t, output)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title(f'DDS Output — f_out={f_out} Hz')
plt.grid(True)
plt.show()
