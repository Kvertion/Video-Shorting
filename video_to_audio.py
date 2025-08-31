import ffmpeg
import moviepy
import sys
import subprocess
from datetime import timedelta
from pydub import AudioSegment
import time


def get_time(input_path):
    return subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", input_path]
    ).decode().strip()

def convertation(input_path,output_path,number_of_chapters=1):
    duration = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", input_path]
    ).decode().strip()

    timecodes=[str(timedelta(seconds=int(float(duration)*(i/number_of_chapters) ))).zfill(8) for i in range(number_of_chapters+1)]
    segment_time=float(duration)/number_of_chapters
    print(timecodes)
    out=output_path.rsplit('.',1)

    cmd = [
            "ffmpeg",
            "-y",
            "-i", input_path,
            "-af", "loudnorm",
            "-ar","44100",
            "-c:a", "pcm_s16le",
            # "-t", duration,
            # "-movflags", "+faststart",
            "-map", "a",
            f'{output_path}'
        ]
    if 'wav' not in input_path:
        subprocess.run(cmd, check=True)

    for i in range(number_of_chapters):
        cmd = [
            "ffmpeg",
            "-y",
            '-ss', timecodes[i],
            "-i", output_path,
            '-t', str(segment_time),
            "-c","copy",
            "-movflags",
            "+faststart",
            "-map", "a",
            f'_{i+1}.'.join(out)
        ]

        subprocess.run(cmd, check=True)
