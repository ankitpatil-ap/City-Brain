import cv2
import numpy as np
import imutils 
import smtplib
import dlib
from tkinter import Tk, messagebox
from PIL import Image, ImageTk
import pymysql
from tkinter import *


# Human Detection
class ads:
    def __init__(self,root):
        self.root=root
        self.root.title("Advance Servilance System")
        self.root.geometry("1280x780+20+20")
        self.bg=ImageTk.PhotoImage(file="mbg.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        title=Label(root,text="Advance Servilance System", font=("times new roman",30,"bold"),bg="white",fg="Blue").place(x=450,y=30)



        Human=Button(root, text="Human Detection", font=("|times new roman",15,"bold"),cursor="hand2",command=self.humandetect ,bg="green",fg="Black").place(x=250,y=220)
        

        Weapon=Button(root, text="Weapon Detection", font=("|times new roman",15,"bold"),command=self.weapon_detection, bg="green",fg="Black").place(x=650,y=220)
             

        Crowd=Button(root, text="Crowd Detection", font=("|times new roman",15,"bold"),cursor="hand2",command=self.crowdcount,bg="green",fg="Black").place(x=1000,y=220)

        #T = Text(root, height =15, width = 75).place(x=390,y=350)

        Exit=Button(root, text="Exit", font=("|times new roman",15,"bold"),cursor="hand2",command=self.Close ,bg="red",fg="Black").place(x=650,y=650)

        

    def humandetect(self):

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
            #a = Label(root,text= "Analysising input image...") 
            #a.place(anchor == NW)


            #T = Text(root, height =15, width = 75).place(x=390,y=350)
            #T.config(font = ("Arial",14))
            #a = """Analysising input image..."""
            #T.insert(root.Text,a)

 
# Showing the output Image 
            cv2.imshow("Image", image) 
            cv2.waitKey(0) 
            people = "People Detected in frame Analysis Completed, Ready to go for next step.\n"
            cv2.destroyAllWindows()



    def crowdcount(self):
        #croud Count

# Connects to your computer's default camera
        cap = cv2.VideoCapture(0)
  
        print("Turning ON System Camera...\n")
        print("Counting Number of Faces in frame.\n")
# Detect the coordinates
        detector = dlib.get_frontal_face_detector()
  
  
# Capture frames continuously
        while True:
  
    # Capture frame-by-frame
         ret, frame = cap.read()
         frame = cv2.flip(frame, 1)
  
    # RGB to grayscale
         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         faces = detector(gray)

    # Iterator to count faces
         i = 0
         for face in faces:
  
# Get the coordinates of faces
            x, y = face.left(), face.top()
            x1, y1 = face.right(), face.bottom()
            cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
  
        # Increment iterator for each face in faces
            i = i+1
  
        # Display the box and faces
            cv2.putText(frame, 'face num'+str(i), (x-10, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            print(face, i)
  
    # Display the resulting frame
            cv2.imshow('frame', frame)
            print("\nNumber of face detected in frame are ",+i)
    
  
    # This command let's us quit with the "q" button on a keyboard.
            if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                
        



    
        #Weapon Detection
    def send_mail_function(self):
            recipientEmail = "amolgholve98@gmail.com"
            recipientEmail = recipientEmail.lower()

            try:
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.ehlo()
                server.starttls()
                server.login("shivamkumarrea@gmail.com",'covid@2019')
                server.sendmail('system_email',recipientEmail, "Weapon is Detected\n")
                print("sent to {}".format(recipientEmail))
                server.close()
            except Exception as e:
                print(e)

    def weapon_detection(self):

        gun_cascade = cv2.CascadeClassifier('cascade.xml')
        camera = cv2.VideoCapture(0)
   
        firstFrame = None
        gun_exist = False
   
        while True:
      
            ret, frame = camera.read()
   
            frame = imutils.resize(frame, width = 500)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       
            gun = gun_cascade.detectMultiScale(gray,
                                       1.3, 5,
                                       minSize = (100, 100))
       
        if len(gun) > 0:
                gun_exist = True
           
        for (x, y, w, h) in gun:
          
            frame = cv2.rectangle(frame,
                              (x, y),
                              (x + w, y + h),
                              (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]    
   
            if firstFrame is None:
                firstFrame = gray
                continue
                
   
    # print(datetime.date(2019))
    # draw the text and timestamp on the frame
        cv2.putText(frame, datetime.datetime.now().strftime("% A % d % B % Y % I:% M:% S % p"),
                    (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.35, (0, 0, 255), 1)
   
        cv2.imshow("Security Feed", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
#            break
            if gun_exist:
                print("guns detected")
            else:
                print("guns NOT detected")
  
            camera.release()
            cv2.destroyAllWindows()
        
  
# Release the capture and destroy the windows
             

    def Close(self):
        root.destroy()

root=Tk()
obj=ads(root)
root.mainloop()












