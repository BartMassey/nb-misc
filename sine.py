# Copyright © 2014 Bart Massey
# Sinusoid generator for audio.

from math import sin, pi

# Sample rate of audio system in samples/sec.
sps = 96000

def make_note(freq, duration):
    samples = round((sps * duration)) * [0]
    for s in range(len(samples)):
        t = s * freq * 2 * pi / sps
        samples[s] = sin(t)
    return samples

for s in make_note(440, 0.1):
    print(s)
