
from pytube import YouTube
import os

def download_video(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()

    destination = "/Users/DOKUR/PycharmProjects/yt_mp3/songs"

    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    return yt.title + " has been successfully downloaded."
