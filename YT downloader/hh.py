import os, time

#title  = "\"Run Python script on clicking HTML button  Script Output on Html Page Part1\""
#os.system("ffmpeg -i "+ title +".mp4 -i "+ title +".webm -c copy "+ title +".mkv")
def combine_audio(title):
    char = "|/<>?,:'}{][+_-=)(*&%$#@!~`"
    for c in char:
        title = title.replace(c , "")
    try:
        os.system("ffmpeg -i vid.mp4 -i aud.webm -c copy \""+ title +"\".mkv")
    except:
        os.system("ffmpeg -i vid.webm -i aud.webm -c copy \""+ title +"\".webm")
    os.remove("aud.webm")
    try:
        os.remove("vid.mp4")
    except:
        os.remove("vid.webm")
    os.rename(title + ".mkv", "Download\\" + title + ".mkv")
#combine_audio("[4K series] Hong Kong 30 seconds")

