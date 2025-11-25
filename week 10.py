from gpiozero import MotionSensor
import time

mtsens = MotionSensor(4)
n = 0

while True:
    mtsens.wait_for_active()
    print(f"Movement detected {n}")
    n+=1
    time.sleep(0.5)
    