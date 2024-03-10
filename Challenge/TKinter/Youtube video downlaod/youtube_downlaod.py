from pytube import *
# link = "https://youtu.be/1Rm9s0u5L78"
link = "https://youtu.be/gRo5a5kEFr8"
yt = YouTube(link)
# print("Title:", yt.title)
# print("Id_video: ",yt.video_id)
# print("Age: ",yt.age_restricted)
# print("Channel:", yt.author)
# print("Published date:", yt.publish_date.strftime("%Y-%m-%d"))
# print("Number of views:", yt.views)
# print("Length of video:", yt.length, "seconds")
# print(yt.channel_url)


#! Get all resolution => .mp4
# x = yt.streams.filter(file_extension='mp4')
# all_resolution =[]
# for i in x :
#     all_resolution.append((str(i).split(' '))[3][4:].replace("\"",""))
# [print(i) for i in set(all_resolution)]

#! Customize resolution => .mp4
#yt.streams.filter(file_extension='mp4').filter(res="480p").first().download("C:/Users/aa/Desktop")

# #! Hight resolution
# # yt.streams.get_highest_resolution().download()


# x = yt.streams.filter(file_extension='mp4')
# all_itag =[ int((str(i).split(' '))[1][5:].replace("\"",""))   for i in x ]
# all_resolution =[ (str(i).split(' '))[3][4:].replace("\"","")   for i in x    if (str(i).split(' '))[3][4:].replace("\"","")[-1] == "p" ]

# all = {str((str(i).split(' '))[3][4:].replace("\"","")):int((str(i).split(' '))[1][5:].replace("\"",""))   for i in x       if (str(i).split(' '))[3][4:].replace("\"","")[-1] == "p"}

# # print(all_itag)
# # print(all_resolution)
# print(all)
# print(list(all.keys()))
# print(list(all.values()))

# res = int(all[list(all.keys())[2]])

# # yt.streams.get_by_resolution(res).download()
# yt.streams.filter(progressive=True).filter(file_extension="mp4").get_by_resolution(1080).download()


all = yt.streams.filter(file_extension="mp4",progressive=True)
[print(str(i).split(' ')[3][5:-1]) for i in all]
# all.get_by_resolution(resolution="360p").download()
# all_res = [(f"{lg+1}: " + str(i).split(' ')[3] + str(i).split(' ')[4])  for lg,i in enumerate(all) if str(i).split(' ')[3][-2] == "p"]
# print(all_res)
print("Video successfullly downloaded from", link)





#!
#  ----------------------------------------------------------------------------------------------------------




# #importing the module 
# from pytube import YouTube 
  
# # where to save 
# SAVE_PATH = "D:/Files/SCHOOL/Python/Challenge/TKinter/Youtube video downlaod" #to_do 
  
# # link of the video to be downloaded 
# link="https://youtu.be/z-A4Wn0mauE"
  
# try: 
#     # object creation using YouTube
#     # which was imported in the beginning 
#     yt = YouTube(link) 
# except: 
#     print("Connection Error") #to handle exception 
  
# # filters out all the files with "mp4" extension 
# mp4files = yt.streams.filter('mp4') 
  
# #to set the name of the file
# yt.set_filename('GeeksforGeeks Video')  
  
# # get the video with the extension and
# # resolution passed in the get() function 
# d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
# try: 
#     # downloading the video 
#     d_video.download(SAVE_PATH) 
# except: 
#     print("Some Error!") 
# print('Task Completed!') 


#! ----------------------------------------------------------------------------------------------------------

# importing the module
from pytube import *

# where to save
SAVE_PATH = "C:/Users/aa/Desktop" #to_do

# link of the video to be downloaded
link="https://youtu.be/1Rm9s0u5L78"

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
mp4files = yt.streams.filter('mp4')

#to set the name of the file
yt.set_filename('GeeksforGeeks Video')

# get the video with the extension and
# resolution passed in the get() function
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
	# downloading the video
	d_video.download(SAVE_PATH)
except:
	print("Some Error!")
print('Task Completed!')

