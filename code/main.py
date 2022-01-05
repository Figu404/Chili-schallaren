# Here every import is being imported
from json import load
from machine import Pin
import machine
import time
from lib.internet import Internet
from lib.memory import Memory

# Here every pin is set
heatlamp = Pin("P23", mode=Pin.OUT)
pump  = Pin("P22", mode=Pin.OUT)
power = Pin("P21", mode=Pin.OUT)
humidity = Pin("P20", mode=Pin.IN)
button = Pin('P10', mode = Pin.IN)

# Created for the humidity sensor
adc = machine.ADC()             # create an ADC object
apin = adc.channel( attn = adc.ATTN_11DB ,pin='P16')  # create an analog pin on P16


# A function for the controlling the hearlamp. Set on to True for on and set on to false for off
def heatlamp_on(on):
    heatlamp.value(1 if on else 0)
    send("heatlamp " + ("on" if on else "off"))


# A function to check the humidty in the soil
def humidity_sensor():
    for i in range(10):
        def calculate_humidty():
            return apin().voltage()/3
        power.value(1)
        time.sleep(2)
        humidity = calculate_humidty()
        print(humidity)
        #send(humidity)
        time.sleep(2)
        power.value(0)


# A function for controlling the pump
def water_pump():
    pump.value(1)
    time.sleep(2)
    pump.value(0)
    
# A function for sending a message
def send(message):
    web = Internet()
    web.comunicate(message = message)
    print("Skickar sedan ", message, " till användaren?")

# A function to check if a message was sent......this does not work beacues the
# connection is new every time you start it so it does not read new messages.
# Do we even need to have a check message?
def check():
    web = Internet()
    return web.comunicate()

# This is a function for testing the program
def test():
    print("Running test:")
    m = Memory()
    localMemory = m.local_memory
    localMemory[8] = "df"
    print(localMemory[8])
    m.save()

    m2 = Memory()
    print(m2.local_memory[8])


    
    print("Test run done.")

# Here we run the code
humidity_sensor()

