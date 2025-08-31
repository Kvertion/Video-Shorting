import subprocess
import os
from datetime import timedelta

def cleaning(func):
    def wrapper(*args,**kwargs):
        # if str(args[0:2]).count('[[')==0: 
        timer=[]
        timer.append([args[0:2]])
        timer.extend(args[2:])
            # args=timer
        a=timer[0]
        if str(a[0]).count(':')==0:
            timer[0:2]=[[str(timedelta(seconds=int(i))).zfill(8) for i in timecode] for timecode in a]
            print(timer[0:2])
        args=timer
        result=func(*args,**kwargs)
        return result
    return wrapper

def casino(input_name,output_name,resolution=720):  
    '''
    обрезает вокруг вебки
    '''
    x=200 #отступ справа
    y=160 #отступ сверху
    x1080={720:1,1080:1920/1280}[resolution]
    y1080={720:1,1080:1080/720}[resolution]
    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_name, #mp4
        "-vf", f"crop={415*x1080:.0f}:{(720-y)*y1080:.0f}:{0}:{y*y1080:.0f}",
        # "-c", "copy",
        output_name #mp4
    ]
    subprocess.run(cmd, check=True)

# @cleaning
def short_maker(start,end,input_name,output_name):
    '''
    обрезает видео
    '''
    cmd = [
        "ffmpeg",
        "-y",
        "-ss", str(timedelta(seconds=int(start))).zfill(8),      # начало
        "-i", input_name, #mp4
        "-t", str(float(end) - float(start)),
        "-c:v", "copy",
        "-c:a", "copy",
        '-copyinkf',
        output_name
    ]
    subprocess.run(cmd, check=True)

def short_maker_blackpad(input_name, output_name, target_width=1080, target_height=1920):#превращает горизонтальное в вертикальное добавляя полосы сверху и снизу
    if not os.path.exists(input_name):
        raise FileNotFoundError(f"Файл не найден: {input_name}")

    # Фильтр: масштабируем до максимальной стороны, сохраняем пропорции
    # и добавляем чёрные поля сверху/снизу или по бокам
    vf = (
        f"scale='min(iw,{target_width})':'min(ih,{target_height})':force_original_aspect_ratio=decrease,"
        f"pad={target_width}:{target_height}:(ow-iw)/2:(oh-ih)/2:black"
    )

    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_name,
        "-vf", vf,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "23",
        "-pix_fmt", "yuv420p",      # исправляет затемнение
        "-c:a", "copy",
        "-movflags", "+faststart",  # сразу старт воспроизведения
        output_name
    ]

    subprocess.run(cmd, check=True)
    # subprocess.run(cmd, check=True)





def append_video(video1, video2, output_name):
    """
    Вставляет video2 в конец video1, создавая один файл.
    Видео должны быть одного формата, разрешения и кодека.
    """
    cmd = [
        "ffmpeg",
        "-y",
        "-i", video1,
        "-i", video2,
        "-filter_complex", "[0:v:0][0:a:0][1:v:0][1:a:0]concat=n=2:v=1:a=1[outv][outa]",
        "-map", "[outv]",
        "-map", "[outa]",
        output_name
    ]
    subprocess.run(cmd, check=True)
    print(f"Видео склеено: {output_name}")