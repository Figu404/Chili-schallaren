from machine import Pin
import time

heatlamp = Pin("P23", mode=Pin.OUT)
button = Pin('P10', mode = Pin.IN)

def heatlamp_on(on):
    heatlamp.value(1 if on else 0)
    send("heatlamp " + ("on" if on else "off"))

def send(message):
    print("Skickar sedan ", message, " till användaren?")


while True:
    if button() == 0:
    # if button is pressed
        heatlamp_on(True)
        start = time.time()
        while True:
        #for how long does the button get pressed
            time.sleep(0.1)
            stopTime = time.time()-start
            if button() == 1:
                heatlamp_on(False)
                break
        
