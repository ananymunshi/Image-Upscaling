# import libraries
import cv2
from sewar import full_ref
from DISTS_pytorch.DISTS_pt import *
from tkinter import *  
from PIL import ImageTk, Image   
import os 



def main_function(file_name1, file_name2, no):
    global file_name_upscaled
    global file_save_name
    # Second window created 
    top = Toplevel()
    top.title("second window")
    top.configure(bg="#333333")

    # read passed images 
    img = cv2.imread(file_name1)
    ref_img = cv2.imread(file_name2)

    """
                                    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                                                    Interpolation
                                    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    """

    # Linear interpolation
    if no == 0:
        img_int = cv2.resize(img,(384,384),fx=0,fy=0, interpolation = cv2.INTER_LINEAR)
        file_save_name = 'linear_interpolation.png'
        cv2.imwrite(file_save_name, img_int)

    # Bicubic interpolation
    elif no == 1:
        img_int = cv2.resize(img,(384,384),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        file_save_name = 'bicubic_interpolation.png'
        cv2.imwrite(file_save_name, img_int) 
    
    # Lanczos Interpolation
    elif no == 2:
        img_int = cv2.resize(img,(384,384),fx=0,fy=0, interpolation = cv2.INTER_LANCZOS4)
        file_save_name = 'Lanczos.png'
        cv2.imwrite(file_save_name, img_int)
    
    # Nearest Neighbor Interpolation 
    elif no == 3:
        img_int = cv2.resize(img,(384,384),fx=0,fy=0, interpolation = cv2.INTER_NEAREST)
        file_save_name = 'Nearest.png'
        cv2.imwrite(file_save_name, img_int) 
    
    # Pixel area Resampling
    elif no == 4:
        img_int = cv2.resize(img,(384,384),fx=0,fy=0, interpolation = cv2.INTER_AREA)
        file_save_name = 'pixel.png'
        cv2.imwrite(file_save_name, img_int)

    elif no == 5:
        pass
    
    else:
        pass


    """
                                    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                                                 Designing TKINTER GUI
                                    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    """

    # display labels 
    label_HR = Label(top, text="HR Image", bg="#333333", fg="#fff")
    label_HR.grid(row=0, column=2)
    label_LR = Label(top, text="LR Image", bg="#333333", fg="#fff")
    label_LR.grid(row=0, column=0)
    label_Upscaled = Label(top, text="Upscaled Image", bg="#333333", fg="#fff")
    label_Upscaled.grid(row=0, column=1)

    # display the image

    # display HR image
    disp_HR = ImageTk.PhotoImage(Image.open(file_name2))  
    label_HR_img = Label(top, image = disp_HR, bg="#333333", fg="#fff")
    label_HR_img.grid(row=1, column=2)

    # display LR image
    disp_LR = ImageTk.PhotoImage(Image.open(file_name1))  
    label_LR_img = Label(top, image = disp_LR, bg="#333333", fg="#fff")
    label_LR_img.grid(row=1, column=0)

    # display upscaled image
    file_name_upscaled = os.path.abspath(file_save_name)
    disp = ImageTk.PhotoImage(Image.open(file_name_upscaled))
    label_1 = Label(top, image=disp, bg="#333333", fg="#fff")
    label_1.grid(row=1, column=1)

    # calculate the MS-SSIM and DISTS
    msssim_img= full_ref.msssim(ref_img, img_int, weights=[0.0448, 0.2856, 0.3001, 0.2363, 0.1333], ws=11, K1=0.01, K2=0.03, MAX=None)
    dists_img = arguments(file_name2, file_name_upscaled)

    
    # display the calculated error
    label_msssim = Label(top, text = "MS-SSIM: "+str(msssim_img.real), bg="#333333", fg="#fff")
    label_msssim.grid(row=2, column=0, columnspan=2)
    print(msssim_img.real)

    label_dists = Label(top, text = "DISTS: "+str(dists_img), bg="#333333", fg="#fff")
    label_dists.grid(row=2, column=2)
    print(dists_img)

    label_msssim.config(font=("Courier", 18))
    label_dists.config(font=("Courier", 18))

    # end of program
    mainloop()


   
    
    
