import os, numpy
import scrapetube
from PIL import Image
import requests
import time

timeToWork = time.time()

#Downloaded images=============================================

channelID = 'UCN6pxGXExD8z6XiIuqZ80gA'  #find: channelID
n=50     #Number of videos 

try:
    os.stat(f"images/{channelID}")
except:
    os.makedirs(f"images/{channelID}")

try:
    os.stat(f"images/{channelID}/im")
except:
    os.makedirs(f"images/{channelID}/im")

videos = scrapetube.get_channel(channelID) #get id of videos

file_path = f'images\\{channelID}\\im\\'

id_video = []
for video, i in zip(videos, range(n)):
    if i>n: continue
    id_video = id_video + [video['videoId']]
    url = f'https://i.ytimg.com/vi/{id_video[i]}/hq720.jpg'
    im = Image.open(requests.get(url, stream=True).raw)
    if im.size[0] == 1280:
        print("Downloaded image:", file_path+f"im{i}.png")
        im.save(file_path+f"im{i}.png")
#=============================================================





#Combine images================================================
print("#--------------------------------#")
print("Load image:", end=" ")

allfiles=os.listdir(os.getcwd()+'\\'+file_path)
imlist=[file_path + filename for filename in allfiles if  filename[-4:] in [".png",".PNG",".JPG",".jpg"]]

w,h=Image.open(imlist[0]).size
N=len(imlist)

arr=numpy.zeros((h,w,3),numpy.float64)

for im in imlist:
    imarr=numpy.array(Image.open(im),dtype=numpy.float64)
    arr=arr+imarr/N

arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)

out=Image.fromarray(arr,mode="RGB")
out.save(f"images\\{channelID}\\Average.png")
print(f"images\\{channelID}\\Average.png")
#=============================================================

print(f'Time to work Average: {time.time() - timeToWork }')




#UC-b89a0Fw6pNoP-g-_qLeiw   cienduk
#UCTzm7UqF0kVkxhPVj-Rui2g   spectator
#UCWnqnojAgMdN0fQpr_xByJw   MORGENSHTERN
#UC9-y-6csu5WGm29I7JiwpnA   computerphilw
#UCN6pxGXExD8z6XiIuqZ80gA   codebullet
#UCtI0Hodo5o5dUb67FeUjDeA   space x
#UC7f5bVxWsm3jlZIPDzOMcAg   haudiho
#UC6bTF68IAV1okfRfwXIP1Cg   itpedia


'''
url = f'https://i.ytimg.com/vi/{id_video[1]}/hq720.jpg'
im = Image.open(requests.get(url, stream=True).raw)
im.save(f"im{1}.png")
#im.show()
'''
