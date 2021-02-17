# Imports
from tkinter import *
from tkinter.filedialog import askopenfilename
from functions import *
from functools import partial


# Root window
root = Tk()
root.title("Image Upscaling")
root.configure(bg="#333333")


# Function to Upload Image
def fileopener_img():
    global file_name1
    file_name1 = askopenfilename(initialdir=r"D:\image_upscaling\Data\LR",  filetypes=(("png files", "*.png"),("all files", "*.*")))
    if not file_name1:
        return None

# Function to upload reference image
def fileopener_ref():
    global file_name2
    file_name2 = askopenfilename(initialdir=r"D:\image_upscaling\Data\HR",  filetypes=(("png files", "*.png"),("all files", "*.*")))
    if not file_name2:
        return None
        
# Button Image
ButtonImg1 = PhotoImage(file='Images/Upload.png')
ButtonImg2 = PhotoImage(file='Images/Linear.png')
ButtonImg3 = PhotoImage(file='Images/bicubic.png')
ButtonImg4 = PhotoImage(file='Images/Lanczos.png')
ButtonImg5 = PhotoImage(file='Images/Nearest.png')
ButtonImg6 = PhotoImage(file='Images/pixel.png')
ButtonImg7 = PhotoImage(file='Images/ShowAll.png')

# Image Upload function
Button01 = Button(root, image=ButtonImg1, borderwidth=0, bg="#333333", command=fileopener_img)
Button01.grid(row=0, column=0, padx=10, pady=10)

Button02 = Button(root, image=ButtonImg1, borderwidth=0, bg="#333333", command=fileopener_ref)
Button02.grid(row=0, column=1, padx=10, pady=10)

# bicubic interpolation method 
Button2 = Button(root, image=ButtonImg2, bg="#333333", borderwidth=0, command=lambda: main_function(file_name1, file_name2, 0))
Button2.grid(row=1, column=0, padx=5, pady=10)

Button3 = Button(root, image=ButtonImg3, bg="#333333", borderwidth=0, command=lambda: main_function(file_name1, file_name2, 1))
Button3.grid(row=1, column=1, padx=5, pady=10)

Button4 = Button(root, image=ButtonImg4, bg="#333333", borderwidth=0, command=lambda: main_function(file_name1, file_name2, 2))
Button4.grid(row=2, column=0, padx=5, pady=10)

Button5 = Button(root, image=ButtonImg5, bg="#333333", borderwidth=0, command=lambda: main_function(file_name1, file_name2, 3))
Button5.grid(row=2, column=1, padx=5, pady=10)

Button6 = Button(root, image=ButtonImg6, bg="#333333", borderwidth=0, command=lambda: main_function(file_name1, file_name2, 4))
Button6.grid(row=3, column=0, padx=5, pady=10)

# Button That executes all functions
Button7 = Button(root, image=ButtonImg7, bg="#333333", borderwidth=0)
Button7.grid(row=3, column=1, padx=5, pady=10)

# Event Loop
root.mainloop()