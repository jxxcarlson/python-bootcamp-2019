# This Python code generates a sine wave at 440 Herz and saves it
# to `a440-sine.wav`.  To generate other sounds, modify the line
# where the samples are computed:
#
#       samples = VOLUME*np.sin(2 * np.pi * freq * t / SAMPLERATE)
#
# Note the parameters VOLUME, DURATION, SAMPLERATE.  The VOLUME parameters
# should not exceed 255.  The DURATION is in secondes.  SAMPLERATE should
# not be changed.  Generating a 3 second `.wav` file took 7.3 seconds,
# of which 3.6 seconds was CPU time.

# I used two sources in writing this code, namely (1) and (2) below.
# (1) https://thehackerdiary.wordpress.com/2017/06/09/it-is-ridiculously-easy-to-generate-any-audio-signal-using-python/
# (2) https://soledadpenades.com/posts/2009/fastest-way-to-generate-wav-files-in-python-using-the-wave-module/

import struct
import numpy as np
import struct
import wave

FREQUENCY = 440             # Hertz
AMPLITUDE = 255             # Max 255
DURATION = 2                # seconds
SAMPLERATE = 44100          # Don't change
FILENAME = 'sine.wav'       # up to you

# Construct an array of N integers,
# 0, 1, ... , SAMPLESIZE - 1
SAMPLESIZE = SAMPLERATE * DURATION                           ## Sampling Rate
index = np.arange(SAMPLESIZE)

# Construct an array of samples.
# Note the dimensions: FREQUENCY is in Hertz, SAMPLERATE is in Hertz,
# the elements of `index` are integers, hence dimensionless, as is n=`np.pi`
# Therefore the argument of the `sin` function is dimensionless,
# as it should be.
samples = AMPLITUDE*np.sin(2 * np.pi * FREQUENCY * index / SAMPLERATE)

# Open a .wav file and set its parameters so that standard
# program can read it, that is: play it!
output = wave.open(FILENAME, 'w')
# parameters: (nchannels, sampwidth, framerate, nframes, comptype, compname),
output.setparams((2, 2, SAMPLERATE, 0, 'NONE', 'not compressed'))

# Write the samples to hte file in the correct format
for s in samples:
    packed_value = struct.pack('h', s)
    output.writeframes(packed_value)
    output.writeframes(packed_value)

# Tidy up!
output.close()
