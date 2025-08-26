# import ffmpeg
# import moviepy
# import whisper
import os
# import pickle
# import pandas as pd
import subprocess
from datetime import timedelta
import datetime
from video_to_audio import convertation
from video_shorting import *

# vid_dir=os.listdir('videos')
# list_of_videos=[i for i in vid_dir if 'mp4' in i]
# list_of_audios=[f"{i.split('.')[0]}.m4a" for i in list_of_videos]

name='ИГРОПОЛИУС2025.webm'
# timecodes=[[1861.92, 2025.37],[878.38, 976.82],[5700.42, 5978.98],[1420.86, 1529.74],[1204.57, 1292.39],[1861.92, 2025.37],[692.74, 744.78],
#            [1695.66, 1725.47],[1857.92, 1941.85],[1204.57, 1333.29],[1080.1, 1200.68],[1420.86, 1559.72]]

timecodes=[882, 976.82+12.5]
timecodes=[timecodes]

timecodes=[[str(timedelta(seconds=int(i))).zfill(8) for i in timecode] for timecode in timecodes]
# print(timecodes)

#mp4 to wav
convertation(name,name.replace('webm','wav'),number_of_chapters=5)

#делаю шортсы
# for timecode in timecodes:
#     print(*timecode)
#     short_maker(*timecode,name,f"videos/{'_'.join(timecode).replace(':','_')}_short.mp4")

# обрезаю вебку
# all_shorts=[_ for _ in os.listdir('videos') if "short" in _]
# for i in all_shorts:
#     new_name=i.replace('short','black')
#     casino(f'videos/{i}',f'videos/{new_name}',1080) 

#делаю горизонтальные шортсы 
# all_shorts=[_ for _ in os.listdir('videos') if "short" in _]
# for i in all_shorts:
#     new_name=i.replace('short','black')
#     short_maker_blackpad(f'videos/{i}',f'videos/{new_name}')

# short_maker_blackpad(*timecodes,name,f'videos/{datetime.datetime.now().strftime("%d_%m___%H_%M_%S")}_short_.mp4')
# casino('smuta.mp4','smuta1.mp4') 