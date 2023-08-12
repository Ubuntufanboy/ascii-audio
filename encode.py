import wave
import numpy as np
from num2txt import Convert

# Replace 'your_audio.wav' with the actual path to your WAV file
wav_file_path = 'full.wav'

# Open the WAV file in read mode
with wave.open(wav_file_path, 'rb') as wav_file:
    num_frames = wav_file.getnframes()       # Number of frames
    sample_width = wav_file.getsampwidth()   # Sample width in bytes

    # Read all the audio frames as bytes
    raw_audio_data = wav_file.readframes(num_frames)

print(num_frames)
print(sample_width)

# Convert the raw bytes to a NumPy array of int8
audio_array = np.frombuffer(raw_audio_data, dtype=np.int8)

pre_ascii_characters = [value + 128 for value in audio_array]

post_ascii_characters = []

for num in pre_ascii_characters:
    converter = Convert(num)
    converter.inttotxt()
    post_ascii_characters.append(converter.txt)

# Print the first few ASCII characters for demonstration
with open("asciiaudio.txt", 'w', encoding='utf-8') as f:
    f.write(''.join(post_ascii_characters))

