import cv2
def draw_collar(img,result):
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
	        	try:
	        		question = cv2.imread("question.jpg")
	        		xQ,yQ,s=question.shape
	        		img[br[0]:br[0]+xQ,br[1]:br[1]+yQ] = question
	        		img = cv2.rectangle(img,t1,br,(100,0,0),7)
	        		img = cv2.putText(img,label,t1,cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
	        		return img,False
	        	except:
	        		return img,True
	try:
		thumb = cv2.imread("thumb.jpg")
		xQ,yQ,s = thumb.shape
		label="good collar"
		img[br[0]:br[0]+xQ,br[1]:br[1]+yQ] = thumb
		img = cv2.rectangle(img,t1,br,(100,100,0),7)
		img = cv2.putText(img,label,t1,cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
		return img,True
	except:
		return img,True

def detect_person(img,result):
	try:
		a = 0
		for i in result:
			if i["label"]=="person":
				a += 1
				t1 = i["topleft"]["x"],i["topleft"]["y"]
				br = i["bottomright"]["x"],i["bottomright"]["y"]
				label = "person"
				img = cv2.rectangle(img,t1,br,(0,255,100),7)
				img = cv2.putText(img,label,t1,cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
		
		if a == 0:
			question = cv2.imread("question-mark-face.jpg")
			xQ,yQ,s = question.shape
			x,y,shape = img.shape
			x=x//3
			y=y//3
			img[x:x+xQ,y:y+yQ] = question
			return img,False

		else:
			return img,True
	except:
		return img, True
		
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
		label = "belt"
		img[br[0]:br[0]+xQ,br[1]:br[1]+yQ] = thumb
		img = cv2.rectangle(img,t1,br,(200,0,0),7)
		img = cv2.putText(img,label,t1,cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
		return img,True
	except:
		return img,False
	return img,False


