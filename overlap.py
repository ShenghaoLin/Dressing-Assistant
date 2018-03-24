import cv2
from PIL import Image 

im = Image.open("question.jpg")
x,y = im.size
im=im.resize((int(x/2),int(y/2)))
im.save("question.jpg")


img1 = cv2.imread("image0.jpg")
thumb= cv2.imread("question.jpg")

x,y,shape = img1.shape
x=x//3
y=y//3


xQ,yQ,s = thumb.shape
print(xQ,yQ,s)
img1[x:x+xQ,y:y+yQ] = thumb

cv2.imshow("image",img1)
cv2.waitKey(0)