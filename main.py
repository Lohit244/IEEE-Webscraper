import os
from tkinter import *
from PIL import ImageTk
from PIL import ImageTk, Image

root = Tk()
root.title("Job Search")
root.configure(background='#101E3F')

# Funtions
def job():
    os.system('python GUI_JobSearch.py')
def google():
    os.system('python GUI_google.py')

# Images

image2 = Image.open('./google.png')
app_logo2 = ImageTk.PhotoImage(image2)
app_logo2_label = Label(root, image=app_logo2,borderwidth=0,height=350)
app_logo2_label.configure(background="#101E3F")
app_logo2_label.grid(row=0,column=0)
image = Image.open('./logo.png')
image = image.resize((350, 350), Image.ANTIALIAS)
app_logo = ImageTk.PhotoImage(image)
app_logo_label = Label(root, image=app_logo,borderwidth=0)
app_logo_label.grid(row=0, column=1)



# Buttons
btn = Button(root,text="Google Search",command=google)
btn.grid(row =1 , column=0,rowspan=1)
btn = Button(root,text="Job Search",command=job)
btn.grid(row =1 , column=1,rowspan=1)
# Start mainloop
root.mainloop()