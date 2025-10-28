import mediapipe as mp
import cv2
import math
import pyautogui
import autopy
pyautogui.FAILSAFE=False

mp_drawing= mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
screen_w, screen_h = pyautogui.size()
cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(min_detection_confidence=0.7, min_tracking_confidence=0.7) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()
        flipped=cv2.flip(frame,1)
        img = cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB)
        results= holistic.process(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        
        # mp_drawing.draw_landmarks(flipped, results.face_landmarks,mp_holistic.FACEMESH_TESSELATION)
        mp_drawing.draw_landmarks(flipped, results.left_hand_landmarks,mp_holistic.HAND_CONNECTIONS)
        if results.left_hand_landmarks:
            
            
            index_finger_tip = results.left_hand_landmarks.landmark[8]
         
            middle_finger_tip=results.left_hand_landmarks.landmark[12]
            thumb_tip=results.left_hand_landmarks.landmark[4]
            h,w,c=flipped.shape
            cx, cy = int(index_finger_tip.x*w ), int(index_finger_tip.y *h)
            ax, ay = int(middle_finger_tip.x*w ), int(middle_finger_tip.y *h)
            bx, by = int(thumb_tip.x*w ), int(thumb_tip.y *h)
            rect_size = 40
            rect_size1 = 55
            x1, y1 = cx - rect_size , cy - rect_size 
            x2, y2 = cx + rect_size , cy + rect_size
            p1, q1 = ax - rect_size1 , ay - rect_size1
            p2, q2 = ax + rect_size1 , ay + rect_size1
            l1, m1 = bx - rect_size1 , by - rect_size1
            l2, m2 = bx + rect_size1 , by + rect_size1

            cv2.rectangle(flipped, (x1, y1), (x2, y2), (0, 255, 0), 2) 
            rect1=cv2.rectangle(flipped, (p1, q1), (p2, q2), (255, 0, 0), 2) 
            rect2=cv2.rectangle(flipped, (l1, m1), (l2, m2), (0, 0, 255), 2) 
            
            
            # distance = math.sqrt((bx - ax)**2 + (by - ay)**2)
            # print(distance)
            # if distance<60:
            #     autopy.mouse.click()
            if results.left_hand_landmarks:
                if results.left_hand_landmarks.landmark[mp_holistic.HandLandmark.THUMB_TIP].x< results.left_hand_landmarks.landmark[mp_holistic.HandLandmark.THUMB_IP].x:
                    print("up")
                else:
                    print("down")
                    pyautogui.moveTo(index_finger_tip.x*screen_w,index_finger_tip.y*screen_h/5)

            
        cv2.imshow('Holistic', flipped)
        if cv2.waitKey(10) & 0xff == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()