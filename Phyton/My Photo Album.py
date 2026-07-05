from tkinter import *   
from tkinter import messaggebox
from tkinter import messagebox
from PIL import Image, ImageTk
window = Tk()
window.title("My Photo Album")
window.geometry("400x420")
title = Label(window, text="My Photo Album", fg="white", bg="purple", width=40)
title.pack(pady=10)     
img_file = Image.open("myname.PNG")
img_file = img_file.resize((300, 180))
photo = ImageTk.PhotoImage(img_file)
pic = Label(window, image=photo)    
pic.pack(pady=5)
def show_message():
    messagebox.showinfo("Great", "You Clicked The Photo!")
msg_btn = Button(window, text="Click To React !", bg = "blue" , fg = "white", command=show_message)
msg_btn.pack(pady=5)
def show_details():
 top = Toplevel()
 top.title("Photo Details")
 top.geometry("200x120")
 info = Label(top , text = "Taken on : 1st June 2025")
 info.pack(pady=10)
 Place = Label(top, text="Location: My Garden")
 Place.pack()
 top.mainloop()
details_btn = Button(window, text="See Details", bg = "green" , fg = "white" , command=show_details )
details_btn.pack(pady=5)    
window.mainloop()  









