import mediapipe as mp
import cv2
import math
import pyautogui
pyautogui.FAILSAFE=False
# -----
mp_drawing= mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
screen_w, screen_h = pyautogui.size()
cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(static_image_mode=False,min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()
        flipped=cv2.flip(frame,1)
        img = cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB)
        results= holistic.process(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        if results.left_hand_landmarks:
        
            index_finger = results.left_hand_landmarks.landmark[8]
            thumbs = results.left_hand_landmarks.landmark[4]
            element = results.left_hand_landmarks.landmark[5]
            h, w, _ = flipped.shape
            x2=element.x
            x1=element.x
            y2=thumbs.y
            y1=thumbs.y
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
           
            cx, cy = int(index_finger.x * w), int(index_finger.y * h)
            bx, by = int(thumbs.x * w), int(thumbs.y * h)
            ax,ay=int(element.x * w), int(element.y * h)
            cv2.circle(flipped, (cx, cy), 8, (0, 255, 0), cv2.FILLED)
            cv2.circle(flipped, (bx, by), 8, (0, 255, 0), cv2.FILLED)
            cv2.circle(flipped, (ax, ay), 8, (0, 255, 0), cv2.FILLED)
            
            
         
            pyautogui.moveTo(index_finger.x*screen_w,index_finger.y*screen_h)
        

            # if distance<210 and distance<220:
            #     pyautogui.click()
            
        cv2.imshow('Holistic', flipped)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()