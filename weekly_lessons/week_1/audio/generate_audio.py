# Source: https://pypi.org/project/wavio/
# File: gen_sound.py
# Run
#
#   $ python gen_sound.py
#
# to create the file `sine440.py
#
# Then run (for example on Mac OS)
#
#   $ afplay sine.wav
#
# to listen to the sound

import numpy as np
import wavio
from time import time

# Parameters
rate = 44100    # samples per second
T = 3           # sample duration (seconds)
f = 440.0       # sound frequency (Hz)

# Compute waveform samples
start = time()

t = np.linspace(0, T, T*rate, endpoint=False)
x = np.sin(2*np.pi * f * t)
end = time()
print "Compute waveform: ", round((end - start)*1000,2) , "ms"

# Write the samples to a file
start = time()

wavio.write("sine.wav", x, rate, sampwidth=3)

end = time()
print "Write file: ", round((end - start)*1000,2) , "ms"
