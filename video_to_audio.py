import ffmpeg
import moviepy
import sys
import subprocess
from datetime import timedelta

# input_path = "5320_480p_1.mp4"
# output_path = "audio_clip.m4a"

# def convertation(input_path,output_path):
#     duration = subprocess.check_output(
#         ["ffprobe", "-v", "error", "-show_entries", "format=duration",
#         "-of", "default=noprint_wrappers=1:nokey=1", input_path]
#     ).decode().strip()

#     cmd = [
#         "ffmpeg",
#         "-y",
#         "-i", input_path,
#         "-vn",                 # без видео
#         # "-acodec", "aac",     # копировать аудио
#         "-af", "loudnorm",
#         "-ar","44100",
#         "-movflags",
#         "+faststart",
#         "-map", "a",
#         "-t", duration,
#         output_path
#     ]

#     subprocess.run(cmd, check=True)

def convertation(input_path,output_path,number_of_chapters=1):
    duration = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", input_path]
    ).decode().strip()

    timecodes=[str(timedelta(seconds=int(float(duration)*(i/number_of_chapters) ))).zfill(8) for i in range(number_of_chapters+1)]
    print(timecodes)
    out=output_path.rsplit('.',1)

    for i in range(number_of_chapters):
        cmd = [
            "ffmpeg",
            "-y",
            "-i", input_path,
            '-ss', timecodes[i],
            '-to', timecodes[i+1],
            "-af", "loudnorm",
            "-ar","44100",
            "-movflags",
            "+faststart",
            "-map", "a",
            f'_{i+1}_.'.join(out)
        ]

        subprocess.run(cmd, check=True)

# tay=4
# tau='as.dasd.mpe'
# for i in range(tay):
#     print(f'{i}.'.join(tau.rsplit('.',1)))

# duration=28123
# number_of_chapters=5
# timecodes=[str(timedelta(seconds=int(duration*(i/number_of_chapters) ))).zfill(8) for i in range(number_of_chapters+1)]
# print(timecodes)