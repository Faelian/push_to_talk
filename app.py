#!/usr/bin/env python3
#coding: utf-8

import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100 # Sample rate
seconds = 3

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
print("Recording...")
sd.wait() # Wait until recording is finished
write('output.wav', fs, myrecording) # Save as WAV file

print("Finished !")
