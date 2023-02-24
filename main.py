import whisper
import os
from os import walk
import sys
import argparse
import torch
import moviepy.editor as mp
import datetime
import math
import soft_embedd

from config import DEFAULT

def init_parser():
  parser = argparse.ArgumentParser(description = "Whisper aplication to sub video")
  parser.add_argument(
  	'--model',
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

  return parser

def extract_audio(video_file: str):
  name = f'{video_file.replace(".mkv" , "")}.mp3'
  video = mp.VideoFileClip(video_file)
  video.audio.write_audiofile(name)
  return name

def audio_transcribe(audio: str, use_model: str):

  model = whisper.load_model(use_model)
  result = model.transcribe(audio)
  segments = result["segments"]

  subtitles = f'{audio.replace(".mp3" , "")}.srt'

  def create_srt_file(data, output_filename):
      with open(output_filename, 'w', encoding='utf-8') as f:
          for i, item in enumerate(data):
              start = datetime.timedelta(seconds=item['start'])
              end = datetime.timedelta(seconds=item['end'])
              start_srt = start_to_srt(start)
              end_srt = start_to_srt(end)
              f.write(str(i+1) + '\n')
              f.write(start_srt + ' --> ' + end_srt + '\n')
              f.write(item['text'] + '\n')
              f.write('\n')

  def start_to_srt(start):
      hours, remainder = divmod(start.seconds, 3600)
      minutes, seconds = divmod(remainder, 60)
      milliseconds = math.floor(start.microseconds / 1000)
      return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"
  
  create_srt_file(segments, subtitles)


  
def delete_audio(audio):
  os.remove(audio)
"""
def insert_subs():

"""

def process_video(parser, video):
  audio = extract_audio(video)
  audio_transcribe(audio, getattr(parser.parse_known_args()[0], "model")[0])
  delete_audio(audio)


if __name__ == "__main__":
  parser = init_parser()

  dir = getattr(parser.parse_known_args()[0], "folder")[0]
  res = []
  for (dir, dir_names, file_names) in walk(dir):
      res += list(map(lambda file: dir+ "/" + file if file.endswith('.mkv') else '', file_names))
      res = list(filter(('').__ne__, res))
  
  for video in res:
    process_video(parser, video)
