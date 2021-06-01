import tkinter as tk
import pytube

def downloadvid():
    global E1
    link=E1.get()
    global D1
    destination=D1.get()
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    stream.download(destination)

root=tk.Tk()

root.geometry("500x200")
w=tk.Label(root,text="YouTube Downloader")
w.pack()

label2=tk.Label(root,text="Destination:")
label2.place(x=10,y=80)
D1=tk.Entry(root,bd=5)
D1.pack()
D1.place(x=100,y=80)

label1=tk.Label(root,text="Video URL:")
label1.place(x=10,y=40)
E1=tk.Entry(root,bd=5)
E1.pack()
E1.place(x=100,y=40)
button=tk.Button(root,text="Download", fg="purple", command=downloadvid)
button.pack()
button.place(x=250,y=160)

root.mainloop()
