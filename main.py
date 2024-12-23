from tkinter import *
from PIL import Image,ImageTk

root=Tk()

root.title("Immortal Jellfish (know as the Turritopsis dohrnii)")
root.geometry("500x500")

upload=Image.open("Immortal Jellfish.png")

image=ImageTk.PhotoImage(upload)

label=Label(root,image=image,height=350,width=500)
label.place(x=50,y=50)

label=Label(root,text="The medusa of Turritopsis dohrnii is the only form known to have the ability to return to a polyp state, by a specific transformation process that requires the presence of certain cell types (tissue from both the jellyfish bell surface and the circulatory canal system).")
label.place(x=50,y=390)

root.mainloop()