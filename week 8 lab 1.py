from gpiozero import LED
from gpiozero import Button
import time

red_led = LED(18)
green_led = LED(23)
button1 = Button(15,pull_up=False )


# Exercise 1
# for _ in range(40):
#     red_led.on()
#     time.sleep(0.25)
#     red_led.off()
#     time.sleep(0.25)

# Exercise 2
# while True:
#     if button1.value == 1:
#         print("GPIO 15 has detected that the button was pressed")
#         time.sleep(0.5)

# Exercise 3
while True:
    red_led.off()
    green_led.off()
    
    if button1.value == 1:
        for _ in range(5):
            red_led.toggle()
            if red_led.is_active:
                green_led.off()
            else:
                green_led.on()
            time.sleep(0.5)
            red_led.toggle()
            green_led.toggle()
            time.sleep(0.5)
            




