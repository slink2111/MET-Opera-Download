# MET-Opera-Download
**Python 3** script which downloads MET Opera streams from metopera.org

The free streams are available during the corova virus period

You only have to enter a url for the video stream the audio stream and the subtitles stream, you can obtain them from the network tool of the developer options of firefox while you play the stream.
![Firefox Network](/Capture.png)
For the subs you have to look for a "vtt" file 
for the audio and video check for "mp2t" files, the size of each file will hint you which one is the video (larger ones)

Just enter the links from any files (doesn't have to be the first in order) of the stream and it will work. Do not forget all 3 file types should have links in order to work.

Prerequests except of a python lib or two that you need to install, is the ffmpeg.exe you can get it from https://www.ffmpeg.org/download.html. Place the .exe in the same folder as the python script.

also the joiner.bat needs to be in the same dir as the main.py
