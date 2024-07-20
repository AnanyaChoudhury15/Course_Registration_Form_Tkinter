from tkinter import *
from PIL import Image, ImageTk

# Function to clear the frame
def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()

# Home Page
def show_home_page():
    clear_frame()
    background_image = Image.open('homebg.png')  # Use your image file
    background_image = background_image.resize((1200, 800), Image.LANCZOS)  # Resize image to fit window
    background_photo = ImageTk.PhotoImage(background_image)
    
    background_label = Label(frame, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    heading = Label(frame, text='WELCOME TO COURSE REGISTRATION!', fg='black', font=('Helvetica', 28, 'bold'))
    heading.place(x=20, y=3)
    
    signin_button = Button(frame, text="Sign In", width=30,bg='black', fg='white', font=('Open sans', 15, 'bold'), 
                cursor='hand2',border=0, borderwidth=5, command=show_signin_page)
    signin_button.place(x=200, y=150)

    login_button = Button(frame, text="Login", width=30,bg='black', fg='white', font=('Open sans', 15, 'bold'), 
                cursor='hand2',border=0, borderwidth=5, command=show_login_page)
    login_button.place(x=200, y=240)
    background_label.image = background_photo


# Sign In Page
def show_signin_page():
    windows.destroy()
    import Registrationform

# Login Page
def show_login_page():
    windows.destroy()
    import Login_page


# Main Window
windows = Tk()
windows.title("Course Registration Form")
windows.geometry('800x450+100+50')
windows.resizable(0, 0)

frame = Frame(windows, width=1200, height=500, bg='black', bd=8)
frame.place(x=0, y=0)

# Show Home Page initially
show_home_page()

windows.mainloop()
