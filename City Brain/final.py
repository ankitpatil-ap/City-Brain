import cv2
import numpy as np
import playsound
import smtplib
import imutils 


print("Analysising...")

hog = cv2.HOGDescriptor() 
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) 
   
# Reading the Image 
image = cv2.imread('img.jpg') 
   
# Resizing the Image 
image = imutils.resize(image, 
                       width=min(800, image.shape[1])) 
   
# Detecting all the regions in the  
# Image that has a pedestrians inside it 
(regions, _) = hog.detectMultiScale(image,  
                                    winStride=(4, 4), 
                                    padding=(4, 4), 
                                    scale=1.05) 
   
# Drawing the regions in the Image 
for (x, y, w, h) in regions: 
    cv2.rectangle(image, (x, y),  
                  (x + w, y + h),  
                  (0, 0, 255), 2) 
  
# Showing the output Image 
cv2.imshow("Image", image) 
cv2.waitKey(0) 
   
cv2.destroyAllWindows() 



def fire():
	Fire_Reported = 0
Alarm_Status = False

def play_audio():
	playsound.playsound("alsound.mp3",True)
video = cv2.VideoCapture("fr.mp4")

while True:
	ret, frame = video.read()
	#frame = cv2.resize(frame, (1000*600))
	#blur = cv2.GaussianBlur(frame, (15,15),0)
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	lower = [18,50,50]
	upper = [35,255,255]

	lower = np.array(lower,dtype='uint8')
	upper = np.array(upper,dtype='uint8')

	mask = cv2.inRange(hsv,lower,upper)

	output = cv2.bitwise_and(frame,hsv,mask=mask)

	size =cv2.countNonZero(mask)
	Fire_Reported = 0
	if int(size) > 15:
		Fire_Reported = Fire_Reported + 1

		if Fire_Reported >= 1:
			if Alarm_Status == False:
				#send_mail_function()
				play_audio()
				Alarm_Status = True

	if ret ==False:
		break

	cv2.imshow("Output",output)

	if cv2.waitKey(40000) & 0xFF == ord("q"):
		break

	cv2.destroyAllWindows()
	video.release()




fire()
	