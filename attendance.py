from tkinter import *
from tkinter import ttk
from PIL import  Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2, os, csv, tkinter
from tkinter import filedialog
from time import strftime
from datetime import datetime

mydata=[]
class Attendance:
    def __init__(self, root, fname):
        self.root = root
        # self.main_window = main_window 
        self.root.geometry("1350x690+0+0")
        self.root.configure(bg='lightblue')
        self.root.title("ATTENDANCE REPORT")

        # ========= Variables ===========
        self.var_atten_sid = StringVar()
        self.var_atten_rno = StringVar()
        self.var_atten_sname = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_dept = StringVar()
        self.var_atten_fname = StringVar()
        self.var_atten_papercode = StringVar()
        self.var_atten_attendance = StringVar()

       # Techno logo
        logo_img = Image.open("Images/tmsl.png")
        self.photoimg = ImageTk.PhotoImage(logo_img)
        f_label = Label(self.root, image=self.photoimg)
        f_label.place(x=0, y=0, width=98, height=94)

        title_label = Label(root, text="ATTENDANCE REPORT",
                            font=("times new roman", 32, "bold"),bg="lightyellow", fg="darkgreen")
        title_label.place(x=98, y=0,width=1250,height=94)

        # =========== Logout Button ===========
        logout_x = 1200
        logout_y = 40
        logout_width = 60
        logout_height = 30
        logout_btn = Button(root, text="Logout", cursor="hand2", command=self.iExit,
                      font=("times new roman", 12, "bold"),bg="red", fg="white",
                      activebackground="darkblue", activeforeground="white")
        logout_btn.place(x=logout_x, y=logout_y, width=logout_width, height=logout_height)

        # ========== Label to display the first name of user  ===========
        # Adjusting fname label position
        fname_label_width = 230  # Adjust the width of the label as needed
        fname_label_x = logout_x - (fname_label_width - logout_width) // 2  # Calculate x position
        fname_label_y = logout_y - 30 
        self.user_label = Label(root, text=f"Welcome, {fname}", font=("times new roman", 12), bg='lightyellow')
        self.user_label.place(x=fname_label_x, y=fname_label_y, width=fname_label_width)

        # ================ Main Frame ====================
        main_frame = Frame(root, bd=2)
        main_frame.place(x=10, y=95, width=1330, height=580)

        # ============================== Top Label Frame ===================================
        top_frame = LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE, text="Take Attendance", 
                                font=("times new roman", 20, "bold"))
        top_frame.place(x=10, y=10, width=1302, height=120)

        # Paper Code
        papercode_label = Label(top_frame, text="Paper Code", font=("times new roman", 12, "bold"),bg="white")
        papercode_label.grid(row=0, column=0, padx=5, pady=20, sticky=W)
        papercode_combo = ttk.Combobox(top_frame, textvariable = self.var_atten_papercode,
                                  font=("times new roman", 12, "bold"), width=15, state="readonly")
        papercode_combo["values"]=("-Paper Code-", "A", "B", "C", "D")
        papercode_combo.current(0)
        papercode_combo.grid(row=0, column=1, padx=20, pady=2, sticky=W)

        # Faculty Name 
        fname_label = Label(top_frame, text="Faculty Name:", font=("times new roman", 12, "bold"),bg="white")
        fname_label.grid(row=0, column=2, padx=5,  pady=20, sticky=W)
        fname_combo = ttk.Combobox(top_frame, textvariable = self.var_atten_fname,
                                  font=("times new roman", 12, "bold"), width=15, state="readonly")
        fname_combo["values"]=("-Faculty Name-", "A", "B", "C", "D")
        fname_combo.current(0)
        fname_combo.grid(row=0, column=3, padx=2, pady=20, sticky=W)

        # ============================== Top Label Frame ===================================
        top_left_frame = LabelFrame(top_frame, bg="white", bd=0, relief=RIDGE,
                                font=("times new roman", 20, "bold"))
        top_left_frame.place(x=570, y=0, width=720, height=70)

        # ================== Buttons =====================
        openCam_btn = Button(top_left_frame, text="Open Camera", width=12, command=self.face_recog, cursor="hand2",
                             font=("times new roman", 12, "bold"), bg="lightgreen", fg="black")
        openCam_btn.grid(row=0, column=4, padx=12, pady=20)

        fingerprint_btn = Button(top_left_frame, text="Fingerprint", width=12, cursor="hand2",
                             font=("times new roman", 12, "bold"), bg="lightblue", fg="black")
        fingerprint_btn.grid(row=0, column=5, padx=12, pady=20)

        import_btn = Button(top_left_frame, text="Import csv", width=12, command=self.importCsv, cursor="hand2",
                          font=("times new roman", 12, "bold"), bg="green", fg="white")
        import_btn.grid(row=0, column=6, padx=12, pady=20)

        export_btn = Button(top_left_frame, text="Export csv", width=12, command=self.exportCsv, cursor="hand2",
                          font=("times new roman", 12, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=7, padx=12, pady=20)

        reset_btn = Button(top_left_frame, text="Reset", width=12, command=self.reset_data, cursor="hand2",
                          font=("times new roman", 12, "bold"), bg="lightblue", fg="black")
        reset_btn.grid(row=0, column=8, padx=12, pady=20)

        # ============================ Bottom Label Frame =====================================
        bottom_frame = LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE, text="Attendance Report", 
                                font=("times new roman", 20, "bold"))
        bottom_frame.place(x=10, y=150, width=1302, height=410)

        # ============================ Table Frame ==============================
        table_frame = Frame(bottom_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=10, width=1275, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        #style = ttkthemes.ThemedStyle(root)
        #style.theme_use("clam")
        #style.configure("Treeview.Heading")

        self.AttendanceReport_table = ttk.Treeview(table_frame, column=("student_id", "rollno", "name",
                                                                         "department", "semester", "date", "time", "attendance"),
                                                                xscrollcommand=scroll_x.set,
                                                                yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReport_table.xview)
        scroll_y.config(command=self.AttendanceReport_table.yview)

        #self.AttendanceReport_table.heading("slno", text="Sl No.")
        self.AttendanceReport_table.heading("student_id", text="Student ID")
        self.AttendanceReport_table.heading("rollno", text="Roll No")
        self.AttendanceReport_table.heading("name", text="Name")
        self.AttendanceReport_table.heading("department", text="Department")
        self.AttendanceReport_table.heading("semester", text="Semester")
        #self.AttendanceReport_table.heading("faculty_name", text="Faculty Name")
        #self.AttendanceReport_table.heading("subject_name", text="Paper Code")
        self.AttendanceReport_table.heading("date", text="Date")
        self.AttendanceReport_table.heading("time", text="Time")
        self.AttendanceReport_table.heading("attendance", text="Attendance")
        self.AttendanceReport_table["show"] = "headings"

        #self.AttendanceReport_table.column("slno", width=30,anchor=CENTER)
        self.AttendanceReport_table.column("student_id", width=70,anchor=CENTER)
        self.AttendanceReport_table.column("rollno", width=100,anchor=CENTER)
        self.AttendanceReport_table.column("name", width=130,anchor=CENTER)
        self.AttendanceReport_table.column("department", width=80,anchor=CENTER)
        self.AttendanceReport_table.column("semester", width=80,anchor=CENTER)
        #self.AttendanceReport_table.column("faculty_name", width=130,anchor=CENTER)
        #self.AttendanceReport_table.column("subject_name", width=130,anchor=CENTER)
        self.AttendanceReport_table.column("date", width=85,anchor=CENTER)
        self.AttendanceReport_table.column("time", width=85,anchor=CENTER)
        self.AttendanceReport_table.column("attendance", width=85,anchor=CENTER)

        #self.AttendanceReport_table.tag_configure("odd", background="#eee")
        #self.AttendanceReport_table.tag_configure("even", background="#ddd")
        
        self.AttendanceReport_table.pack(fill=BOTH, expand=1)
        self.AttendanceReport_table.bind("<ButtonRelease>", self.get_cursor)

    # ===================================== Function Declaration ===================================
    # =================== Mark Attendance ==================
    def mark_attendance(self, i, r, n, d, s):
        with open("Attendance.csv","r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((",")) # Aritra, 1, IT
                name_list.append(entry[0])           
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) and (s not in name_list)):
                now =  datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                #self.AttendanceReport_table.insert("", "end", values=(len(self.AttendanceReport_table.get_children())+1,
                #                                                f.writelines(f"\n{i},{r},{n},{d},{s},{d1},{dtString},P")))
                f.writelines(f"\n{i},{r},{n},{d},{s},{d1},{dtString},P")

    # ================ Face Recognition Function ================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)
            coord = []           
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100 * (1 - predict / 300))
                
                if confidence > 77:
                    conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="facerecog")
                    my_cursor = conn.cursor()

                    my_cursor.execute("select student_id, rollno, name, department, semester from student where student_id=" + str(id))
                    result = my_cursor.fetchone()

                    if result is not None:
                        i, r, n, d, s = map(str, result)
                        cv2.putText(img, f"Student ID: {i}", (x, y-130), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Roll no: {r}", (x, y-100), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name: {n}", (x, y-70), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department: {d}", (x, y-40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Semester: {s}", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_attendance(i, r, n, d, s)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
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

    # ================ Fetch Data =====================
    def fetchData(self, rows):
        self.AttendanceReport_table.delete(*self.AttendanceReport_table.get_children())
        for i in rows:
            self.AttendanceReport_table.insert("",END,values=i)
        #for i, row in enumerate(rows, start=1):
        #    self.AttendanceReport_table.insert("", END, values=(i,) + row)
   
    # ================ Import csv =================
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir = os.getcwd(), title="Open CSV", filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # ================ export csv ===============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir = os.getcwd(), title="Open CSV", filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln, mode = "w", newline = "") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent = self.root)

    # ================= Get Cursor Function ========================
    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReport_table.focus()
        #content=self.AttendanceReport_table.item(cursor_row)
        #rows = content['values']
        #self.var_atten_fname.set(rows[0])
        #self.var_atten_papercode.set(rows[1])
    
    # ================ Reset Data Function ================
    def reset_data(self):
        self.var_atten_fname.set("-Faculty Name-")
        self.var_atten_papercode.set("-Paper Code-")

    # ============== Exit / Logout ==================
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("LOGOUT", "Are you sure to Logout?", parent=self.root)
        if self.iExit > 0:
            # self.main_window.destroy()
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root = Tk()
    # main_window = Toplevel(root)
    # obj = Attendance(root, main_window)
    obj = Attendance(root)
    root.mainloop()