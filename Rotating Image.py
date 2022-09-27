from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root=Tk()
root.title("Image opener")
root.geometry("600x600")
root.configure(background="black")



img_path=""
def Open():
    global img_path
    img_path=filedialog.askopenfilename(title = "Select Image File", filetypes= [("Image Files", "*.jpg *.gif *.png *.jpeg")])
    print(img_path)
    img=ImageTk.PhotoImage(Image.open(img_path))
    label_image["image"] = img
    img.close()
    
def rotate():
    print("Rotate")
    print(img_path)
    im=Image.open(img_path)
    rotated_img=im.rotate(180)
    img=ImageTk.PhotoImage(rotated_img)
    label_image.configure(image=img)
    img.close()
    


btn_open=Button(root,text="Open Image",command=Open,relief="flat",font=("Times New Roman",15),bg="#808080",fg="white")
btn_open.place(relx=0.5,rely=0.08,anchor=CENTER)

btn_rotate=Button(root,text="Rotate Image",command=rotate,relief="flat",font=("Times New Roman",15),bg="#808080",fg="white")
btn_rotate.place(relx=0.5,rely=0.75,anchor=CENTER)

label_image=Label(root, bg = "gold2", highlightthickness=5)
label_image.place(relx=0.5, rely=0.5, anchor=CENTER)

label_footer=Label(root,text="By:Vihaan",bg="black",fg="white", font=("Times New Roman",15))
label_footer.place(relx=0.5, rely=0.85, anchor=CENTER)

root.mainloop()