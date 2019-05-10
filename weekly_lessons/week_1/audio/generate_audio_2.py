# I used two sources in writing this code, namely (1) and (2) below.
# (1) https://thehackerdiary.wordpress.com/2017/06/09/it-is-ridiculously-easy-to-generate-any-audio-signal-using-python/
# (2) https://soledadpenades.com/posts/2009/fastest-way-to-generate-wav-files-in-python-using-the-wave-module/

import struct
import numpy as np
import struct
import wave

DURATION = 3
SAMPLERATE = 44100

# Construct an array of sample times
n_samples = SAMPLERATE * DURATION                           ## Sampling Rate
t = np.arange(n_samples)

# Construct an array of samples.
# In this case at hand, samples are taken from
# a sine wave operating at 440 Herz
freq = 880  ## Frequency (in Hz)
samples = 100*np.sin(2 * np.pi * freq * t / SAMPLERATE)

output = wave.open('test.wav', 'w')
output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

for s in samples:
    packed_value = struct.pack('h', s)
    output.writeframes(packed_value)
    output.writeframes(packed_value)

output.close()
