import mediapipe as mp
import time
import cv2 as cv 
cap=cv.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
cTime=0
pTime=0
while True:
    success,frame=cap.read()
    frame=cv.flip(frame,1)
    frameRGB=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    results=hands.process(frameRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
    cTime=time.time()
    fps=1/(cTime-pTime)    
    pTime=cTime
    cv.putText(frame, str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN, 3, (255,0,255), 2)
    cv.imshow('Webcam',frame)
    k=cv.waitKey(1)
    if k==ord('q'):
        break 
cap.release()
cv.destroyAllWindows()

