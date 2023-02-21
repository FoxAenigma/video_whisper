import whisper
import os
import sys 
import argparse
import torch
import moviepy.editor as mp

from config import DEFAULT

def target_check(generator):
  def inner():
    parser = generator()
    space, _ = parser.parse_known_args()
    conditions = sum(map(lambda value: 0 if value == None else 1, [space.file, space.folder]))
    if conditions != 1:
      sys.exit("Incorrect arguments")
  return inner


@target_check
def init_parser():
  parser = argparse.ArgumentParser(description = "Whisper aplication to sub video")
  parser.add_argument(
  	'--model',
    type = str,
    nargs = 1,
    required = False,
  )
  
  parser.add_argument(
  	'--device',
    type = str,
    nargs = 1,
    required = False,
  )
  
  parser.add_argument(
  	'--language',
    type = str,
    nargs = 1,
    required = False,
  )
  
  
  parser.add_argument(
  	'--translate',
    type = str,
    nargs = '+',
    required = False,
  )
  
  parser.add_argument(
  	'--folder',
    type = str,
    nargs = 1,
    required = False,
  )
  
  parser.add_argument(
  	'--file',
    type = str,
    nargs = 1,
    required = False,
  )

  return parser

def extract_audio(base: str, video_file: str):
  name, _ = video_file.split('.')
  video = mp.VideoFileClip(video_file)
  video.audio.write_audiofile(f"{base}/{name}.mp4")
  return


if __name__ == "__main__":
  parser = init_parser()