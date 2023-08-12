# ascii-audio
I'm serious... You play sound with ASCII lol

# Examples of decoded audio
https://github.com/Ubuntufanboy/ascii-audio/assets/82414370/15b5c198-cb9b-4e17-8c77-6a48eb3a4afa

# Install

If you want to try it out yourself you can install it like this
``git clone https://github.com/Ubuntufanboy/ascii-audio``
Then run
``cd ascii-audio``
At this point you are going to want to find some audio and name it full.wav

**WARNING: You need to set the video sample rate to 4000 because your computer will crash with higher quality**
You can do this in audacity by following these steps
1. Import some audio
2. selecting all of the audio with the select button
3. clicking on ``Tracks``
4. Clicking on ``Resample``
5. Setting to 4000
6. Exporting the audio as wav and set file name to ``full.wav`` and make sure the audio is signed 16 bit PCM
7. Make sure the audio is in the ``ascii-audio`` directory
8. Continue following the instalation guide

After that run
``python3 encode.py``
This will take a while depending on your hardware and the length of the video. Be pateint!
Then run ``python3 decode.py``
After that you should have a file named ``decoded.wav`` which you can play with any audio player

# Contributing

This program was made as a joke but feel free to fix any bugs you encounter or make an issue and I'll fix it
