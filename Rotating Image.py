from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root=Tk()
root.title("Image opener")
root.geometry("600x600")
root.configure(background="black")



img_open=""

def Open():
    global img_open
    img_open = filedialog.askopenfilename(title = "Select Image File", filetypes= [("Image Files", "*.jpg *.gif *.png *.jpeg")])
    print(img_open)
    img=ImageTk.PhotoImage(Image.open (img_open))
    


btn_open=Button(root,text="Open Image",command=Open,relief="flat",font=("Times New Roman",15),bg="#808080",fg="white")
btn_open.place(relx=0.5,rely=0.08,anchor=CENTER)


label_image=Label(root,text="By:Vihaan",bg="black",fg="white", font=("Times New Roman",15))
label_image.place(relx=0.5, rely=0.85, anchor=CENTER)

root.mainloop()