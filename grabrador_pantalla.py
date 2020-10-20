import pyautogui
import numpy
import cv2
from PIL import Image

video = cv2.VideoWriter('pantalla.mp4',cv2.VideoWriter_fourcc(*'XVID'),20,(700,700))

while True:
    image = pyautogui.screenshot()
    image = image.resize((700,700),Image.ANTIALIAS)
    frame = numpy.array(image)
    video.write(frame)
    cv2.imshow('window',frame)
    if cv2.waitKey(1) == ord('x'):
        break

video.release()
cv2.destroyAllWindows()
