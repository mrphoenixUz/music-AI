# -*- coding: utf-8 -*-
"""music-AI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XWgGX6QHzIv9kpwFQFihFSHi3Xc1AzIZ
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def generate_spectrogram(wav_file):
    # Read the WAV file
    sample_rate, data = wavfile.read(wav_file)

    # Check if data is stereo or mono
    if len(data.shape) > 1:
        data = data[:, 0]  # Use one channel if stereo

    # Create a spectrogram
    plt.figure(figsize=(12, 6))
    plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='inferno')

    plt.title(f'Spectrogram of {wav_file}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    plt.xlim(0, len(data) / sample_rate)  # Set x-axis limit
    plt.ylim(0, sample_rate / 2)           # Frequency range from 0 to Nyquist frequency
    plt.grid(True)
    plt.show()

# Example usage
wav_file_path = './music/music1.wav'  # Replace with your WAV file path
generate_spectrogram(wav_file_path)

wav_file_path2 = './music/music2.wav'  # Replace with your WAV file path
generate_spectrogram(wav_file_path2)

wav_file_path3 = './music/music3.wav'  # Replace with your WAV file path
generate_spectrogram(wav_file_path3)

pip install gtts

from gtts import gTTS
import os

# Matnni belgilash
text = "Hi guys that is me Phoenix"

# Ovoz yaratish (gTTS - Google Text-to-Speech)
language = 'en'  # Changed to English ('en')
tts = gTTS(text=text, lang=language, slow=False)

# Ovoz faylini saqlash
audio_file = "./music/music1.wav"
tts.save(audio_file)

# Ovoz faylini tinglash (Google Colab-da)
from IPython.display import Audio
Audio(audio_file)