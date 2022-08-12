
import cv2
import os


count = 0
vidcap = cv2.VideoCapture(r"C:\WorkFiles\ivms_client_tester\cut2.mp4")
success,image = vidcap.read()
#success = True
while(True):
            if success:
                path_out = "C:\WorkFiles\ivms_client_tester\data2"
                vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
                success,image = vidcap.read()
                print ('Read a new frame: ', success)
                cv2.imwrite( path_out + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
                count = count + 30
            else:
                break