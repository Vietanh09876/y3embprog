from gpiozero import LED
from gpiozero import MotionSensor
import time

mtsens = MotionSensor(4)
red = LED(18)
yellow = LED(15)
green = LED(14)
n = 0

#Exercise 1
# while True:
#     mtsens.wait_for_active()
#     print(f"Movement detected {n}")
#     time.sleep(1)

#Exercise 2
# while True:
#     green.off()
#     red.off()
#     yellow.off()
#     
#     green.on()
#     time.sleep(10)
#     green.off()
#     yellow.on()
#     time.sleep(5)
#     yellow.off()
#     red.on()
#     time.sleep(10)
#     red.off()
#     for _ in range(20):
#         yellow.toggle()
#         time.sleep(0.25)
#         yellow.toggle()
#         time.sleep(0.25)

#Exercise 3
while True:
    green.on()
    red.off()
    yellow.off()
    mtsens.wait_for_active()
    n += 1
    print(f"Movement detected {n}")
    
    green.off()
    yellow.on()
    time.sleep(5)
    yellow.off()
    red.on()
    time.sleep(10)
    red.off()
    for _ in range(20):
        yellow.toggle()
        time.sleep(0.25)
        yellow.toggle()
        time.sleep(0.25)

