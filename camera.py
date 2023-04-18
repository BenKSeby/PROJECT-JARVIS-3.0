import cv2
import pyttsx3 as p
engine = p.init()

def camera():
    cam = cv2.VideoCapture(0) 
    cv2.namedWindow("test")    
    img_counter = 0
    
    while True:
        ret, frame = cam.read()
        if not ret:
            engine.say("failed to grab frame")
            engine.runAndWait()
            break
        cv2.imshow("Photo Taking. IN PROGRESS...", frame)
    
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            engine.say("Escape hit, closing camera...")
            engine.runAndWait()
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "Taken_photo_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            engine.say("photo is taken. View it in this folder".format(img_name))
            engine.runAndWait
            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()
    #from repetition import first
    #first()

#camera()