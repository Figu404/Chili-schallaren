# Here every import is being imported
from machine import Pin
import machine
import time
from lib.internet import Internet
from lib.memory import Memory
import pycom

# Here every pin is set
adc = machine.ADC() 
heatlamp = Pin("P23", mode=Pin.OUT)
pump  = Pin("P22", mode=Pin.OUT)
power = Pin("P21", mode=Pin.OUT)
humidity = adc.channel( attn = adc.ATTN_11DB ,pin='P16')
button = Pin('P10', mode = Pin.IN)
pycom.heartbeat(False)
cycle = True
settings_menu = True
t = time.time()
m = Memory()
memory = m.local_memory

# A function for the controlling the hearlamp. Set on to True for on and set on to false for off
def heatlamp_on(on):
    heatlamp.value(1 if on else 0)
    send("heatlamp " + ("on" if on else "off"))


# A function to check the humidty in the soil
def humidity_sensor():
    def calculate_humidty():
        # An algorithm to get a percentage on the humidity instead of the value given by the sensor
        # The algorithm is gotten from the test values from the different situations (in air/dry soil/wet soil)
        percent_humidity = (1 - ((humidity()) / 4000)) * 100
        return percent_humidity
    power.value(1)
    time.sleep(2)

    sum = 0
    num = 5
    for i in range(num):
        sum += calculate_humidty()
    humidity_value= (sum/num)
    print(humidity_value)
    #send(humidity)
    time.sleep(2)
    power.value(0)
    time.sleep(2)
    return humidity_value


# A function for controlling the pump
def water_pump():
    pump.value(1)
    time.sleep(10)
    pump.value(0)
    
# A function for sending a message
def send(message, internet_name=None, internet_password=None):
    web = Internet(internet_name = internet_name, internet_password=internet_password)
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


def button_event_callback(argument):
    global t
    global cycle
    global settings_menu
    if time.time()*1000 - t >= 1000:
        if settings_menu:
            settings_menu = False
        if cycle:
            heatlamp_on(False)
            cycle = False
        else:
            heatlamp_on(True)
            cycle = True
        
        t = time.time()*1000


def menu(choices, choice):
    global settings_menu
    if not settings_menu:
        return -1
    i = 0
    print("\n" * 12)
    for e in choices:
        i += 1
        if i == choice:
            print("--->", end="")
        print(e)
    
    key = input()
    if key == "d":
        if len(choices) <= choice:
            return menu(choices, choice)
        else:
            return menu(choices, choice+1)
    if key == "u":
        if 1 >= choice:
            return menu(choices, choice)
        else:
            return menu(choices, choice-1)
    if key == "":
        return choice
    if key == "stop":
        return None

    else:
        return menu(choices, choice)

def main_menu():
    global memory
    if settings_menu:
        choice = menu({"Instructions", "Settings", "Check Data"}, 1)
        if choice == 1:
            print("\n" * 12)
            print("Instruktions: ")
            print("To do stuff you do stuff")
            input()
            main_menu()
        if choice == 2:
            choice = menu({"Pump on seconds"}, 1)
            if choice == 1:
                while True:
                    try:
                        inp = input()
                        inp.type()
                        number = int(input())
                        if abs(number) - number == 0:
                            memory["Pump duration"] = number
                            break
                        print("Please write a positive integer")
                    except OSError as er:
                        print("Error:" + str(er))
                        print("Please write a positive integer")
            main_menu()

        if choice == 3:
            print(memory)
            main_menu()
        

            
        

def main():
    global memory
    global m
    main_menu()
    m.save()

    realtime = 0
    time_elapsed = time.time()
    i = Internet(internet_name="NETGEAR39", internet_password="smoothrabbit467")
    while True:
        if cycle:
            if realtime == 19:
                heatlamp_on(True)
            if realtime == 10:
                heatlamp_on(False)
        if time_elapsed - time.time() > 10800:
            print("measure humidity")
            data = humidity_sensor()
            memory[time.time()] = data
            m.save()
            if data > 0.55:
                water_pump()
            i.communicate(str(data))




# connect button to callback event function.

button.callback(Pin.IRQ_FALLING, button_event_callback)


# Here we run the code
print("fdsa")
main()
