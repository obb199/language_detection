import pytube as pt
from moviepy.editor import *
import os


def download_videos(links):
    """
    :param links: list with all links to download
    :return: None
    """
    for link in links:
        yt = pt.YouTube(link)
        t = yt.streams.filter()
        t[0].download()


def video_to_mp3(directory_of_videos):
    """
    :param directory_of_videos: name of directory with video files.
    :return: None
    """
    video_dirs = os.listdir(directory_of_videos)
    for v in video_dirs:
        video = VideoFileClip(f"{directory_of_videos}/" + v)
        video.audio.write_audiofile(f"{directory_of_videos}/sound_of_{v}.mp3")


if __name__ == '__main__':
    #download_videos(['https://www.youtube.com/watch?v=fb_v5Bc8PSk'])

    video_to_mp3("English Videos")
    #video_to_mp3('Portuguese Videos')

