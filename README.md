ASVS (Audio Spectrum Visualising System)



Required packages (possibly some are not mentioned)
-python 1/2/3
-python2-tools
-python alsaaudio
-python wave
-python struct
-python numpy
-python setuptools
-alsa-lib
-alsa-tools
-alsa-utils
-ffmpeg
-gcc
-Python RPIO



Source code found in Documentation/Source/play.py
Sample wav files are found in Documentation/Implementation/Media/


Current Usage:

$ python play.py    AUDIO_FILE_PATH_HERE

-Notice that only ".wav" files can be played
-Also due to UI inexperience, the CLI window will be to be adjusted to the size of the 
data being printed to avoid bad looking new prints (due to new-line each iteration) 
there connecting remotely (i.e. ssh) is recommended.

-Notice that as of the current implementation the program finishes with a ValueError 
(Can be solved)


