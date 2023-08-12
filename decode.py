import numpy
import wave
from num2txt import Convert

with open("asciiaudio.txt", 'r') as f:
    INPUT_STRING = f.read()
SUBSTRING_LENGTH = 3

# Using a list comprehension to create the list of substrings
SUBSTRINGS = [INPUT_STRING[i:i+SUBSTRING_LENGTH] for i in range(0, len(INPUT_STRING), SUBSTRING_LENGTH)]

numbers = []

for SUBSTRING in SUBSTRINGS:
    converter = Convert(SUBSTRING)
    converter.fromtxt()
    numbers.append(converter.num)

numbers = [num - 128 for num in numbers]

numbers = numpy.array(numbers, dtype=numpy.int8)

with wave.open("decoded.wav", 'wb') as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(48210)
    wav_file.writeframes(numbers.tobytes())