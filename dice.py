from SimpleCV import*

cam=Camera(1)
dis=Display()
colors=[Color.BLACK,Color.RED,Color.WHITE,Color.BLUE]

def getDiceNumber(img,color):
	number=0
	dist=img.scale(3).colorDistance(color)
	segmented=dist.stretch(200,255)
	blobs=segmented.findBlobs()
	
	if(blobs is not None):
		blobs.draw(Color.BLUE,10)
		for z in blobs:
			if(z.isCircle(1)):
				z.draw(Color.YELLOW,10)
				number=number+1		
				
	segmented.drawText("Valore Dado : "+str(number),10,10,Color.WHITE,100)
	segmented.save(dis)
	return number

while not dis.isDone():
	num=getDiceNumber(cam.getImage(),colors[2])
	if(dis.mouseRight):
		break
