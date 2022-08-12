import cv2

cap = cv2.VideoCapture(r"C:\Users\vadmin\Desktop\new\cut1.mp4")
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
print("Length: {}".format(length))
print("FPS: {}".format(fps))