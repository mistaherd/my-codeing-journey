import random
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import signal

#representing cos(x+phi)=cos(x)cos(phi)+cos(x +1/2pi)sin(phi)
a=np.random.randint(2,size =100)
time=np.random.randint(1,10000)
b=np.random.randint(1,5)
b1=np.random.randint(1,6)
phi=90
#sin(phi)
a1 = a*np.sin(2*np.pi*time)
a2 = a*np.cos(2*np.pi*time)
I = a*np.sin(2*np.pi)
Q = a*np.cos(2*np.pi)
vi=I*a1
vq=Q*a2
vo=vi+vq
plt.plot(vo)
plt.title("output of I&Q modulator")
plt.ylabel("frequency(kHz)")
plt.xlabel("relative amplitude")
plt.show()

a0=abs(np.fft.fft(vo)/len(vo))

plt.plot(np.fft.fftshift(a0))
plt.title("FFT of  output of I&Q modulator")
plt.ylabel("frequency(kHz)")
plt.xlabel("relative amplitude")
plt.show()

plt.plot(a1)
plt.title("input of I&Q signal Q signal")
plt.ylabel("amplitude")
plt.xlabel("time")
plt.show()

plt.plot(a2)
plt.title("input of I&Q signal I signal")
plt.ylabel("amplitude")
plt.xlabel("time")
plt.show()

a3=abs(np.fft.fft(a1)/len(a1))

plt.plot(np.fft.fftshift(a3))
plt.title("FFT of  input of I signal")
plt.ylabel("frequency(kHz)")
plt.xlabel("relative amplitude")
plt.show()

a4=abs(np.fft.fft(a2)/len(a2))
plt.plot(np.fft.fftshift(a4))
plt.title("FFT of input of Q signal")
plt.ylabel("frequency(kHz)")
plt.xlabel("relative amplitude")
plt.show()