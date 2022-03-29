from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox
root=Tk()
root.title("Credit Card Authentication")
root.geometry("600x400")
root.configure(background="yellow")

input_box=Entry(root)
input_box.place(relx=0.5,rely=0.3,anchor=CENTER)
card=ImageTk.PhotoImage(Image.open("credit card.png")) 
image=Label(root,image=card)
image.place(relx=0.5,rely=0.6,anchor=CENTER)
def authentication():

    try:
        get_input = int(input_box.get ())
        messagebox.showinfo("Success","Credit Card Value Accepted")
    except(ValueError):
        messagebox.showinfo("Error", "Add Valid details")
    

button=Button(root,text="Check Credit Card",command=authentication)
button.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()