import cv2
import numpy as np

cap=cv2.VideoCapture(1)

while True:
    ret, frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))

    img=cv2.rectangle(frame,(100,100),(200,200),(128,128,128),5)
    font=cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.putText(img,'Sorning Soft',(10,height - 15),font,1.5,(128,128,128),3,cv2.LINE_AA)

    cv2.imshow('frame',img)

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()