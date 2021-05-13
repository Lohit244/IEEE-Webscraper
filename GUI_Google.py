from tkinter import *
from PIL import ImageTk
import PIL.Image
import google as google
import webbrowser

curcolor = ''
fgcol = ''
with open("config.txt",'r',encoding='utf-8') as f:
    curcolor = f.read()
    if curcolor == 'white':
        fgcol = 'black'
    else:
        fgcol = 'white'

def changeMode():
    if curcolor == 'white':
        curcolorNew = '#353535'
    else:
        curcolorNew = 'white'
    with open("config.txt",'w',encoding='utf-8') as f:
        f.write(curcolorNew)

root = Tk()
root.title("Google Search")
root.configure(background=curcolor)


def open_url(link):
    webbrowser.open(link,new=1)

def handle_frame_close():
    container_frame.pack_forget()
    create_container_frame()

def create_container_frame():
    global container_frame
    container_frame = LabelFrame(root, padx=10, pady = 10)
    container_frame.configure(background=curcolor)
    container_frame.pack()
    closeButton = Button(container_frame,text="Close All Results",font=('Segoe UI', 10, 'normal'), width=20, padx=40, command=handle_frame_close)
    closeButton.pack()

def googleClick():
    frame = LabelFrame(container_frame, padx=10, pady = 10)
    frame.configure(background=curcolor)
    frame.pack()
    term = search_bar.get()
    everyting = google.search(term)
    heading = Label(frame, text = everyting[0][0],font=('Segoe UI', 15, 'bold'),fg=fgcol)
    link =    everyting[0][1]
    desc =    Label(frame, text = everyting[0][2], font=('Segoe UI', 15, 'normal'),fg=fgcol)
    desc.config(wraplength=700)
    heading.configure(background=curcolor)
    desc.configure(background=curcolor)
    heading.pack()
    desc.pack()
    open_button = Button(frame,text ="Visit",font=('Segoe UI', 10, 'normal'), width=20, padx=40, command=lambda: open_url(link))
    open_button.pack()


# Mode Switcher
ModeButton = Button(root, text = "Switch Mode(Requires Manual Restart)",font=('Segoe UI', 10, 'normal'), command=changeMode, width=20, padx=40,bg="#F8F9FA")
ModeButton.pack(pady=50)

# App Logo ->

google_logo = ImageTk.PhotoImage(PIL.Image.open('./google.png'))
google_label = Label(root, image=google_logo)
google_label.pack(pady=100,padx=200)
google_label.configure(background=curcolor)

# Search Bar ->

search_bar = Entry(root, width=50,font=('Segoe UI', 15, 'normal'), borderwidth=3)
search_bar.pack(pady=30)

# Search Button ->

GoogleButton = Button(root, text = "Search",font=('Segoe UI', 10, 'normal'), command=googleClick, width=20, padx=40,bg="#F8F9FA")
GoogleButton.pack(pady=50)

# Results Container -->

global container_frame
container_frame = LabelFrame(root, padx=10, pady = 10)
container_frame.configure(background=curcolor)
container_frame.pack()

#Clear All Button 

closeButton = Button(container_frame,text="Close All Results",font=('Segoe UI', 10, 'normal'), width=20, padx=40, command=handle_frame_close)
closeButton.pack()



root.mainloop()