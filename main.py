# import ffmpeg
# import moviepy
# import whisper
import os
# import pickle
# import pandas as pd
import subprocess
from datetime import timedelta
import datetime
from video_to_audio import convertation,get_time
from video_shorting import short_maker,casino,short_maker_blackpad
from downloader import get_short,get_audio,all_formats

def get_short_from_yotube(url:str,timecodes:list)-> None:
    """
    Скачивает шортсы c YouTube по заданным временным кодам.

    Args:
        url (str): URL видео на YouTube.
        timecodes (List[List[float, float]]): Список временных кодов, где каждый код
            — список из двух элементов [start, end] в секундах (int) или формате времени (str).
    """
    for timecode in timecodes:
        print(*timecode)
        new_name='-'.join([str(i) for i in timecode]).replace(':','_')
        get_short(url,*timecode,f"videos/{new_name}_short.mp4")

name='ИГРОПОЛИУС_Мафия.webm'

timecodes=[
#  [4309.15+80, 4524.139999999999-50],
 [8711.56-1, 8748.16+6.5],

 ]


print(timecodes)

# timecodes=[[str(timedelta(seconds=int(i))).zfill(8) for i in timecode] for timecode in timecodes]
# print(timecodes)

# получаю аудио с ютуба
get_audio('https://youtu.be/fIsuSYd-B8w')

# из видео/аудио получаю нормированный wav аудио файл
# convertation(name,name.replace('mp4','wav').replace('webm','wav'),number_of_chapters=8) #оптимизировать чтобы работало не 3 часа
# print(get_time(name))

# делаю шортсы
# for timecode in timecodes:
#     print(*timecode)
#     short_maker(*timecode,name,f"videos/{'_'.join([str(int(i)) for i in timecode]).replace(':','_')}_short.mp4")

####обрезаю вебку
# all_shorts=[_ for _ in os.listdir('videos') if "short" in _]
# for i in all_shorts:
#     new_name=i.replace('short','webcam')
    # casino(f'videos/{i}',f'videos/{new_name}',1080) 

#делаю горизонтальные шортсы 
# all_shorts=[_ for _ in os.listdir('videos') if "full" in _]
# for i in all_shorts:
#     new_name=i.replace('full','black')
#     short_maker_blackpad(f'videos/{i}',f'videos/{new_name}')


# url='https://youtu.be/yJgnSqmYdiw'
# get_short_from_yotube(url,timecodes)

# print(get_time('ИГРОПОЛИУС_мафия.webm'))

# # вырезаю шортсы с ютуба
# url='https://youtu.be/yBp16urXQoA'
# # url='https://youtu.be/HJni6k2-2pQ'
# # all_formats(url)
# for timecode in timecodes:
#     # print(*timecode)
#     new_name='-'.join([str(i) for i in timecode]).replace(':','_').replace('.','_')
#     get_short(url,*timecode,f"videos/{new_name}_short.mp4")

# get_short(url,* [581.59, 810.54],f"videos/{'asdasdasdasd'}_short.mp4")