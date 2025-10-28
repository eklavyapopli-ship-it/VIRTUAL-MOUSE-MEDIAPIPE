import mediapipe as mp
import cv2
import math
import pyautogui
import autopy
pyautogui.FAILSAFE=False
# -----
mp_drawing= mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
screen_w, screen_h = pyautogui.size()
cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(min_detection_confidence=0.1, min_tracking_confidence=0.1) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()
        flipped=cv2.flip(frame,1)
        img = cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB)
        results= holistic.process(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        
        mp_drawing.draw_landmarks(flipped, results.left_hand_landmarks,mp_holistic.HAND_CONNECTIONS)
        if results.left_hand_landmarks:
            
            
            index_finger_tip = results.left_hand_landmarks.landmark[8]
         
            middle_finger_tip=results.left_hand_landmarks.landmark[12]

         
            pyautogui.moveTo(index_finger_tip.x*screen_w,index_finger_tip.y*screen_h)
        

            
        cv2.imshow('Holistic', flipped)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()