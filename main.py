#library
import cv2
from darkflow.net.build import TFNet
import time
#initiaize model
options_cellar = {
    "model" : "ckpt/tiny-yolo-voc-3c.cfg",
    "load" :  800,
    "threshold" : 0.01
}

options_person = {
    "model" : "cfg/yolo.cfg",
    "load" :  "bin/yolo.weights",
    "threshold" : 0.5
}


options_belt= {
    "model" : "ckpt/tiny-yolo-voc-1c.cfg",
    "load" : 500,
    "threshold" : 0.01
}

"""

"""
#load detect person model
#if no : come back
#load model
f = open("labels.txt","w")
f.write("abnormal\n")
f.write("normal\n")
f.write("half-normal")
f.close()
tfnet_cellar = TFNet(options_cellar) #cellar
tfnet_person = TFNet(options_person) #person 
f = open("labels.txt","w")
f.write("belt")
f.close()
tfnet_belt = TFNet(options_belt)

#draw the bounding box and return the image 

"""
def draw_cellar(img,result):
	m = 0
	for i in result:
	    if i["confidence"]>m:
	        m =  i["confidence"]
        
	for i in result:
	    if i["confidence"]==m:
	        t1 = i["topleft"]["x"],i["topleft"]["y"]
	        br = i["bottomright"]["x"],i["bottomright"]["y"] 
	        label = i["label"] 
	        if label =="abnormal":
				img = cv2.rectangle(img,t1,br,(255,0,0),7)
				img = cv2.putText(img,label,t1,cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
				return img
	img = cv2.rectangle(img,t1,br,(0,255,0),7)
	img = cv2.putText(img,label,t1,cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
	return img
"""
def draw_cellar(img,result):
	m = 0
	for i in result:
	    if i["confidence"]>m:
	        m =  i["confidence"]
        
	for i in result:
	    if i["confidence"]==m:
	        t1 = i["topleft"]["x"],i["topleft"]["y"]
	        br = i["bottomright"]["x"],i["bottomright"]["y"] 
	        label = i["label"] 
	        if label =="abnormal":
	        	question = cv2.imread("question.jpg")
	        	xQ,yQ,s=question.shape
	        	img[t1[0]:t1[0]+xQ,t1[1]:t1[1]+yQ] = question
	        	return img
				
	try:
		thumb = cv2.imread("thumb.jpg")
		xQ,yQ,s = thumb.shape
		img[t1[0]:t1[0]+xQ,t1[1]:t1[1]+yQ] = thumb
		return img
	except:
		return img

def detect_person(img,result):
	try:
		for i in result:
		    if i["label"]=="person":
		        t1 = i["topleft"]["x"],i["topleft"]["y"]
		        br = i["bottomright"]["x"],i["bottomright"]["y"]  
		        label = "person"
		img = cv2.rectangle(img,t1,br,(0,255,100),7)
		img = cv2.putText(img,label,t1,cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
		return img
	except:
		question = cv2.imread("question-mark-face.jpg")
		xQ,yQ,s = question.shape
		x,y,shape = img.shape
		x=x//3
		y=y//3
		img[x:x+xQ,y:y+yQ] = question
		return img
	
def draw_belt(img,result):
	color = (138,43,226)
	m = 0
	for i in result:
	    if i["confidence"]>m:
	        m =  i["confidence"]
	for i in result:
	    if i["confidence"]==m:
	        t1 = i["topleft"]["x"],i["topleft"]["y"]
	        br = i["bottomright"]["x"],i["bottomright"]["y"] 
	label = "belt"
	try:
		thumb = cv2.imread("thumb.jpg")
		xQ,yQ,s = thumb.shape
		img[t1[0]:t1[0]+xQ,t1[1]:t1[1]+yQ] = thumb
	except:
		return img
	return img

#use opencv to initize
cap = cv2.VideoCapture(0)
while True:
	ret,img = cap.read()
	#print(int(time.time()))
	#detect boudning box per 5 seconds 
	#if int(time.time()) %5==0:
	result_person = tfnet_person.return_predict(img)
	result = tfnet_cellar.return_predict(img)	
	result_belt =tfnet_belt.return_predict(img)
	#img = draw(img,result_belt,"belt")
	img = draw_belt(img,result_belt)
	img = detect_person(img,result_person)
	img = draw_cellar(img,result)

	cv2.imshow('img',img)

	if cv2.waitKey(30) & 0xff == ord("q"):
		break
cap.release()
cv2.destroyAllWindows()

#voice recognition
#which pattern should render
"""
pygame.mixer.music.load("cartoon001.wav")
pygame.mixer.music.play()
time.sleep(10)"""







