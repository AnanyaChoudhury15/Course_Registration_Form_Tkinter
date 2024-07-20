from tkinter import *
from tkinter import messagebox
import pymysql


#window
windows=Tk()
windows.geometry('500x460+500+10')
windows.resizable(False,False)
windows.title('Forgot Password')

#frame
frame=Frame(windows,width=540,height=640,bg='black',bd=8)
frame.place(x=0,y=0)

Font=('Calibre',16,'bold')


def back():
    windows.destroy()
    import Login_page

def submit():
    if usernameEntry.get() == '' or EmailEntry.get()=='' or NewPasswordEntry.get()=='' or ConfirmPasswordEntry.get()=='':
        messagebox.showerror('Alert','Entry fields must be entered')
        return
    
    elif NewPasswordEntry.get() != ConfirmPasswordEntry.get():
        messagebox.showerror("Alert",'Passwords does not match!')
        return
    else:
        db=pymysql.connect(host='localhost',user='root',password='An@150604',database='Personal_Registration_form')
        cur=db.cursor()

        query='select * from p_details where email=%s'
        cur.execute(query,(EmailEntry.get()))
        row=cur.fetchone() #to fetch the existing data 
        if row==None:
            messagebox.showerror('Alert','This email does not exist.Please input your registered email address')
            return
        else:
            query='update p_details set password=%s where email=%s'  #line to update the password
            cur.execute(query,(NewPasswordEntry.get(), EmailEntry.get()))
            db.commit()
            db.close()
            messagebox.showinfo('Success','Successful changes. Please login with the new password')

            usernameEntry.delete(0,END)
            EmailEntry.delete(0,END)
            NewPasswordEntry.delete(0,END)
            ConfirmPasswordEntry.delete(0,END)


            windows.destroy()
            import Login_page



#labels and btn
heading=Label(frame,text='FORGOT PASSWORD',fg="#97ffff",bg='black', font=('Calibre',23,'bold'))
heading.place(x=100,y=3)

passwordImage=PhotoImage(file='padlock.png')
passwordLabel=Label(frame,image=passwordImage)
passwordLabel.place(x=45,y=3)

usernamelbl=Label(frame,text='Username:',fg='#97ffff',bg='black',font=Font)
usernamelbl.place(x=3,y=150)
usernameEntry=Entry(frame,width=30,borderwidth=2)
usernameEntry.place(x=250,y=150)

Emaillbl=Label(frame,text='Email:',fg='#97ffff',bg='black',font=Font)
Emaillbl.place(x=3,y=200)
EmailEntry=Entry(frame,width=30,borderwidth=2)
EmailEntry.place(x=250,y=200)

NewPasswordlbl=Label(frame,text='NewPassword:',fg='#97ffff',bg='black',font=Font)
NewPasswordlbl.place(x=3,y=250)
NewPasswordEntry=Entry(frame,width=30,borderwidth=2)
NewPasswordEntry.place(x=250,y=250)

ConfirmPasswordlbl=Label(frame,text='ConfirmPassword:',fg='#97ffff',bg='black',font=Font)
ConfirmPasswordlbl.place(x=3,y=300)
ConfirmPasswordEntry=Entry(frame,width=30,borderwidth=2)
ConfirmPasswordEntry.place(x=250,y=300)

backbtn=Button(frame,text='<<',width=7,borderwidth=5,height=2,bg='black',fg='white',cursor='hand2',border=2,
               command=back)
backbtn.place(x=10,y=400)

submitbtn=Button(frame,text='SUBMIT',width=15,height=2,bg='#7f7fff',fg='white',cursor='hand2',border=2,
                 borderwidth=5,font=('#57a1f8',16,'bold'),command=submit)
submitbtn.place(x=130,y=350)


windows.mainloop()