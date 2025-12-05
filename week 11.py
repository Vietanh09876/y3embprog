from gpiozero import DistanceSensor
from gpiozero import LED
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
import time

sonar = DistanceSensor(4,22)
red = LED(21)
yellow = LED(20)
green = LED(16)
buzzer = TonalBuzzer(17)

def flashingled():
    distance = sonar.distance
    green.off()
    yellow.off()
    red.off()
    print(distance)
    
    if distance <= 0.8 and distance >= 0.6:
        green.on()
        time.sleep(0.5)
        green.off()
        time.sleep(0.5)
    elif distance <= 0.6 and distance >=0.4:
        yellow.on()
        time.sleep(0.25)
        yellow.off()
        time.sleep(0.25)
    elif distance <= 0.4:
        red.on()
        time.sleep(0.5)
        
def flashandbuzz():
    distance = sonar.distance
    green.off()
    yellow.off()
    red.off()
    buzzer.stop()
    print(distance)
    
    if distance <= 0.8 and distance >= 0.6:
        green.on()
        buzzer.play(Tone("A4"))
        time.sleep(0.5)
        green.off()
        buzzer.stop()
        time.sleep(0.5)
    elif distance <= 0.6 and distance >=0.4:
        yellow.on()
        buzzer.play(Tone("A4"))
        time.sleep(0.25)
        yellow.off()
        buzzer.stop()
        time.sleep(0.25)
    elif distance <= 0.4:
        red.on()
        buzzer.play(Tone("A4"))
        time.sleep(0.5)

while True:
#     print(sonar.distance) #Ex 1
#     time.sleep(1)
#     flashingled() #Ex 2
#     flashandbuzz() #Ex 3
    