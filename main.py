import requests
from os.path import isfile, join
from bs4 import BeautifulSoup
import os 

dir_path = join(os.getcwd(), "videos")
if not os.path.exists(dir_path):
    os.mkdir(dir_path)
f = open('download_list.txt', 'r')
lines = f.readlines()
for url in lines:
    # Get title of the video and mkdir if not exist
    title = BeautifulSoup(requests.get(url).text, 'html.parser').title.string.replace(" - XVIDEOS.COM", "")
    video_path = join(dir_path, title)
    # Skip if video folder already exist
    if not os.path.exists(video_path):
        os.mkdir(video_path)
        # Change to directory and download file
        os.chdir(video_path)
        print("Downloading {}".format(title))
        ret = os.system("avideo_dl {}".format(url))
        if ret == 0:
            os.system('del *.tmp')
            file = join(video_path, [f for f in os.listdir(video_path) if isfile(join(video_path, f))][0])
            new_file = join(dir_path, title)
            os.system("move {} {}.mp4".format(file, new_file[:-1]))
        # os.system('move *.mp4 {}'.format(video_path))
