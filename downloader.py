import subprocess
import ffmpeg
import yt_dlp

def all_formats(url):
    ytdl_options={
        'listformats': 'True',
    }
    with yt_dlp.YoutubeDL(ytdl_options) as f:
        f.download(base_url)

def get_audio(url):
    ytdl_option={
        'format': 'bestaudio/best',
        'outtmpl': "%(title)s.%(ext)s",
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'wav'}],
        # 'postprocessor_args':[
        #     '-af', 'loudnorm'
        # ]
    # }]
    }

    with yt_dlp.YoutubeDL(ytdl_option) as audio:
        audio.download([url])

def get_short(url,start,end):
    ytdl_options={
        'format': 'bestvideo/best',
        'outtmpl': "%(title)s.%(ext)s",
        'download-sections': f"*10-20"
    }
    with yt_dlp.YoutubeDL(ytdl_options) as video:
        video.download([url])

base_url='https://youtu.be/A767EPK-2pM'
# all_formats(base_url)
# get_short(base_url, "04:15", "05:15")
# print(help(yt_dlp.YoutubeDL))
# get_audio(base_url)

