from pytube import YouTube
from pytube import Playlist
import os
import youtube_dl
import sys

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


#function to download only one video
def video_download(link):
    video =YouTube(link)
    print("Downloading....")
    print(video.title)
    stream=video.streams.get_by_itag(18)
    stream.download()

#function to download one mp3 file
def mp3_download(link):
     video=YouTube(link)
     print("Downloading....")
     print(video.title)
     video=video.streams.filter(only_audio=True).first()
     file = video.download()
     base,ext =os.path.splitext(file)
     new_file= base+ '.mp3'
     os.rename(file,new_file)

#function for Menu display and choice
def Menu():
    print("FOR MP4 DOWNLOAD PRESS -->1")
    print("FOR MP3 DOWNLOAD PRESS -->2")
    print("FOR PLAYLIST PRESS     -->3")
    choice =int(input("Choice: "))
    if choice == 1  :
        return 1
    elif choice ==2:
        return 2
    elif choice ==3:
        return 3
    else:
        return 0
#function for a playlist download
def play_list_download(link):
    playlist=Playlist(link)
    for video in playlist.videos:
        video.streams.first().download()

if __name__ == "__main__":
    if len(sys.argv) !=2 :
        print("Please Give me the URL....")
        sys.exit(-1)
    else:
        choice =Menu()
        link = sys.argv[1]
        if choice == 1:
            video_download(link)
        elif choice==2:
            mp3_download(link)
        elif choice==0:
            play_list_download(link)
        else:
            print("Invalid Value..")
            print("Try Again..")
            
    print("Download Complete!")
