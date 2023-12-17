from tkinter import *
from tkinter import ttk
from PIL import  Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2, os, tkinter, re
import numpy as np
from tkcalendar import DateEntry

class Student:
    def __init__(self, root, fname):
        self.root = root
        # self.main_window = main_window 
        self.root.geometry("1350x690+0+0")
        self.root.configure(bg='lightblue')
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        # Variables
        self.var_sid = StringVar()
        self.var_rollno = StringVar()
        self.var_name = StringVar()
        self.var_dept = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_phno = StringVar()
        self.var_mail = StringVar()
        self.var_gend = StringVar()
        self.var_addr = StringVar()
        self.var_dob = StringVar()
        self.var_photo = StringVar()
        #self.var_fp = StringVar()

        # =========== Techno logo ===============
        logo_img = Image.open("Images/tmsl.png")
        self.photoimg = ImageTk.PhotoImage(logo_img)
        f_label = Label(self.root, image=self.photoimg)
        f_label.place(x=0, y=0, width=98, height=94)

        title_label = Label(root, text="STUDENT MANAGEMENT SYSTEM",
                            font=("times new roman", 32, "bold"),bg="lightyellow", fg="darkgreen")
        title_label.place(x=98, y=0,width=1250,height=94)

        # =========== Logout Button ===========
        logout_x = 1200
        logout_y = 40
        logout_width = 60
        logout_height = 30
        logout_btn = Button(root, text="Back", cursor="hand2", command=self.iExit,
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

        # ============ Left Label Frame =============
        left_frame = LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE, text="Student Details", 
                                font=("times new roman", 20, "bold"))
        left_frame.place(x=10, y=10, width=600, height=555)

        # =================== Current Course Frame =======================
        course_frame = LabelFrame(left_frame, bg="white", bd=2, relief=RIDGE, text="Current Course Information", 
                                font=("times new roman", 15, "bold"))
        course_frame.place(x=10, y=3, width=570, height=120)

        # Department 
        dept_label = Label(course_frame, text="Department", font=("times new roman", 12, "bold"),bg="white")
        dept_label.grid(row=0, column=0, padx=5, sticky=W)
        dept_combo = ttk.Combobox(course_frame, textvariable=self.var_dept,
                                  font=("times new roman", 12, "bold"), width=20, state="readonly")
        dept_combo["values"]=("-Select Department-", "CSE", "CSE_AIML", "IT", "ECE", "EE", "FT", "EIE", "ME")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1,padx=3, pady=10, sticky=W)

        # Course
        course_label = Label(course_frame, text="Course", font=("times new roman", 12, "bold"),bg="white")
        course_label.grid(row=0, column=2, padx=5, sticky=W)
        course_combo = ttk.Combobox(course_frame, textvariable=self.var_course, 
                                    font=("times new roman", 12, "bold"), width=20, state="readonly")
        course_combo["values"]=("-Select Course-", "B.Tech", "M.Tech", "B.Tech(Lateral)")
        course_combo.current(0)
        course_combo.grid(row=0, column=3,padx=3, pady=10, sticky=W)

        # Year
        year_label = Label(course_frame, text="Year", font=("times new roman", 12, "bold"),bg="white")
        year_label.grid(row=1, column=0, padx=5, sticky=W)
        year_combo = ttk.Combobox(course_frame, textvariable=self.var_year, 
                                  font=("times new roman", 12, "bold"), width=20, state="readonly")
        year_combo["values"]=("-Select Year-", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25")
        year_combo.current(0)
        year_combo.grid(row=1, column=1,padx=3, pady=10, sticky=W)

        # Semester
        sem_label = Label(course_frame, text="Semester", font=("times new roman", 12, "bold"),bg="white")
        sem_label.grid(row=1, column=2, padx=5, sticky=W)
        sem_combo = ttk.Combobox(course_frame, textvariable=self.var_sem, 
                                 font=("times new roman", 12, "bold"), width=20, state="readonly")
        sem_combo["values"]=("-Select Semester-", "Sem 1", "Sem 2", "Sem 3", "Sem 4", "Sem 5", 
                             "Sem 6", "Sem 7", "Sem 8", "Sem 9", "Sem 10")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3,padx=3, pady=10, sticky=W)

        # =========== Student Information Frame ============
        sinfo_frame = LabelFrame(left_frame, bg="white", bd=2, relief=RIDGE, text="Student Information", 
                                font=("times new roman", 15, "bold"))
        sinfo_frame.place(x=10, y=132, width=570, height=372)

        # Student Id
        sid_label = Label(sinfo_frame, text="Student ID",font=("times new roman", 12, "bold"),bg="white")
        sid_label.grid(row=0, column=0, padx=10, sticky=W)
        sid_entry = ttk.Entry(sinfo_frame, width=20, textvariable=self.var_sid,
                              font=("times new roman", 12, "bold"))
        sid_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # Student Roll No
        sroll_label = Label(sinfo_frame, text="Roll No.",font=("times new roman", 12, "bold"),bg="white")
        sroll_label.grid(row=0, column=2, padx=10, sticky=W)
        sroll_entry = ttk.Entry(sinfo_frame, width=20, textvariable=self.var_rollno,
                              font=("times new roman", 12, "bold"))
        sroll_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        # Student Name
        sname_label = Label(sinfo_frame, text="Name", font=("times new roman", 12, "bold"),bg="white")
        sname_label.grid(row=1, column=0, padx=10, sticky=W)
        sname_entry = ttk.Entry(sinfo_frame, width=20,  textvariable=self.var_name,
                                font=("times new roman", 12, "bold"))
        sname_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # Student phone number
        sphno_label = Label(sinfo_frame, text="Phone No.", font=("times new roman", 12, "bold"),bg="white")
        sphno_label.grid(row=1, column=2, padx=10, sticky=W)
        sphno_entry = ttk.Entry(sinfo_frame, width=20,  textvariable=self.var_phno, 
                                font=("times new roman", 12, "bold"))
        sphno_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # Student email
        smail_label = Label(sinfo_frame, text="Email", font=("times new roman", 12, "bold"),bg="white")
        smail_label.grid(row=2, column=0, padx=10, sticky=W)
        smail_entry = ttk.Entry(sinfo_frame, width=20,  textvariable=self.var_mail, 
                                font=("times new roman", 12, "bold"))
        smail_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # Student DOB
        sdob_label = Label(sinfo_frame, text="D.O.B", font=("times new roman", 12, "bold"),bg="white")
        sdob_label.grid(row=2, column=2, padx=10, sticky=W)
        sdob_entry = DateEntry(sinfo_frame, textvariable = self.var_dob, font=("times new roman", 12, "bold"),
                               selectmode='day', date_pattern='dd-MM-yyyy')
        sdob_entry.grid(row=2, column=3, padx=10, pady=0, sticky=W)
        
        # Student Address
        sadd_label = Label(sinfo_frame, text="Address", font=("times new roman", 12, "bold"),bg="white")
        sadd_label.grid(row=3, column=0, padx=10, sticky=W)
        sadd_entry = ttk.Entry(sinfo_frame, width=20,  textvariable=self.var_addr, 
                               font=("times new roman", 12, "bold"))
        sadd_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # Student Gender
        sgend_label = Label(sinfo_frame, text="Gender", font=("times new roman", 12, "bold"),bg="white")
        sgend_label.grid(row=3, column=2, padx=10, sticky=W)
        sgend_combo = ttk.Combobox(sinfo_frame, textvariable=self.var_gend, 
                                   font=("times new roman", 12, "bold"), width=18, state="readonly")
        sgend_combo["values"]=("-Select Gender-", "Male", "Female", "Others")
        sgend_combo.current(0)
        sgend_combo.grid(row=3, column=3,padx=10, pady=10, sticky=W)

        # =========== Radio Buttons ==============
        # Take Photo Sample
        self.var_radio1 = StringVar()
        radbtn1 = ttk.Radiobutton(sinfo_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radbtn1.grid(row=4,column=1, pady=5)

        # No Photo Sample
        radbtn2 = ttk.Radiobutton(sinfo_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radbtn2.grid(row=4,column=3, pady=5)

        # ===================== Buttons Frame ============================
        btn_frame = Frame(sinfo_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=30, y=230, width=490, height=36)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=12, cursor="hand2",
                          font=("times new roman", 12, "bold"), bg="green", fg="white")
        save_btn.grid(row=0, column=0, padx=2)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=12, cursor="hand2",
                          font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1, padx=2)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=12, cursor="hand2",
                            font=("times new roman", 12, "bold"), bg="red", fg="white")
        delete_btn.grid(row=0, column=2, padx=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=12, cursor="hand2",
                          font=("times new roman", 12, "bold"), bg="lightblue", fg="black")
        reset_btn.grid(row=0, column=3, padx=2)

        btn_frame1 = Frame(sinfo_frame, bd=0, relief=RIDGE, bg="white")
        btn_frame1.place(x=35, y=290, width=478, height=36)

        takePhoto_btn = Button(btn_frame1, command=self.generate_dataset, text="Take Photo", width=16, cursor="hand2", 
                          font=("times new roman", 12, "bold"), bg="lightblue", fg="black")
        takePhoto_btn.grid(row=0, column=0, padx=2)

        faceImg_btn = Button(btn_frame1, command=self.open_img, text="Face Images", width=16, cursor="hand2", 
                          font=("times new roman", 12, "bold"), bg="lightyellow", fg="black")
        faceImg_btn.grid(row=0, column=1, padx=2)
       
        # ============== Train Data Button =================
        train_btn = Button(btn_frame1, command=self.train_classifier, text="Train Data", cursor="hand2", width=16,
                       font=("times new roman", 12, "bold"), bg="lightgreen", fg="black")
        train_btn.grid(row=0, column=2, padx=2)

        # ======================= Right Label Frame =============================
        right_frame = LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE, text="Search Student", 
                                font=("times new roman", 18, "bold"))
        right_frame.place(x=630, y=10, width=685, height=555)

        # ================== Search Frame ==================
        search_frame = LabelFrame(right_frame, bd=0, bg="white", relief=RIDGE)
        search_frame.place(x=25, y=7, width=630, height=50)
        search_label = Label(search_frame, text="Search By:", 
                            font=("times new roman", 12, "bold"),bg="lightgreen", fg="black")
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.var_com_search = StringVar()
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_com_search, 
                                    font=("times new roman", 12, "bold"), width=12, state="readonly")
        search_combo["values"]=("-Select-", "Student_id", "Rollno", "Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1,padx=5, pady=10, sticky=W)

        self.var_search = StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.var_search,
                                width=20, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        search_btn = Button(search_frame, command=self.search_data, text="Search", width=10, 
                          font=("times new roman", 12, "bold"), bg="lightblue", fg="black")
        search_btn.grid(row=0, column=3, padx=3)

        showall_btn = Button(search_frame, command=self.fetch_data, text="Show All", width=10, 
                          font=("times new roman", 12, "bold"), bg="lightblue", fg="black")
        showall_btn.grid(row=0, column=4, padx=3)

        # =============== Table Frame ==================
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=65, width=655, height=445)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        

        self.student_table = ttk.Treeview(table_frame, 
                                          column=("student_id", "rollno", "name", "department", "course", "year",
                                            "semester", "phoneno", "mail", "gender", "address", "dob", "photo"),
                                            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("student_id", text="Student ID")
        self.student_table.heading("rollno", text="Roll No")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("department", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semseter")
        self.student_table.heading("phoneno", text="Phone No.")
        self.student_table.heading("mail", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("photo", text="Photo Sample")
        #self.student_table.heading("fp", text="Fingerprint Status")
        self.student_table["show"] = "headings"

        self.student_table.column("student_id", width=70,anchor=CENTER)
        self.student_table.column("rollno", width=100,anchor=CENTER)
        self.student_table.column("name", width=130,anchor=CENTER)
        self.student_table.column("department", width=80,anchor=CENTER)
        self.student_table.column("course", width=90,anchor=CENTER)
        self.student_table.column("year", width=80,anchor=CENTER)
        self.student_table.column("semester", width=60,anchor=CENTER)
        self.student_table.column("phoneno", width=90,anchor=CENTER)
        self.student_table.column("mail", width=140,anchor=CENTER)
        self.student_table.column("gender", width=60,anchor=CENTER)
        self.student_table.column("address", width=90,anchor=CENTER)
        self.student_table.column("dob", width=80,anchor=CENTER)
        self.student_table.column("photo", width=85,anchor=CENTER)
        #self.student_table.column("fp", width=120)

        #self.student_table.tag_configure("odd", background="#eee")
        #self.student_table.tag_configure("even", background="#ddd")

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ========================== Function Definition ===============================
    # =============== Add Student Function ================
    def add_data(self):
        if self.var_dept.get() == "Select Department" or self.var_name.get() == "" or self.var_sid.get() == "" or self.var_rollno.get() == "":
            messagebox.showerror("Error!", "All fields are required", parent = self.root)
        elif not self.is_valid_email(self.var_mail.get()):
            messagebox.showerror("Error!", "Invalid email address", parent=self.root)
        elif not self.var_phno.get().isdigit() or len(self.var_phno.get()) != 10:
            messagebox.showerror("Error!", "Invalid phone number. Please enter a 10-digit numeric phone number.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="1234",database="facerecog")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_sid.get(),
                                                                                                    self.var_rollno.get(),
                                                                                                    self.var_name.get(),
                                                                                                    self.var_dept.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_sem.get(),
                                                                                                    self.var_phno.get(),
                                                                                                    self.var_mail.get(),
                                                                                                    self.var_gend.get(),
                                                                                                    self.var_addr.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_radio1.get()
                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                self.reset_data()
                messagebox.showinfo("Success", "Student details added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    # ================ Fetch Data Function ===============
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="1234",database="facerecog")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ============== Get Cursor Function ===============
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_sid.set(data[0]),
        self.var_rollno.set(data[1]),
        self.var_name.set(data[2]),
        self.var_dept.set(data[3]),
        self.var_course.set(data[4]),
        self.var_year.set(data[5]),
        self.var_sem.set(data[6]),
        self.var_phno.set(data[7]),
        self.var_mail.set(data[8]),
        self.var_gend.set(data[9]),
        self.var_addr.set(data[10]),
        self.var_dob.set(data[11]),
        self.var_radio1.set(data[12])
   
    # ============== Open Images from Face Images =================
    def open_img(self):
        os.startfile("data")

    # =============== Update Data Function ===================
    def update_data(self):
        if self.var_dept.get() == "Select Department" or self.var_name.get() == "" or self.var_sid.get() == "" or self.var_rollno.get() == "":
            messagebox.showerror("Error!", "All fields are required", parent = self.root)
        elif not self.is_valid_email(self.var_mail.get()):
            messagebox.showerror("Error!", "Invalid email address", parent=self.root)
        elif not self.var_phno.get().isdigit() or len(self.var_phno.get()) != 10:
            messagebox.showerror("Error!", "Invalid phone number. Please enter a 10-digit numeric phone number.", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update","Do  you want to update this student details?", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="1234",database="facerecog")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set rollno=%s,name=%s,department=%s,course=%s,year=%s,semester=%s,phoneno=%s,mail=%s,gender=%s,address=%s,dob=%s,photo=%s where student_id=%s",(
                                                                                                    self.var_rollno.get(),
                                                                                                    self.var_name.get(),
                                                                                                    self.var_dept.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_sem.get(),
                                                                                                    self.var_phno.get(),
                                                                                                    self.var_mail.get(),
                                                                                                    self.var_gend.get(),
                                                                                                    self.var_addr.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_radio1.get(),
                                                                                                    self.var_sid.get()
                                                                                                ))    
                else:
                    if not update:
                        return            
                messagebox.showinfo("Success","Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()                
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    # ============== Delete Student Function ==============
    def delete_data(self):
        if self.var_sid.get() == "":
            messagebox.showerror("Error","Student id is required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete","Do you want delete this student details?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="1234",database="facerecog")
                    my_cursor = conn.cursor()
                    query = "delete from student where student_id=%s"
                    val=(self.var_sid.get(),)
                    my_cursor.execute(query, val)
                else:
                    if not delete:
                        return                    
                conn.commit()
                self.fetch_data()
                conn.close()
                self.reset_data()
                messagebox.showinfo("Delete","Successfully deleted",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    # ============== Reset Function ===============
    def reset_data(self):
        self.var_sid.set("")
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_dept.set("-Select Department-")
        self.var_course.set("-Select Course-")
        self.var_year.set("-Select Year-")
        self.var_sem.set("-Select Semester-")
        self.var_phno.set("")
        self.var_mail.set("")
        self.var_gend.set("-Select Gender-")
        self.var_addr.set("")
        self.var_dob.set("")
        self.var_radio1.set("")

    # ================== Check for Valid Email ================
    def is_valid_email(self, email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return True if re.match(pattern, email) else False

    # =================== Search Function ========================
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select any option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="1234",database="facerecog")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for  i in data:
                        self.student_table.insert("",END, values=i)
                    conn.commit()
                conn.close()          
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    # ================= Generate Data Set or Take Photo Sample ===================
    def generate_dataset(self):
        if self.var_dept.get() == "Select Department" or self.var_name.get() == "" or self.var_sid.get() == "" or self.var_rollno.get() == "":
            messagebox.showerror("Error!", "All fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="1234",database="facerecog")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set rollno=%s,name=%s,department=%s,course=%s,year=%s,semester=%s,phoneno=%s,mail=%s,gender=%s,address=%s,dob=%s,photo=%s where student_id=%s",(
                                                                                                    self.var_rollno.get(),
                                                                                                    self.var_name.get(),
                                                                                                    self.var_dept.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_sem.get(),
                                                                                                    self.var_phno.get(),
                                                                                                    self.var_mail.get(),
                                                                                                    self.var_gend.get(),
                                                                                                    self.var_addr.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_radio1.get(),
                                                                                                    self.var_sid.get()==id+1
                                                                                                ))

                conn.commit()    
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ========= Load predefined data on face frontals from opencv ============
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")                
                def face_cropped(img):
                    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # Scaling Factor = 1.3
                    # Minimum Neighbour = 5     
                    for(x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face= cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break               
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Sets Completed",parent=self.root)  # CHANGE HERE
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    # ==================== Train Data Function ====================
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img = Image.open(image).convert('L')  # Gray scale image
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        # ========= Train the Classifier & Save =============
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets Completed!", parent=self.root)

    # ============== Exit / Logout ==================
    def iExit(self):
        #self.iExit = tkinter.messagebox.askyesno("LOGOUT", "Are you sure to Logout?", parent=self.root)
        #if self.iExit > 0:
            # self.main_window.destroy()
        #    self.root.destroy()
        #else:
        #    return
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    # main_window = Toplevel(root)
    obj = Student(root)
    root.mainloop()