import sys
import math
import wave
import array

DURATION = 3
FREQUENCY = 440
VOLUME = 100
SAMPLERATE = 44100
DATASIZE = 2
CHANNEL = 2
RANGE = (2 << 14) - 1

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage ./{} [sine/triangle/square]".format(sys.argv[0]))
        exit(1)

    data = array.array('h')
    fpr = int(SAMPLERATE / FREQUENCY)
    samples_length = SAMPLERATE * DURATION * CHANNEL
    mode = sys.argv[1]
    if not mode in ['triangle', 'sine', 'square']:
        print("mode is must be 'triangle', 'sine' or 'square'")
        exit(1)

    for i in range(samples_length):
        sample = RANGE * float(VOLUME) / 100
        if mode == 'sine':
            sample *= math.sin(math.pi * 2 * (i % fpr) / fpr)
        elif mode == 'triangle':
            sample *= abs((i % fpr) - fpr / 2) / float(fpr)
        elif mode == 'square':
            sample *= 1 if i % fpr < fpr / 2 else 0
        data.append(int(sample))

    f = wave.open('{}.wav'.format(mode), 'w')
    f.setparams((CHANNEL, DATASIZE, SAMPLERATE, samples_length, "NONE", "Uncompressed"))
    f.writeframes(data.tostring())
f.close()
