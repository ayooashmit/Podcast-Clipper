from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url1 = "https://www.youtube.com/watch?v=j_TvWRS2_Hw"
url2 = "https://www.youtube.com/watch?v=skyTCk57IZ0"

try:
   
    yt = YouTube(url2, on_progress_callback=on_progress)
    print(yt.title)
    
   
    ys = yt.streams.get_highest_resolution()
    
    print("Downloading...")
    ys.download()
    print("Download complete!")

except Exception as e:
    print(f"An error occurred: {e}")

