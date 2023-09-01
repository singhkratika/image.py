#agian imaging
from tkinter import*
from PIL import ImageTk,Image
root=Tk()
root.geometry("300x400")
#fixing image
image=Image.open("new1.jpg")
image=image.resize((300,400),Image.LANCZOS)
img=ImageTk.PhotoImage(image)
lbl=Label(root,image=img)
lbl.pack()
root.mainloop()