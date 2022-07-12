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



        #Human=Button(root, text="Human Detection", font=("|times new roman",15,"bold"),cursor="hand2",command=self.humandetect ,bg="green",fg="Black").place(x=250,y=220)
        

        Weapon=Button(root, text="Weapon Detection", font=("|times new roman",15,"bold"),command=self.value, bg="green",fg="Black").place(x=650,y=220)
             

        #Crowd=Button(root, text="Crowd Detection", font=("|times new roman",15,"bold"),cursor="hand2",command=self.crowdcount,bg="green",fg="Black").place(x=1000,y=220)

        #T = Text(root, height =15, width = 75).place(x=390,y=350)

        Exit=Button(root, text="Exit", font=("|times new roman",15,"bold"),cursor="hand2",command=self.Close ,bg="red",fg="Black").place(x=650,y=650)

    def value():
            pass
            net = cv2.dnn.readNet("yolov3_training_2000.weights", "yolov3_testing.cfg")
            classes = ["Weapon"]


            layer_names = net.getLayerNames()
            output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
            colors = np.random.uniform(0, 255, size=(len(classes), 3))

            def send_mail_function():
                recipientEmail = "itsankitpatil@gmail.com"
                recipientEmail = recipientEmail.lower()

                try:
                        server = smtplib.SMTP('smtp.gmail.com',587)
                        server.ehlo()
                        server.starttls()
                        server.login("ankitpatilprojects@gmail.com",'Code@Prog')
                        server.sendmail('system_email',recipientEmail, "Warning A Fire is Detected in JSPM")
                        print("sent to {}".format(recipientEmail))
                        server.close()
                except Exception as e:
                        print(e)


# Enter file name for example "ak47.mp4" or press "Enter" to start webcam

            val = input("Enter file name or press enter to start webcam : \n")
            if val == "":
                val = 0
            return val




# for video capture
            cap = cv2.VideoCapture(value(0))

# val = cv2.VideoCapture()
            while True:
                _, img = cap.read()
                height, width, channels = img.shape
    # width = 512
    # height = 512

    # Detecting objects
                blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

                net.setInput(blob)
                outs = net.forward(output_layers)

    # Showing information on the screen
                class_ids = []
                confidences = []
                boxes = []
                for out in outs:
                    for detection in out:
                        scores = detection[5:]
                        class_id = np.argmax(scores)
                        confidence = scores[class_id]
                        if confidence > 0.5:
                # Object detected
                            center_x = int(detection[0] * width)
                            center_y = int(detection[1] * height)
                            w = int(detection[2] * width)
                            h = int(detection[3] * height)

                # Rectangle coordinates
                            x = int(center_x - w / 2)
                            y = int(center_y - h / 2)

                            boxes.append([x, y, w, h])
                            confidences.append(float(confidence))
                            class_ids.append(class_id)

                indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
                print(indexes)
                if indexes == 0: print("weapon detected in frame")
                font = cv2.FONT_HERSHEY_PLAIN
                for i in range(len(boxes)):
                    if i in indexes:
                            x, y, w, h = boxes[i]
                            label = str(classes[class_ids[i]])
                            color = colors[class_ids[i]]
                            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                            cv2.putText(img, label, (x, y + 30), font, 3, color, 3)

    # frame = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
                cv2.imshow("Image", img)
                key = cv2.waitKey(1)
                if key == 27:
                    break
                send_mail_function()
                cap.release()
                cv2.destroyAllWindows() 
    def Close(self):
        root.destroy()
root=Tk()
obj=ads(root)
root.mainloop()

        

    








