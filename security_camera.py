import cv2
import winsound
import pyttsx3 as p
import time
import os


def security():
    engine = p.init()
    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        ret, frame = cam.read()
        ret, frame2 = cam.read()
        diff = cv2.absdiff(frame, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if cv2.contourArea(c) < 4000:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y),(x+w, y+h), (0, 255, 0), 4)
            winsound.Beep(500, 200)
            cv2.destroyAllWindows()
            time.sleep(2)
            engine.setProperty("rate", 140)
            engine.say("motion detected, turning on security login")
            engine.runAndWait()
            cam.release()
            time.sleep(1)
            os.system('python security_check.py')
        if cv2.waitKey(10) == ord('j'):
            break
        cv2.imshow('SECURITY CAM', frame)

#security()