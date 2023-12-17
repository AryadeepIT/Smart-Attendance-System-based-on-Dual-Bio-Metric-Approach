from tkinter import *
from PIL import  Image, ImageTk
import os, time,tkinter
from time import strftime
from student import Student
from attendance import Attendance

class Attendance_System:
    def __init__(self, root, fname):
        self.root = root
        self.fname = fname
        self.root.geometry("1350x690+0+0") 
        self.root.configure(bg='lightblue')
        self.root.title("AUTOMATED ATTENDANCE SYSTEM")
        self.child_windows = []

        # Techno logo
        logo_img = Image.open("Images/tmsl.png")
        self.photoimg = ImageTk.PhotoImage(logo_img)
        f_label = Label(self.root, image=self.photoimg)
        f_label.place(x=0, y=0, width=98, height=94)

        # Title Label
        title_label = Label(root, text="AUTOMATED ATTENDANCE SYSTEM",
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
        fname_label_width = 230 
        fname_label_x = logout_x - (fname_label_width - logout_width) // 2 
        fname_label_y = logout_y - 30 
        self.user_label = Label(root, text=f"Welcome, {fname}", font=("times new roman", 12), bg='lightyellow')
        self.user_label.place(x=fname_label_x, y=fname_label_y, width=fname_label_width)

        # =========== Student Details button ==============
        student_img = Image.open("Images/student.png")
        self.studentimg = ImageTk.PhotoImage(student_img)
        b1 = Button(root, image=self.studentimg, command=self.student_details, cursor="hand2")
        b1.place(x=450, y=300, width=150, height=125)
        b1_1 = Button(root, text="Student Details", command=self.student_details, cursor="hand2", 
                      font=("times new roman", 14, "bold"),bg="darkblue", fg="white", 
                      activebackground="darkblue", activeforeground="white")
        b1_1.place(x=450, y=420, width=150, height=30)

        # ========== Attendance Report button =============
        attend_img = Image.open("Images/attendance.png")
        self.attendimg = ImageTk.PhotoImage(attend_img)
        b1 = Button(root, image=self.attendimg, cursor="hand2", command=self.attendance_data)
        b1.place(x=720, y=300, width=150, height=125)
        b1_1 = Button(root, text="Mark Attendance", cursor="hand2", command=self.attendance_data,
                      font=("times new roman", 14, "bold"),bg="darkblue", fg="white",
                      activebackground="darkblue", activeforeground="white")
        b1_1.place(x=720, y=420, width=150, height=30)

        global datetimeLabel
        datetimeLabel = Label(root,font=('times new roman',18,'bold'), bg="lightblue")
        datetimeLabel.place(x=2,y=105)
        self.clock()

    # =========================== Function Declaration ====================================
    def clock(self):
        global date,currenttime
        date = time.strftime('%d/%m/%Y')
        currenttime = time.strftime('%H:%M:%S')
        datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
        datetimeLabel.after(1000, self.clock)  

    def iExit(self):
        #result = tkinter.messagebox.askyesno("LOGOUT", "Are you sure to Logout?", parent=self.root)
        #if result:
        #    self.root.destroy()
        #else:
        #    return
        for window in self.child_windows:
            window.destroy()
        self.root.destroy()
        
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.child_windows.append(self.new_window)
        self.app = Student(self.new_window, self.fname)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.child_windows.append(self.new_window)
        self.app = Attendance(self.new_window, self.fname)

if __name__ == "__main__":
    root = Tk()
    obj = Attendance_System(root)
    root.mainloop()
