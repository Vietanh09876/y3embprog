import tkinter as tk
from tkinter import ttk
from tkinter import *

GPIO21_state = False 
GPIO22_state = False

def GPIO21Button():
    print("hello")

def GPIO22Button():
    pass
        
def GPIO24Button():
    pass

#Create plain gui
gui = tk.Tk()
gui.title("Gui demo")

#Add image
image = tk.PhotoImage(file="ATU-Logo.png")

#Config window size and bg colour
tools_frame = tk.Frame(gui, width=200, height=400, bg="skyblue")
tools_frame.grid(row=0, column=0)

#Display image
tk.Label(tools_frame, bg="skyblue").grid(row=0, column=0)
thumbnail_image = image.subsample(5,5) #resize image
tk.Label(tools_frame, image=thumbnail_image).grid(row=0, column=0)

#Create tab layout
notebook = ttk.Notebook(tools_frame)
notebook.grid(row=1, column=0)

#Create tab 1
tools_tab = tk.Frame(notebook, bg="skyblue")
#Add button to tab 1
green_button = Button(tools_tab, text="Green LED", bg="lightgrey", height=10, width=60, command=GPIO21Button())
green_button.grid(row=0, column=0)
red_button = Button(tools_tab, text="Red LED", bg="lightgrey", height=10, width=60, command=GPIO22Button())
red_button.grid(row=1, column=0)

#Create tab 2
status_tab = tk.Frame(notebook, bg="skyblue")

#Add button to tab 2
distance_button = Button(status_tab, text="Read Distance", bg="lightgrey", height=10, width=60, command=GPIO21Button())
distance_button.grid(row=0, column=0)


#Display tab
notebook.add(tools_tab, text="Command")
notebook.add(status_tab, text="Status")

gui.mainloop()