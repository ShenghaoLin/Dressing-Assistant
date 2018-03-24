from PIL import Image
import os
name = 0
for i in os.listdir("."):
	if ".jpg" in i:
		Image.open(i).convert("RGB").save("image"+str(name)+".jpg")
		name+=1
