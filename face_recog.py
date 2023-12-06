from tkinter import *
from tkinter import ttk
from PIL import  Image, ImageTk
from tkinter import messagebox
import mysql.connector, cv2, os
import numpy as np
from time import strftime
from datetime import datetime



class Face_Recog:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x690+0+0")
        self.root.configure(bg='lightblue')
        self.root.title("FACE RECOGNITION SYSTEM")


        # Techno logo
        logo_img = Image.open("Images/tmsl.png")
        self.photoimg = ImageTk.PhotoImage(logo_img)
        f_label = Label(self.root, image=self.photoimg)
        f_label.place(x=0, y=0, width=98, height=94)


        # Title Label
        title_label = Label(root, text="FACE RECOGNITION SYSTEM",
                            font=("times new roman", 32, "bold"),bg="lightyellow", fg="darkgreen")
        title_label.place(x=98, y=0,width=1250,height=94)


        # Face Recognition Button
        face_recogbtn_img = Image.open("Images/face_recog_btn.jpeg")
        self.face_recogbtnimg = ImageTk.PhotoImage(face_recogbtn_img)
        b1 = Button(self.root, image=self.face_recogbtnimg, command=self.face_recog, cursor="hand2")
        b1.place(x=500, y=190, width=250, height=250)

        btn = Button(self.root, text="Face Recognition", command=self.face_recog, cursor="hand2", 
                     font=("times new roman", 25, "bold"), bg="blue", fg="white",
                     activebackground="blue", activeforeground="white")
        btn.place(x=500, y=420, width=250, height=60)



    # ================ Attendance ===============
    def mark_attendance(self, i, r, n, d):
        with open("Attendance.csv","r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((",")) # Aritra, 1, IT
                name_list.append(entry[0])
            
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now =  datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{d1},{dtString},Present")



    # ============= Face Recognition Function ============
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            coord = []
            
            for (x,y,w,h) in features:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int(100*(1-predict/300))

                conn = mysql.connector.connect(host="localhost",username="root",password="1234",database="facerecog")
                my_cursor = conn.cursor()

                my_cursor.execute("select student_id from student where student_id="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                my_cursor.execute("select rollno from student where student_id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)
                
                my_cursor.execute("select name from student where student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select department from student where student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)


                if confidence > 77:
                    cv2.putText(img, f"Student ID: {i}", (x,y-95),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Roll no: {r}", (x,y-65),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Name: {n}", (x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Department: {d}", (x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)

                else:
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 3)
                    cv2.putText(img, "Unknown Face", (x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)


                coord=[x,y,w,h]

            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255,255,255), "Face", clf)
            return img
        

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0) # 0 for Laptop Camera & 1 for others


        while True:
            ret, img=video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recog(root)
    root.resizable(False,False)
    root.mainloop()