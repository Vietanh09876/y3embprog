import tkinter as tk
from tkinter import ttk
from tkinter import *
from gpiozero import LED
from gpiozero import DistanceSensor

green_LED = LED(27)
red_LED = LED(17)
sonar_sensor = DistanceSensor(4,22)
GPIO21_state = False 
GPIO22_state = False


def GPIO21Button():
    global GPIO21_state
    if GPIO21_state == True:
        GPIO21_state = False
        green_button.config(bg="green")
        green_LED.on()
    else:
        GPIO21_state = True
        green_button.config(bg="lightgrey")
        green_LED.off()

def GPIO22Button():
    global GPIO22_state
    if GPIO22_state == True:
        GPIO22_state = False
        red_button.config(bg="red")
        red_LED.on()
    else:
        GPIO22_state = True
        red_button.config(bg="lightgrey")
        red_LED.off()
        
def GPIO24Button():
    global sonar_sensor
    #Delete textbox content
    text_box.delete("1.0", END)
    #Display data in textbox
    text_box.insert(END, sonar_sensor.distance)

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
green_button = Button(tools_tab, text="Green LED", bg="lightgrey", height=10, width=60, command=GPIO21Button)
green_button.grid(row=0, column=0)
red_button = Button(tools_tab, text="Red LED", bg="lightgrey", height=10, width=60, command=GPIO22Button)
red_button.grid(row=1, column=0)

#Create tab 2
status_tab = tk.Frame(notebook, bg="skyblue")

#Add button to tab 2
distance_button = Button(status_tab, text="Read Distance", bg="lightgrey", height=10, width=60, command=GPIO24Button)
distance_button.grid(row=0, column=0)
text_box = Text(status_tab, height=10, width=50)
text_box.grid(row=1, column=0,padx=3,pady=3)



#Display tab
notebook.add(tools_tab, text="Command")
notebook.add(status_tab, text="Status")

gui.mainloop()