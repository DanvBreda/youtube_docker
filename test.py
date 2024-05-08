
from pytube import YouTube
import ffmpeg, os, subprocess

location = 'files'
file_name = f'{location}/youtube_url.txt'

with open(file_name) as file:
    myList = filter(None, [i for i in file.read().strip().split('\n')])

for i in myList:
    print(i)

    if len(i) in myList <1:
        pass
    else:
        print(len(i))


