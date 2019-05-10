import wave
import random
import struct

SAMPLE_LEN = 132300

noise_output = wave.open('noise.wav', 'w')
noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

for i in range(0, SAMPLE_LEN):
    value = random.randint(-32767, 32767)
    packed_value = struct.pack('h', value)
    noise_output.writeframes(packed_value)
    noise_output.writeframes(packed_value)

noise_output.close()
