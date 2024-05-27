import cv2 as cv
vid=cv.VideoCapture(0)
print('Press c for taking screenshot')
print('Press q to exit')
while True:
    r,frame=vid.read()
    frame=cv.resize(frame,(700,500))
    frame_flip=cv.flip(frame,1)
    cv.imshow('Video',frame_flip)
    k=cv.waitKey(25)
    if k==ord('c'):
       cv.imwrite('D:\\Data\\Image.jpg',frame_flip)
    if k==ord('q'):
      break
vid.release()
cv.destroyAllWindows()
