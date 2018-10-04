#!/usr/bin/python
#-*- encoding:utf-8 -*-
import os
from pydub import AudioSegment
import sys

target=raw_input("Album folder location:")
os.chdir(target)
flist=os.listdir(os.getcwd())
flist.sort()

for song in flist:
  ext=song.split(".")[-1]
  cmd="ffmpeg -i '%s' -nostats -loglevel 0 -codec:a libmp3lame -qscale:a 0 '%s.mp3'" %(song,song.replace(".%s" %(ext),""))
  os.popen(cmd)
  sys.stdout.write('\rConverting file:(%s)' %(song))
  sys.stdout.flush()
print "\nDone"
