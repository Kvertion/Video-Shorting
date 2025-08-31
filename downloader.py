import subprocess
import ffmpeg
import yt_dlp

def all_formats(url):
    ytdl_options={
        'listformats': 'True',
    }
    with yt_dlp.YoutubeDL(ytdl_options) as f:
        f.download(url)

def get_audio(url):
    if 'kick' not in url:
        ytdl_option={
            'format': 'bestaudio/best',
            'outtmpl': "%(title)s.%(ext)s",
            # 'postprocessors':[{
            #     'key':'FFmpegExtractAudio',
            #     'preferredcodec':'wav'}],
            # 'postprocessor_args':[
            #     '-af', 'loudnorm'
            # ]
        # }]
        }
    else:
        ytdl_option={
            'format': f'best[height<=200]',
            # 'format': '160p60',
            'outtmpl': f"kick_%(duration)s_%(title|slugify)s.%(ext)s", 
            # 'download_ranges': lambda info_dict, yt_instance: [
            # {'start_time': start, 'end_time': end},
            # ],
            'force_keyframes_at_cuts': False,
            'merge_output_format': 'm4a'
        }
    with yt_dlp.YoutubeDL(ytdl_option) as audio:
        audio.download([url])

def get_short(url,start,end,out,video_quality='bestvideo'):
    ytdl_options={
        'format': f'{video_quality}+bestaudio/best',
        # 'format': '299+140',
        'outtmpl': f"{out}",#.%(ext)s",
        'download_ranges': lambda info_dict, yt_instance: [
        {'start_time': start, 'end_time': end},
        ],
        'force_keyframes_at_cuts': False,
        'merge_output_format': 'mp4'
    }
    with yt_dlp.YoutubeDL(ytdl_options) as video:
        video.download([url])

def get_kick(url,start,end,out,video_quality='bestvideo'):
    ytdl_options={
        'format': f'{video_quality}+bestaudio/best',
        # 'format': '160p60',
        'outtmpl': f"{out}.%(ext)s",
        # 'download_ranges': lambda info_dict, yt_instance: [
        # {'start_time': start, 'end_time': end},
        # ],
        'force_keyframes_at_cuts': False,
        'merge_output_format': 'mp4'
    }
    with yt_dlp.YoutubeDL(ytdl_options) as video:
        video.download([url])

# get_kick('https://kick.com/maddyson/videos/48cbd65c-20d4-4881-abf5-59ca0ca09df5', 4000, 4100, 'kick_attempt12')

base_url='https://kick.com/maddyson/videos/48cbd65c-20d4-4881-abf5-59ca0ca09df5'
get_audio(base_url)
# all_formats(base_url)
# get_short(base_url, "04:15", "05:15")
# print(help(yt_dlp.YoutubeDL))
# get_audio(base_url)

