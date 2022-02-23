import cv2

img=cv2.imread('./app1/fluoritefish.jpg',0)
img=cv2.resize(img,(0,0),fx=0.8,fy=0.8)
img=cv2.rotate(img,cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('./app1/new.jpg',img)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()