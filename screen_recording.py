import cv2 as cv
import pyautogui as p
import numpy as np
rs=p.size()
fn=('D:\\Data\\record.mp4')
fps=60.0
fourcc=cv.VideoWriter_fourcc(*'XVID')
output=cv.VideoWriter(fn,fourcc,fps,rs)
cv.namedWindow('Live-Recording',cv.WINDOW_NORMAL)
cv.resizeWindow('Live-Recording',(600,400))
while True:
    img=p.screenshot()
    f=np.array(img)
    f=cv.cvtColor(f,cv.COLOR_BGR2RGB)
    output.write(f)
    cv.imshow('Live-Recording',f)
    if cv.waitKey(1)==ord('q'):
        break
output.release()
cv.destroyAllWindows()
