from PIL import ImageGrab #importing pillow in sort PIL
import cv2 #importing opencv
import numpy as np
 while True:
    img=ImageGrab.grab(bbox=(0,0,1920,1080))
    img_np=np.array(img)
   cv2.imshow("screen recorder",img_np)
    video_cap.write(img_np)
    if cv2.waitKey(1)==ord("q"):
        break
