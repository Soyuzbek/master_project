# -*- coding: utf-8 -*-
from scipy import signal
from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi, cos

fs = 2000
t = np.arange(0, 0.2, 1/fs)  # time(s) t e [0, 0.2] seconds
num_plot = 5
# carier wave
Ac = 1
Fc = 50
Pc = 0
carier = Ac * cos(2*pi*Fc*t + Pc)
plt.subplot(num_plot, 1, 1)
plt.plot(t, carier)
plt.xlabel('Time(s)')
plt.ylabel('Carier wave')


# message wave
Am = 1
Fm = 5
Pc = 0.5
message = Am * signal.sawtooth(2*pi*Fm*t, Pc)
plt.subplot(num_plot, 1, 2)
plt.plot(t, message)
plt.xlabel('Time(s)')
plt.ylabel('Message wave')


# Amplitude modulation case
a_modulated = carier * (1 + message/Ac)
plt.subplot(num_plot, 1, 3)
plt.plot(t, a_modulated)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude Modulation')

# Frequency modulation case
b = 5  # modulation index
integrated = np.asarray([quad(signal.sawtooth, 0, 2*pi*Fm*b, args=(Pc,))
                         for b in t])
integrated = integrated[:, 0]
f_modulated = Ac * cos(2*pi*Fc*t + b*integrated)
plt.subplot(num_plot, 1, 4)
plt.plot(t, f_modulated)
plt.xlabel('Time(s)')
plt.ylabel('Frequency Modulation')


# Phase modulation case
b = 3*Am  # modulation index
p_modulated = Ac * cos(2*pi*Fc*t + b*message)
plt.subplot(num_plot, 1, 5)
plt.plot(t, p_modulated)
plt.xlabel('Time(s)')
plt.ylabel('Phase Modulation')

#plt.tight_layout()
