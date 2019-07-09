import numpy as np 
from PIL import ImageGrab 
import cv2 
import time
import win32api
import pywinauto
from directkeys import ReleaseKey, PressKey, W, A, S, D 

width = 800
height = 600

hs_cascade = cv2.CascadeClassifier('HS.xml')

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    heads_shoulders = hs_cascade.detectMultiScale(processed_img, 1.1, 3)

    for (x,y,w,h) in heads_shoulders:
        print('hs dected X:' + str(x) + ' Y:' + str(y))
        cv2.rectangle(processed_img,(x,y),(x+w,y+h),(0,255,0),2)
        win32api.SetCursorPos((x,y))
        pywinauto.mouse.click(button='left')
        time.sleep(.5)
    return processed_img

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)
    
last_time = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,0,800,600)))
    new_screen = process_img(screen)

    last_time = time.time()
    #uncomment if you want to see it work
    #cv2.imshow('window', new_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break