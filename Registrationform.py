from tkinter import *
import pycountry
from tkinter import messagebox
import pymysql

#windows size
windows=Tk()
windows.title("Personal Registration form")
windows.geometry('540x640+200+10')
windows.resizable(0,0)           #This is used to disable the maximize button so cannot change window size.


def back():
    windows.destroy()
    import HomePage


#database section
def submit():
    if firstnameEntry.get()=='':
        messagebox.showerror("ALERT!","Please enter your first name.")
    elif lastnameEntry.get()=='':
        messagebox.showerror("ALERT!","Please enter your last name.")
    elif emailEntry.get()=='':
        messagebox.showerror("ALERT!","Please enter your email.")
    elif gender.get()=='':
        messagebox.showerror("ALERT!","Please enter your gender.")
    elif OM.get()=='':
        messagebox.showerror("ALERT!","Please enter your country.")
    elif usernameEntry.get()=='':
        messagebox.showerror("ALERT!","Please enter your user name.")
    elif passwordEntry.get()=='':
        messagebox.showerror("ALERT!","Please enter your password.")
    elif confirmpasswordEntry.get()=='':
        messagebox.showerror("ALERT!","Please confirm your password.")
    elif passwordEntry.get()!=confirmpasswordEntry.get():
        messagebox.showerror("Alert!",'Passwords do not match.')
    else:
        db=pymysql.connect(host='localhost',user='root',password='An@150604',database='Personal_Registration_form')
        cur=db.cursor()

        try:
            query='create database Personal_Registration_form'
            cur.execute(query)
            query='use Personal_Registration_form'
            cur.execute(query)
            #messagebox.showinfo('success','successful connection')
            #print('worked')
        
            query='create table P_details(id int auto_increment primary key not null, firstname varchar(40), lastname varchar(40), \
                email varchar(40),gender varchar(10),country varchar(40), username varchar(40),password varchar(40),confirmpassword varchar(40))'
            cur.execute(query)
            messagebox.showinfo('success','fields created successfully')

        except:
            cur.execute('use Personal_Registration_form')
            query='insert into P_details(firstname, lastname, email, gender, country, username, password,\
                  confirmpassword) values(%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(query,(firstnameEntry.get(), lastnameEntry.get(), emailEntry.get(), gender.get(), OM.get(),
                               usernameEntry.get(), passwordEntry.get(), confirmpasswordEntry.get()))
            
            db.commit()
            db.close()
            messagebox.showinfo('Success','Successful Registration!!')

            firstnameEntry.delete(0,END)
            lastnameEntry.delete(0,END)
            emailEntry.delete(0,END)
            gender.set(0)
            OM.set('Select country')
            usernameEntry.delete(0,END)
            passwordEntry.delete(0,END)
            confirmpasswordEntry.delete(0,END)



#to show or hide the password entry
def show1():
    passwordEntry.configure(show='#')
    check1.configure(command=hide1)
def hide1():
    passwordEntry.configure(show='')
    check1.configure(command=show1)

def show2():
    confirmpasswordEntry.configure(show='#')
    check2.configure(command=hide2)
def hide2():
    confirmpasswordEntry.configure(show='')
    check2.configure(command=show2)

#section for getting data from entry fields
firstname=StringVar()
lastname=StringVar()
email=StringVar()
gender=StringVar()
OM=StringVar()
username=StringVar()
password=StringVar()
confirmpassword=StringVar()
#frame
frame=Frame(windows, width=610, height=640, bg='black', bd=8)
frame.place(x=0, y=0)

#used to insert country names into the list imported from package pycountry.
countries = [country.name for country in pycountry.countries]
OM.set("Select Country")

#label and entry fields
heading=Label(frame, text= 'Personal Registration form',fg='#97ffff', bg='black',font=('Calibre',20,'bold'))
heading.place(x=90, y=3)

usernameImage = PhotoImage(file='usernamelogo.png')
usernameLabel = Label(frame, image=usernameImage)
usernameLabel.place(x=45, y=3)

firstNamelbl=Label(frame, text='First Name:',fg='#97ffff',bg='black',font=('Calibre', 15, 'bold'))
firstNamelbl.place(x=10, y=70)

firstnameEntry=Entry(frame, width=30, borderwidth=2)
firstnameEntry.place(x=240, y=70)

lastNamelbl=Label(frame, text='Last Name:',fg='#97ffff',bg='black',font=('Calibre', 15, 'bold'))
lastNamelbl.place(x=10, y=110)

lastnameEntry=Entry(frame, width=30, borderwidth=2)
lastnameEntry.place(x=240, y=110)

emaillbl=Label(frame, text='Email:',fg='#97ffff',bg='black',font=('Calibre', 15, 'bold'))
emaillbl.place(x=10, y=150)

emailEntry=Entry(frame, width=30, borderwidth=2)
emailEntry.place(x=240, y=150)

genderlbl=Label(frame, text='Select Gender:',fg='#97ffff',bg='black',font=('Calibre', 15, 'bold'))
genderlbl.place(x=10, y=200)

gender.set(0)
genderRadio1=Radiobutton(frame, text='Male' ,variable=gender, value='Male', font='Tahoma 13 bold')
genderRadio1.place(x=240, y=200)

genderRadio2=Radiobutton(frame, text='Female' ,variable=gender, value='Female', font='Tahoma 13 bold')
genderRadio2.place(x=350, y=200)

countrylabelDropdown=Label(frame, text='Select Country:',fg='#97ffff',bg='black',font=('Calibre', 15, 'bold'))
countrylabelDropdown.place(x=10, y=250)

countrylabelDropdown = OptionMenu(frame, OM, *countries)
countrylabelDropdown.place(x=240, y=250)
countrylabelDropdown.config(width=18, font=('Calibre', 13, 'bold'), fg='black')

usernamelbl=Label(frame, text='UserName:',fg='#97ffff',bg='black',font=('Calibre', 15, 'bold'))
usernamelbl.place(x=10, y=300)

usernameEntry=Entry(frame, width=30, borderwidth=2)
usernameEntry.place(x=240, y=300)

passwordlbl=Label(frame, text='Password:',fg='#97ffff',bg='black',font=('Calibre', 15, 'bold'))
passwordlbl.place(x=10, y=350)

passwordEntry=Entry(frame, width=30, borderwidth=2)
passwordEntry.place(x=240, y=350)

confirmpasswordlbl=Label(frame, text='Confirm Password:',fg='#97ffff',bg='black',font=('Calibre', 15, 'bold'))
confirmpasswordlbl.place(x=10, y=400)

confirmpasswordEntry=Entry(frame, width=30, borderwidth=2)
confirmpasswordEntry.place(x=240, y=400)

submitbtn = Button(frame, text='SUBMIT', width=15, borderwidth=5, height=2, bg='#7f7fff',fg='white', cursor='hand2',
                   border=2, font=('#57a1f8', 16, 'bold'),command=submit)
submitbtn.place(x=150, y=480)

backbtn= Button(frame, text='Back', width=10, border=2, height=2, cursor='hand2',bg='black', fg='white', command=back)
backbtn.place(x=0, y=580)

#checkbuttons
check1 = Checkbutton(frame, text='Hide/Show', bg= 'black',fg='#7f7fff',command=show1)
check1.place(x=420, y=350)

check2 = Checkbutton(frame, text='Hide/Show', bg= 'black',fg='#7f7fff',command=show2)
check2.place(x=420, y=400)



windows.mainloop()