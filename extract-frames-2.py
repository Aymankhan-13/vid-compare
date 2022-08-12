
import cv2
import os


count = 0
vidcap = cv2.VideoCapture(r"C:\WorkFiles\ivms_client_tester\cut1.mp4")
success,image = vidcap.read()
success = True
while success:
    path_out = "C:\WorkFiles\ivms_client_tester\data"
    vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))              # saves a frame every second
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    cv2.imwrite( path_out + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
    count = count + 30                                          # saves frame every 30 seconds