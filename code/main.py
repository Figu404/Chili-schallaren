from machine import Pin
import time

Heatlamp = Pin("P8", mode=Pin.OUT)

for i in range(10):
    Heatlamp.value(1)
    time.sleep(2)
    Heatlamp.value(0)
    time.sleep(2)