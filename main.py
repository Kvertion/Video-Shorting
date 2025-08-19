import ffmpeg
import moviepy
import whisper
import os
import pickle
import pandas as pd
import subprocess


vid_dir=os.listdir('videos')
list_of_videos=[i for i in vid_dir if 'mp4' in i]
list_of_audios=[f"{i.split('.')[0]}.m4a" for i in list_of_videos]

# input_path = 
# output_path = "audio_clip.m4a"


model = whisper.load_model("turbo")
result = model.transcribe("part1.m4a")
print(result["text"])

with open("whisper_result.pkl", 'wb') as f:
    pickle.dump(result,f)

df = pd.DataFrame(result["segments"])
df.to_csv("segments.csv", index=False)



















# нарезка
# cmd = [
#     "ffmpeg",
#     "-y",
#     "-i", "audio_clip.m4a",
#     "-ss", "00:30:00",      # начало
#     "-to", "00:31:00",      # конец
#     "-c", "copy",
#     "part1.m4a"
# ]
# subprocess.run(cmd, check=True)