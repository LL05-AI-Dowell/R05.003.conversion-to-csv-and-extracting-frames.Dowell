import os
import cv2
import datetime

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("./captured_frame/image"+str(count)+".jpg", image)     
    return hasFrames


#creating a folder to save the captured images
rootdir = os.getcwd()
frame_folder = "captured_frame"

if not os.path.exists(frame_folder):
    os.makedirs(frame_folder)
    print('Created "/captured_frame/" directory')

print("Please keep the vedio file in current working directory")
print("from where you are running the script\n\n")

#reading video file
vidcap = cv2.VideoCapture("Video2.mp4")


s = float(input("Enter the time in sec,you want to extract a frame : "))

sec = 0
frameRate = s 
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

 
frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT) 
fps = int(vidcap.get(cv2.CAP_PROP_FPS)) 
  

seconds = int(frames / fps)

video_time = str(datetime.timedelta(seconds=seconds)) 
print("\nduration in seconds:", seconds) 
print("\nvideo time:", video_time)
total_frame_save = seconds/s

t = round(total_frame_save)
print("\nTotal frames saved :{0} \n".format(t))

print("The frames are saved in capture frame directory")
