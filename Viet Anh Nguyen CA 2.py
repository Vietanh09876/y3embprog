from gpiozero import AngularServo
from gpiozero import DistanceSensor
from gpiozero import LED
import time

servo = AngularServo(17)
sonar = DistanceSensor(4,22)
green = LED(16)
yellow = LED(20)
red = LED(21)

def checkdistance():
    print(sonar.distance)
    if sonar.distance > 0.6:
        green.off()
        yellow.off()
        red.on()
        servo.value = -1
        time.sleep(0.5)

    else :
        #Opening
        green.on()
        yellow.off()
        red.off()
        servo.value = 1
        time.sleep(0.5) 
        
        green.off()
        yellow.on()
        red.off()
        time.sleep(5)
        
        #Closing
        green.on()
        yellow.off()
        red.off()
        servo.value = -1
        time.sleep(0.5)
        
        green.off()
        yellow.off()
        red.on()

while True:
    checkdistance()
    