from gpiozero import AngularServo
from gpiozero import DistanceSensor
from gpiozero import LED
import time


servo = AngularServo(17)
sonar = DistanceSensor(4,22)
red = LED(21)
yellow = LED(20)
green = LED(16)

def checkinput():
    try:
        value = float(input("Your number:"))
        if value <= 90 and value >= -90:
            return value
        else :
            print("Not within range")
            return 
    except :
        print("Not a number")
        return

def ex1():
    servo.min()
    time.sleep(1)
    servo.mid()
    time.sleep(1)
    servo.max()
    time.sleep(1)

def ex2():
    check_value = checkinput()
    if check_value == None:
        return
    calc = check_value/90
    servo.value = calc
    return 
    
def ex3():
    print(sonar.distance)
    
    
    if sonar.distance < 0.15 or sonar.distance > 0.5: #only open when there is a car 
        if servo.value == 1 and sonar.distance > 0.5: #close the gate when no car is near
            yellow.off()
            print("Gate closing")
            red.on()
            time.sleep(0.5)
            red.off()
            green.on()
            servo.value = -1
            time.sleep(1)
            green.off()
        yellow.on()
        time.sleep(0.5) 
    else:
        if servo.value != 1:
            yellow.off()
            print("Opening gate")
            red.on()
            time.sleep(0.5)
            red.off()
            green.on()
            servo.value = 1
            time.sleep(2) #Wait for car to start moving
    red.off()
    yellow.off()
    green.off()

while True:
    # ex1()
    # ex2()
    ex3()
    