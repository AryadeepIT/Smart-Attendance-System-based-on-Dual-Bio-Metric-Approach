from tkinter import *
from tkinter import ttk, messagebox
from PIL import  Image, ImageTk
import mysql.connector, re
from main import Attendance_System

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.bind('<Return>', self.on_enter_key_press)
        self.root.title("LOGIN")
        self.root.geometry("1350x690+0+0")
        self.root.configure(bg='lightblue')
        self.full_name = ""

        # Techno logo
        logo_img = Image.open("Images/tmsl.png")
        self.photoimg = ImageTk.PhotoImage(logo_img)
        f_label = Label(self.root, image=self.photoimg)
        f_label.place(x=0, y=0, width=98, height=94)

        # Title Label
        title_label = Label(text="WELCOME TO ATTENDANCE MANAGEMENT SYSTEM",
                            font=("times new roman", 32, "bold"),bg="lightyellow", fg="darkgreen")
        title_label.place(x=98, y=0,width=1250,height=94)

        frame = Frame(self.root, bg="black")
        frame.place(x=500, y=160, width=340, height=460)

        img1 = Image.open(r"Images\login.jpg")
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(frame, image=self.photoimg1, bg="black",borderwidth=0)
        lblimg1.place(x=130, y=5, width=90, height=90)

        get_start = Label(frame, text="Get Started", font=("times new roman", 18, "bold"), bg="black", fg="white")
        get_start.place(x=110, y=100)

        # ========== Username Label =============
        username_lbl = Label(frame, text="Username", font=("times new roman", 15), bg="black", fg="white")
        username_lbl.place(x=80, y=150)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15))
        self.txtuser.place(x=50, y=180, width=240)

        img2 = Image.open("Images/user.png")
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(frame, image=self.photoimg2, bg="black",borderwidth=0)
        lblimg2.place(x=50, y=150, width=25, height=25)

        # ========== Password Label =============
        pass_lbl = Label(frame, text="Password", font=("times new roman", 15), bg="black", fg="white")
        pass_lbl.place(x=80, y=230)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15), show='*')
        self.txtpass.place(x=50, y=260, width=240)
        img3 = Image.open("Images/password.jpeg")
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(frame, image=self.photoimg3, bg="black",borderwidth=0)
        lblimg3.place(x=50, y=230, width=25, height=25)

        # ============ Show / Hide Password =============
        self.show_pass_var = IntVar()
        self.show_pass_checkbtn = Checkbutton(frame, text="Show Password", variable=self.show_pass_var,cursor="hand2",  
                                              onvalue=1, offvalue=0, command=self.toggle_password, 
                                              font=("times new roman", 8), bg="black", fg="white", 
                                              activebackground="black", activeforeground="white", selectcolor="black")
        self.show_pass_checkbtn.place(x=197, y=235)

        # ========= Login Button ==========
        loginBtn = Button(frame, text="Login", cursor="hand2", font=("times new roman", 15, "bold"), 
                          bd=3, relief=RIDGE, fg="white", command=self.login, bg="green", 
                          activeforeground="white", activebackground="green")
        loginBtn.place(x=120, y=310, width=100, height=35)

        # ========= New User Button ==========
        newUserBtn = Button(frame, text="New User Register", font=("times new roman", 10), borderwidth=0,
                            command=self.register_window, fg="white", bg="black", cursor="hand2", 
                            activebackground="black", activeforeground="white")
        newUserBtn.place(x=40, y=375, width=110, height=25)

        # ========= Forget Password Button ==========
        forgetPassBtn = Button(frame, text="Forget Password", command=self.forgot_pass, cursor="hand2", 
                               font=("times new roman", 10), borderwidth=0, fg="white", bg="black", 
                               activebackground="black", activeforeground="white")
        forgetPassBtn.place(x=40, y=410, width=100, height=25)

    # ============== Login Function ===============
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error!", "All fields required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="facerecog")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where uname=%s and password=%s",(self.txtuser.get(), 
                                                                                       self.txtpass.get()
                                                                                       ))
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                self.full_name = row[0]
                open_main = messagebox.askyesno("Yes/No", "Access only admin")
                if open_main>0:
                    messagebox.showinfo("Success", "Welcome {}".format(self.full_name))
                    self.new_window=Toplevel(self.root)
                    self.app = Attendance_System(self.new_window, self.full_name)
                    self.reset_login()    
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close() 
            self.show_pass_var.set(0)

    # Add this method to handle the "Enter" key press event
    def on_enter_key_press(self, event):
        self.login()    
        self.show_pass_var.set(0)           

    # ============ Show / Hide Password =============
    def toggle_password(self):
        if self.show_pass_var.get() == 1:
            self.txtpass.config(show="")
        else:
            self.txtpass.config(show="*")

    # ============ Show / Hide Password =============
    def toggle_newpassword(self):
        if self.show_pass_var.get() == 1:
            self.new_password_entry.config(show="")
        else:
            self.new_password_entry.config(show="*")

    # =========== Reset Login Credentials =============
    def reset_login(self):
        self.txtuser.delete(0,END)
        self.txtpass.delete(0,END)
    
    # ========== Register Function ==============
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)
 
    # =========== Forgot Password =============
    def forgot_pass(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter username to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="facerecog")
            my_cursor = conn.cursor()
            value=(self.txtuser.get(),)
            my_cursor.execute("select * from register where uname=%s", value)
            row=my_cursor.fetchone()
            
            if row == None:
                messagebox.showerror("Error!", "Please enter valid username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.configure(bg="black")
                self.root2.geometry("340x450+500+180")

                img4 = Image.open("Images/forgotpass.png")
                self.photoimg4 = ImageTk.PhotoImage(img4)
                lblimg4 = Label(self.root2, image=self.photoimg4, bg="black",borderwidth=0)
                lblimg4.place(x=5, y=5, width=50, height=50)
                forgotPass_label = Label(self.root2, text="Forgot Password", 
                                         font=("times new roman", 18), fg="red", bg="black")
                forgotPass_label.place(x=80, y=10)

                securityQ = Label(self.root2,text="Secuity Question", font=("times new roman", 14), 
                                  bg="black", fg="white")
                securityQ.place(x=50, y=80)
                self.securityQ_combo = ttk.Combobox(self.root2, 
                                       font=("times new roman", 12), width=20, state="readonly")
                self.securityQ_combo["values"]=("-Select Security Question-", "In what city were you born?", 
                                "What is the name of your pet?", "What high school did you attend?", 
                                "What is your favorite movie?")
                self.securityQ_combo.current(0)
                self.securityQ_combo.place(x=50, y=110, width=240)

                securityA = Label(self.root2,text="Secuity Answer", font=("times new roman", 14), 
                                  bg="black", fg="white")
                securityA.place(x=50, y=150)
                self.securityA_entry = ttk.Entry(self.root2, font=("times new roman", 14))
                self.securityA_entry.place(x=50, y=180, width=240)

                new_password = Label(self.root2,text="New Password", font=("times new roman", 14), 
                                     bg="black", fg="white")
                new_password.place(x=50, y=220)
                self.new_password_entry = ttk.Entry(self.root2, font=("times new roman", 14), show='*')
                self.new_password_entry.place(x=50, y=250, width=240)

                self.show_pass_var = IntVar()
                self.show_pass_checkbtn = Checkbutton(self.root2, text="Show Password", variable=self.show_pass_var, cursor="hand2",  
                                              onvalue=1, offvalue=0, command=self.toggle_newpassword, 
                                              font=("times new roman", 8), bg="black", fg="white", 
                                              activebackground="black", activeforeground="white", selectcolor="black")
                self.show_pass_checkbtn.place(x=197, y=225)

                confirm_newPass = Label(self.root2,text="Confirm Password", font=("times new roman", 14), 
                                        bg="black", fg="white")
                confirm_newPass.place(x=50, y=290)
                self.confirm_newPass_entry = ttk.Entry(self.root2, font=("times new roman", 14), show='*')
                self.confirm_newPass_entry.place(x=50, y=320, width=240)

                reset_btn = Button(self.root2, text="Reset", font=("times new roman", 14), command=self.reset_pass, cursor="hand2",
                                   bg="green", fg="white")
                reset_btn.place(x=140, y=380)    

    # ================= Reset Password ====================
    def reset_pass(self):
        if self.securityQ_combo.get()=="-Select Security Question-":
            messagebox.showerror("Error","Select Security Question", parent=self.root2)

        elif self.securityA_entry.get()=="":
            messagebox.showerror("Error", "Please enter the answer", parent=self.root2)

        elif self.new_password_entry.get()=="":
            messagebox.showerror("Error", "Please enter new password", parent=self.root2) 

        elif self.new_password_entry.get() != self.confirm_newPass_entry.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same", parent=self.root2)

        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="facerecog")
            my_cursor = conn.cursor()
            query = ("select * from register where uname=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.securityQ_combo.get(), self.securityA_entry.get())
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Please enter correct security answer", parent=self.root2)
            else:
                qry=("update register set password=%s where uname=%s")
                val=(self.new_password_entry.get(), self.txtuser.get())
                my_cursor.execute(qry, val)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been reset, please login with new password", parent=self.root2)
                self.root2.destroy()

# =========================================== Register Class ==========================================================
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("NEW USER REGISTRATION")
        self.root.geometry("1350x690+0+0")
        self.root.configure(bg='lightblue')

        # ========= Text Variables ===========
        self.var_fname = StringVar()
        self.var_uname = StringVar()
        self.var_phno = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confirmPass = StringVar()
        self.var_showpass = IntVar()
        self.var_check = IntVar()

        # Techno logo
        logo_img = Image.open("Images/tmsl.png")
        self.photoimg = ImageTk.PhotoImage(logo_img)
        f_label = Label(self.root, image=self.photoimg)
        f_label.place(x=0, y=0, width=98, height=94)

        # Title Label
        title_label = Label(root, text="NEW USER REGISTRATION",
                            font=("times new roman", 32, "bold"),bg="lightyellow", fg="darkgreen")
        title_label.place(x=98, y=0,width=1250,height=94)

        # =========== Main Frame ==============
        frame = Frame(self.root, bg="black")
        frame.place(x=400, y=125, width=500, height=530)

        register_lbl = Label(frame, text = "REGISTER HERE",font=("times new roman", 18, "bold"),
                             bg="black", fg="green")
        register_lbl.place(x=150, y=10)
  
        # ============ Labels & Entry Fields =============
        fname = Label(frame,text="Full Name", font=("times new roman", 15), bg="black", fg="white")
        fname.place(x=30, y=90)
        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15))
        fname_entry.place(x=30, y=120, width=200)

        uname = Label(frame,text="Username", font=("times new roman", 15), bg="black", fg="white")
        uname.place(x=270, y=90)
        uname_entry = ttk.Entry(frame, textvariable=self.var_uname, font=("times new roman", 15))
        uname_entry.place(x=270, y=120, width=200)

        phno = Label(frame,text="Contact No.", font=("times new roman", 15), bg="black", fg="white")
        phno.place(x=30, y=170)
        phno_entry = ttk.Entry(frame, textvariable=self.var_phno, font=("times new roman", 15))
        phno_entry.place(x=30, y=200, width=200)

        email = Label(frame,text="Email", font=("times new roman", 15), bg="black", fg="white")
        email.place(x=270, y=170)
        email_entry = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        email_entry.place(x=270, y=200, width=200)

        securityQ = Label(frame,text="Secuity Question", font=("times new roman", 15), bg="black", fg="white")
        securityQ.place(x=30, y=250)
        securityQ_combo = ttk.Combobox(frame, textvariable=self.var_securityQ, 
                                       font=("times new roman", 12), width=20, state="readonly")
        securityQ_combo["values"]=("-Select Security Question-", "In what city were you born?", 
                                "What is the name of your pet?", "What high school did you attend?", 
                                "What is your favorite movie?")
        securityQ_combo.current(0)
        securityQ_combo.place(x=30, y=280, width=200)

        securityA = Label(frame,text="Secuity Answer", font=("times new roman", 15), bg="black", fg="white")
        securityA.place(x=270, y=250)
        securityA_entry = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        securityA_entry.place(x=270, y=280, width=200)

        password = Label(frame,text="Password", font=("times new roman", 15), bg="black", fg="white")
        password.place(x=30, y=330)
        self.password_entry = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show='*')
        self.password_entry.place(x=30, y=360, width=200)

        # ============ Show / Hide Password =============
        self.show_pass_checkbtn = Checkbutton(frame, text="Show Password", variable=self.var_showpass, cursor="hand2", 
                                              onvalue=1, offvalue=0, command=self.newuser_password, 
                                              font=("times new roman", 8), bg="black", fg="white", 
                                              activebackground="black", activeforeground="white", selectcolor="black")
        self.show_pass_checkbtn.place(x=135, y=335)

        confirm_pass = Label(frame,text="Confirm Password", font=("times new roman", 15), bg="black", fg="white")
        confirm_pass.place(x=270, y=330)
        confirm_pass_entry = ttk.Entry(frame, textvariable=self.var_confirmPass, font=("times new roman", 15), show='*')
        confirm_pass_entry.place(x=270, y=360, width=200)

        # =========== Check Box ============
        self.checkBtn = Checkbutton(frame, variable=self.var_check, cursor="hand2", 
                                    text="I Agree to the Terms & Conditions", font=("times new roman", 10,"bold"),
                               bg="lightblue", fg="black", onvalue=1, offvalue=0, activebackground="lightblue", activeforeground="black")
        self.checkBtn.place(x=30, y=415)

        # ========= Register Button ========== 
        registerBtn = Button(frame, text="Register",font=("times new roman",14,"bold"),command=self.register_data, cursor="hand2",  
                            relief=RIDGE,bd=3,fg="white",bg="green", activeforeground="white",activebackground="green")
        registerBtn.place(x=80, y=460, width=100, height=32)

        # ========= Login Button ==========
        loginBtn = Button(frame, text="Login", font=("times new roman", 14, "bold"), command=self.return_login, cursor="hand2", 
                          bd=3, relief=RIDGE, fg="white", bg="blue", activeforeground="white", activebackground="blue")
        loginBtn.place(x=320, y=460, width=100, height=32)

    # ================================ Function Declaration =======================================
    # ============ Show / Hide Password =============
    def newuser_password(self):
        if self.var_showpass.get() == 1:
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    # =============== Login Button in Register page ==================
    def return_login(self):
        self.root.destroy()
        
    # ============== New User Register Function ===============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_uname.get()=="" or self.var_phno.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="-Select Secuity Question-" or self.var_pass.get()=="":
            messagebox.showerror("Error!!", "All fields required", parent=self.root)
        elif not self.is_valid_email(self.var_email.get()):
            messagebox.showerror("Error!", "Invalid email address", parent=self.root)
        elif not self.var_phno.get().isdigit() or len(self.var_phno.get()) != 10:
            messagebox.showerror("Error!", "Invalid phone number. Please enter a 10-digit numeric phone number.", parent=self.root)      
        elif self.var_pass.get() != self.var_confirmPass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to the trems & conditins", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="facerecog")
            my_cursor = conn.cursor()
            query = "select * from register where email=%s"
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","User already exist, please try another email", parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_uname.get(),
                                                                                    self.var_phno.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_pass.get()
                                                                                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "You are successfully registered :)")    

    # ================== Check for Valid Email ================
    def is_valid_email(self, email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return True if re.match(pattern, email) else False  

if __name__ == "__main__":
    main()

