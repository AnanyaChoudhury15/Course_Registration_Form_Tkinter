from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import pymysql

class CourseRegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Course Registration Form")
        self.root.geometry('1000x1000+0+0')
        self.root.resizable(0, 0)

        self.frame = Frame(self.root, width=1000, height=1000, bg='black', bd=8)
        self.frame.place(x=0, y=0)

        self.show_course_registration_page()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def submit_form(self):
        if self.name_entry.get() == '':
            messagebox.showerror("ALERT!", "Please enter your name.")
        elif self.email_entry.get() == '':
            messagebox.showerror("ALERT!", "Please enter your email.")
        elif self.phone_entry.get() == '':
            messagebox.showerror("ALERT!", "Please enter your Phone number.")
        elif self.address_entry.get() == '':
            messagebox.showerror("ALERT!", "Please enter your Address.")
        elif self.course_var.get() == '':
            messagebox.showerror("ALERT!", "Please select a course.")
        elif self.date_entry.get() == '':
            messagebox.showerror("ALERT!", "Please enter a date.")
        elif self.mode_var.get() == '':
            messagebox.showerror("ALERT!", "Please enter mode.")
        elif self.student_id_entry.get() == '':
            messagebox.showerror("ALERT!", "Please enter your Student id.")
        elif self.program_entry.get() == '':
            messagebox.showerror("ALERT!", "Please enter your degree program.")
        elif self.payment_var.get() == '':
            messagebox.showerror("ALERT!", "Please enter Payment mode.")
        else:
            db = pymysql.connect(host='localhost', user='root', password='An@150604', database='Personal_Registration_form')
            cur = db.cursor()

            try:
                query = 'use Personal_Registration_form'
                cur.execute(query)

                query = '''create table if not exists C_details(
                    id int auto_increment primary key not null,
                    Name varchar(40),
                    email varchar(40),
                    Phone varchar(40),
                    Address varchar(100),
                    Course varchar(40),
                    Date varchar(40),
                    Mode varchar(40),
                    StudentId varchar(40),
                    Degree varchar(40),
                    Payment varchar(40)
                )'''
                cur.execute(query)
                db.commit()

            except Exception as e:
                print(e)

            try:
                query = '''insert into C_details(
                    Name, email, Phone, Address, Course, Date, Mode, StudentId, Degree, Payment
                ) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
                cur.execute(query, (
                    self.name_entry.get(), self.email_entry.get(), self.phone_entry.get(),
                    self.address_entry.get(), self.course_var.get(), self.date_entry.get(),
                    self.mode_var.get(), self.student_id_entry.get(), self.program_entry.get(),
                    self.payment_var.get()
                ))
                db.commit()
                db.close()
                messagebox.showinfo('Success', 'Successful Registration!!')


                messagebox.showinfo("Registration Successful", "You have successfully registered for the course.\nFurther details will be sent to your email, and we will contact you.")

                

                self.root.destroy()
                import HomePage

            except Exception as e:
                messagebox.showerror('Error', str(e))
                db.rollback()
                db.close()

    def show_course_registration_page(self):
        self.clear_frame()

        heading = Label(self.frame, text='COURSE REGISTRATION FORM', bg='black', fg='#97ffff', font=('Calibre', 30, 'bold'))
        heading.place(x=200, y=3)

        # Personal Information
        name_label = Label(self.frame, text="Full Name:", bg='black', fg='#97ffff', font=('Calibre', 15,'bold'))
        name_label.place(x=300, y=100)
        self.name_entry = Entry(self.frame, font=('Calibre', 15,'bold'))
        self.name_entry.place(x=600, y=100)

        email_label = Label(self.frame, text="Email:", bg='black', fg='#97ffff', font=('Calibre', 15,'bold'))
        email_label.place(x=300, y=140)
        self.email_entry = Entry(self.frame, font=('Calibre', 15,'bold'))
        self.email_entry.place(x=600, y=140)

        phone_label = Label(self.frame, text="Phone Number:", bg='black', fg='#97ffff', font=('Calibre', 15,'bold'))
        phone_label.place(x=300, y=180)
        self.phone_entry = Entry(self.frame, font=('Calibre', 15,'bold'))
        self.phone_entry.place(x=600, y=180)

        address_label = Label(self.frame, text="Address:", bg='black', fg='#97ffff', font=('Calibre', 15,'bold'))
        address_label.place(x=300, y=220)
        self.address_entry = Entry(self.frame, font=('Calibre', 15,'bold'))
        self.address_entry.place(x=600, y=220)

        # Course Information
        course_label = Label(self.frame, text="Select Course:", bg='black', fg='#97ffff', font=('Calibre', 15,'bold'))
        course_label.place(x=300, y=260)
        courses = ["Web Development", "Machine Learning", "Cyber Security", "Artificial Intelligence"]
        self.course_var = StringVar()
        course_menu = ttk.Combobox(self.frame, textvariable=self.course_var, values=courses, font=('Calibre', 15,'bold'), state='readonly')
        course_menu.place(x=600, y=260)

        date_label = Label(self.frame, text="Preferred Start Date:", bg='black', fg='#97ffff', font=('Calibre', 15,'bold'))
        date_label.place(x=300, y=300)
        self.date_entry = DateEntry(self.frame, font=('Calibre', 15), width=19, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd-mm-y')
        self.date_entry.place(x=600, y=300)

        mode_label = Label(self.frame, text="Mode of Study:", bg='black', fg='#97ffff', font=('Calibre', 15,'bold'))
        mode_label.place(x=300, y=340)
        modes = ["Online", "Offline", "Hybrid"]
        self.mode_var = StringVar()
        mode_menu = ttk.Combobox(self.frame, textvariable=self.mode_var, values=modes, font=('Calibre', 15,'bold'), state='readonly')
        mode_menu.place(x=600, y=340)

        # Additional Information
        student_id_label = Label(self.frame, text="Student USN:", bg='black', fg='#97ffff', font=('Calibre', 15,'bold'))
        student_id_label.place(x=300, y=380)
        self.student_id_entry = Entry(self.frame, font=('Calibre', 15))
        self.student_id_entry.place(x=600, y=380)

        program_label = Label(self.frame, text="Current Degree Program:", bg='black', fg='#97ffff', font=('Calibre', 15,'bold'))
        program_label.place(x=300, y=420)
        self.program_entry = Entry(self.frame, font=('Calibre', 15))
        self.program_entry.place(x=600, y=420)

        payment_label = Label(self.frame, text="Payment Method:", bg='black', fg='#97ffff', font=('Calibre', 15,'bold'))
        payment_label.place(x=300, y=460)
        payments = ["Credit Card", "UPI", "Bank Transfer"]
        self.payment_var = StringVar()
        payment_menu = ttk.Combobox(self.frame, textvariable=self.payment_var, values=payments, font=('Calibre', 15,'bold'), state='readonly')
        payment_menu.place(x=600, y=460)

        submit_button = Button(self.frame, text='SUBMIT', width=15, borderwidth=5, height=2, bg='#7f7fff', fg='white', cursor='hand2',
                               border=2, font=('#57a1f8', 16, 'bold'), command=self.submit_form)
        submit_button.place(x=470, y=540)

if __name__ == "__main__":
    root = Tk()
    app = CourseRegistrationApp(root)
    root.mainloop()
