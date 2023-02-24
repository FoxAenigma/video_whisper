import whisper
import datetime
import math

model = whisper.load_model("base")
result = model.transcribe("Introduction.mp3")
segments = result["segments"]

def timestamp(seconds): return str(datetime.timedelta(seconds=int(math.modf(seconds)[1])))+',000'
with open("subs.srt", "a") as subs:
    i = 1
    for seg in segments:
        subs.write(str(i)+'\n')
        subs.write(f'{timestamp(seg["start"])} --> {timestamp(seg["end"])}'+'\n')
        subs.write(seg["text"]+'\n')
        subs.write(""+'\n')
        i += 1
