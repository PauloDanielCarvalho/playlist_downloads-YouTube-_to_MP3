import pytube
from moviepy.editor import VideoFileClip
import os
import glob

def remove_non_ascii(string: str)->str:
    return string.encode('ascii','ignore').decode('utf8')


class download_to_mp3:
    def __init__(self):
        pass

    def download(self):
        p=pytube.Playlist('https://www.youtube.com/playlist?list=PL0Ov__yuxfmg-NWyD2148ebjfHHzFikpl')
        for video in p.videos:
            print(video)
            video.streams.get_highest_resolution().download(r'D:\Documentos\python_projeto\mp4-mp3\mp4')
            
            


    def rename(self, path):
        for i in os.listdir(path):
            old_file = os.path.join("D:\Documentos\python_projeto\mp4-mp3\mp4", i)
            new_file = os.path.join("D:\Documentos\python_projeto\mp4-mp3\mp4", remove_non_ascii(i))

            os.rename(old_file, new_file)

    def convert(self):
        for i in os.listdir(r'D:\Documentos\python_projeto\mp4-mp3\mp4'):
            print(i)
            mp4_file = f'D:\Documentos\python_projeto\mp4-mp3\mp4\{i}'

            mp3_file = f'D:\Documentos\python_projeto\mp4-mp3\mp3\{i}.mp3'
            clip = VideoFileClip(mp4_file)

            audio = clip.audio

            audio.write_audiofile(mp3_file)
            os.remove(f'D:\Documentos\python_projeto\mp4-mp3\mp4\{i}')
    def remove(self):
            for i in os.listdir(r'D:\Documentos\python_projeto\mp4-mp3\mp4'):
                print(i)
                os.remove(f'D:\Documentos\python_projeto\mp4-mp3\mp4\{i}')


