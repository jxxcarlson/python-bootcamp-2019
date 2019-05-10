# Generating Audio

In this folder you will find some Python code for generating audio. We first discuss some theory: (a) what is sound, and how might we represent it digitally, (b) frequency and the sample rate, (c) how can a digitial representation be stored in a binary file (a `.wav` file).


## Representing sound

 The basic idea is as follows.  Sound waves are longitudinal wayes of compression and rarefication of air pressure.  A graph of the air pressure *y(t)* at a fixed location might look like what you see in the figure below. We have graphed pressure versus time, where `y(t) = 10*pi*sin(t)`

![Image](image/sine.png)


To represent sound digitally, one *samples* it, recording the values of *y(t)* at regular intervals.  Here are the first seven samples:

```
   [0.0, 0.309, 0.588, 0.809, 0.951, 1.0, 0.951, ...]
```

They were created as follows.  First, use `numpy` to create an array of regularly spaced points on the t-axis (the *sample points*):

```
import numpy as np
t = np.arange(0.0, 2.01, 0.01)
# [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, ...]
```

In this case the spacing is at intervals of *0.01* units. We then apply the function `t -> np.sin(10*np.pi*t)` to the array of samples.

```
y = np.sin(10*np.pi*t)

```

One can then plot the graph of pressure versus time and save it in an image file, as in the code fragment below.

```
plt.plot(y) 
plt.savefig('sine.png')
```

## Frequency and the sample rate

Fine, we can represent sound digitally by sampling the waveform to get an array of numbers, the sampled wave amplitudes. Standard audio playback software uses a sample rate of 44100 Hertz.   Thus, for every second of generated sound, we must "record" 44100 samples.  Let's do this for a pure sine wave of 440 Herz — the frequency of the standard tuning fork used by musicians.  Here is a code fragment

```
Fs = 44100                    ## Sampling Rate
f = 440                       ## Frequency (in Hz)
sample = 44100                ## Number of samples
t = np.arange(sample)         ## Sample times

y = 100*np.sin(2 * np.pi * f * t / Fs)
```


## Saving samples to a file
