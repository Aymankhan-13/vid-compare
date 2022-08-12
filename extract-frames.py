
import cv2
import os
  
# Read the video from specified path
cam = cv2.VideoCapture(r"C:\Users\vadmin\Desktop\new\cut1")
  
try:
      
    # creating a folder named data
    if not os.path.exists('data2'):
        os.makedirs('data2')
  
# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')
  
# frame
currentframe = 0
  
while(True):
      
    # reading from frame
    ret,frame = cam.read()
  
    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)
  
        # writing the extracted images
        cv2.imwrite(name, frame)
  
        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break
  
# Release all space and windows once done
# cam.release()
# cv2.destroyAllWindows()

#################
# vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000)
