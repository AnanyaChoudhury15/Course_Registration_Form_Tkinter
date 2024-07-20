from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql

#windows
windows=Tk()
windows.title('Login Screen')
windows.resizable(0,0)
windows.geometry('490x240+200+200')

#database

def forgotbtn():
    windows.destroy()
    import Forgot_password


def login():
    if emailentry.get() == '':
        messagebox.showerror('Alert!','Please enter your email.')
    elif passwordentry.get() == '':
        messagebox.showerror('Alert!', 'Please enter your password.')
    else:
        db=pymysql.connect(host='localhost',user='root',password='An@150604',database='Personal_Registration_form')
        cur=db.cursor()
        query='select * from p_details where password=%s'
        cur.execute(query, (passwordentry.get()))

        row=cur.fetchone()
        if row == None:
            messagebox.showerror('Alert', 'Incorrect email or password')
            return
        else:
            messagebox.showinfo('Success', 'Login successful')
            messagebox.showinfo('', 'Welcome!!')
    windows.destroy()
    import Course_Registration_form
    root = Tk()
    Course_Registration_form.CourseRegistrationApp(root)

            

        

        
        

#check box configuration
def show():
    passwordentry.configure(show='*')
    check.configure(command=hide, text='')
def hide():
    passwordentry.configure(show='')
    check.configure(command=show, text='')

#event/binding

def On_FocusEmailIn(event):
    emailentry.delete(0, END)

def On_FocusEmailOut(event):
    name=emailentry.get()
    if name == '':
        emailentry.insert(0, 'EMAIL')

def On_FocusPasswdIn(event):
    passwordentry.delete(0,END)

def On_FocusPasswdOut(event):
    passw=passwordentry.get()
    if passw == '':
        passwordentry.insert(0, 'PASSWORD')


def newone():
    windows.destroy()
    import Registrationform

def home():
    windows.destroy()
    import HomePage


#frame
frame=Frame(windows, width=700, height=400, bg='black')
frame.place(x=0, y=0)

#Labels
Logoimage= PhotoImage(file='email (1).png')
emailLabel= Label(frame, text='Email:', fg='#97ffff', image=Logoimage, compound=LEFT, bg='black',
                 font=('Calibre',14,'bold') )
emailLabel.grid(row=1, column=0, pady=20, padx=3)

passwordimage=PhotoImage(file='padlock.png')
passwordlabel= Label(frame, image=passwordimage, compound=LEFT, fg='#97ffff', bg='black', text='Password:',
                    font=('Calibre',14,'bold') )
passwordlabel.grid(row=3, column=0, pady=10, padx=3)

#Entry fields
emailentry=Entry(frame, width=39, bd=3)
emailentry.grid(row=1, column=2, columnspan=2, padx=57)

passwordentry=Entry(frame, width=39, bd=3)
passwordentry.grid(row=3, column=2, columnspan=2)


loginbtn=Button(frame, text='LOGIN', bg='#7f7fff', pady=10, width=23, fg='white', font=('Open sans', 9, 'bold'), 
                cursor='hand2',border=0, borderwidth=5, command=login)
loginbtn.grid(row=9, columnspan=5, pady=30)

donthvacclabel= Label(frame, text='Don\'t have an account?', fg='#97ffff', bg='black', padx=4, font=('Harrington',9,'bold'))
donthvacclabel.place(x=0, y=170)

createnewacc=Button(frame, width=15, text='Create One', border=0, bg='white', fg='black', cursor='hand2',
                    font=('tahoma', 8, 'bold'), command=newone)
createnewacc.place(x=10, y=199)

fgtpassw=Button(frame, text='Forgot Password?', fg='#97ffff', border=0, cursor='hand2', bg='black',
                font=('Harrington',9,'bold'),command=forgotbtn)
fgtpassw.place(x=310, y=120)

#string of information
emailentry.insert(0, '@email.com')
passwordentry.insert(0, 'password')

#event/binding
emailentry.bind('<FocusIn>', On_FocusEmailIn)
emailentry.bind('<FocusOut>', On_FocusEmailOut)

passwordentry.bind('<FocusIn>', On_FocusPasswdIn)
passwordentry.bind('<FocusOut>', On_FocusPasswdOut)

#checkbox
check=Checkbutton(frame, text='', bg='black',command=show)
check.place(x=440, y=95)



windows.mainloop()