import tkinter as tk 
from tkinter import ttk

class home(tk.Tk):
    
    # init function for class home
    def __init__(self, *args, **kwargs):
        
        # init function for class TK 
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of different page layouts 
        for F in (Start, Page1, Page2, Page3, Page1_1):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively 
            # for loop 
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.show_frame(Start)

    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame starpage 
class Start(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame layout 2
        label = ttk.Label(self, text = "Image Upscaling")
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        # button for page 1
        button1 = ttk.Button(self, text = "Page 1", command = lambda: controller.show_frame(Page1))
        button1.grid(row = 1, column = 0, padx = 10, pady = 10)

        # button for page 2
        button2 = ttk.Button(self, text = "Page 2", command = lambda: controller.show_frame(Page2))
        button2.grid(row = 1, column = 1, padx = 10, pady = 10)

        # button for page 3
        button2 = ttk.Button(self, text = "Page 3", command = lambda: controller.show_frame(Page3))
        button2.grid(row = 1, column = 2, padx = 10, pady = 10)


class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def call_two():
            controller.show_frame(Page1_1)
            print("hello")


        # Upload Button
        button01 = ttk.Button(self, text = "Upload 1", command = call_two )
        button01.grid(row = 0, column = 0, padx = 10, pady = 10)

        button02 = ttk.Button(self, text = "Upload 2", command = call_two)
        button02.grid(row = 0, column = 1, padx = 10, pady = 10)

        # interpolation Buttons
        button1 = ttk.Button(self, text = "Method 1", command = lambda: controller.show_frame(Page1_1))
        button1.grid(row = 1, column = 0, padx = 10, pady = 10)

        button2 = ttk.Button(self, text = "Method 2", command = lambda: controller.show_frame(Page1_1))
        button2.grid(row = 1, column = 1, padx = 10, pady = 10)

        button3 = ttk.Button(self, text = "Method 3", command = lambda: controller.show_frame(Page1_1))
        button3.grid(row = 2, column = 0, padx = 10, pady = 10)

        button4 = ttk.Button(self, text = "Method 4", command = lambda: controller.show_frame(Page1_1))
        button4.grid(row = 2, column = 1, padx = 10, pady = 10)

        button5 = ttk.Button(self, text = "Method 5", command = lambda: controller.show_frame(Page1_1))
        button5.grid(row = 3, column = 0, padx = 10, pady = 10)

        button6 = ttk.Button(self, text = "Show all", command = lambda: controller.show_frame(Page1_1))
        button6.grid(row = 3, column = 1, padx = 10, pady = 10)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame layout 2
        label = ttk.Label(self, text = "Page 2")
        label.grid(row = 0, column = 0, padx = 10, pady = 10)

        # button for page 2
        button2 = ttk.Button(self, text = "Start", command = lambda: controller.show_frame(Start))
        button2.grid(row = 1, column = 0, padx = 10, pady = 10)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame layout 2
        label = ttk.Label(self, text = "Page 3")
        label.grid(row = 0, column = 0, padx = 10, pady = 10)

        # button for page 2
        button2 = ttk.Button(self, text = "Start", command = lambda: controller.show_frame(Start))
        button2.grid(row = 1, column = 0, padx = 10, pady = 10)  


class Page1_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame layout 2
        label = ttk.Label(self, text = "Page 1.1")
        label.grid(row = 0, column = 0, padx = 10, pady = 10)

        # button for page 2
        button2 = ttk.Button(self, text = "Start", command = lambda: controller.show_frame(Start))
        button2.grid(row = 1, column = 0, padx = 10, pady = 10) 


# Driver code
app = home()
app.mainloop()


