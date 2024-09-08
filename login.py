#create a login page, where the user is able to enter their username,password,and a log in button

import customtkinter 
from tkinter import *
import sqlite3
from tkinter import messagebox


#set the apperance mode to system & set the default color theme to blue

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")
#create function to login 
def login():
    username=user_entry.get()
    password=pw_entry.get() 
    print("Username:"+username)
    print("Password:"+password)
#create a window 
root = customtkinter.CTk()
root.title("Login System")
root.geometry("500x350")

#create a frame
frame=customtkinter.CTkFrame(master=root) 
frame.pack(pady=20,padx=60)

#create a label for the window 
login_label= customtkinter.CTkLabel(master=frame,text="Login System",font=("Roboto",25))
login_label.pack(pady=12,padx=10,fill="both",expand = True) 

#create a username and password entry

user_entry= customtkinter.CTkEntry(master=frame,placeholder_text="Username") 
user_entry.pack(pady=15,padx=10)

pw_entry = customtkinter.CTkEntry(master=frame,placeholder_text="Password",show="*")
pw_entry.pack(pady=15,padx=10)

#create a login button 
login_btn = customtkinter.CTkButton(master=frame,text="Login",command=login)
login_btn.pack(pady=15,padx=10)

#create a remember me checkbox
rmbr_me = customtkinter.CTkCheckBox(master=frame,text="Remember Me")
rmbr_me.pack(pady=12,padx=10)

root.mainloop() 
