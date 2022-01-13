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
m = Memory()
memory = m.local_memory
t= time.time()

# A function for the controlling the hearlamp. Set on to True for on and set on to false for off
def heatlamp_on(on):
    heatlamp.value(1 if on else 0)
    


# A function to check the humidty in the soil
def humidity_sensor():
    def calculate_humidty():
        # An algorithm to get a percentage on the humidity instead of the value given by the sensor
        # The algorithm is gotten from the test values from the different situations (in air/dry soil/wet soil)
        percent_humidity = round((1 - ((humidity()) / 4095)) * 100)
        return percent_humidity
    power.value(1)
    time.sleep(2)

    lst_sum = []
    num = 5
    for i in range(num):
        time.sleep(5)
        lst_sum.append(calculate_humidty())
    humidity_value= sorted(lst_sum)[2]
    print(humidity_value)
    #send(humidity)
    power.value(0)
    time.sleep(2)
    return humidity_value


# A function for controlling the pump
def water_pump():
    pump.value(1)
    time.sleep(5)
    pump.value(0)
    
# A function for sending a message
# def send(message, internet_name=None, internet_password=None):
#     web = Internet(internet_name = internet_name, internet_password=internet_password)
#     web.comunicate(message = message)
#     print("Skickar sedan ", message, " till användaren?")

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
        if cycle:
            heatlamp_on(False)
            cycle = False
        else:
            heatlamp_on(True)
            cycle = True
        
        t = time.time()*1000


def main():
    global memory
    global m

    realtime = 0
    time_elapsed = time.time()
    i = Internet(internet_name="NETGEAR39", internet_password="smoothrabbit467")
    while True:
        if cycle:
            if realtime == 19:
                heatlamp_on(True)
            if realtime == 10:
                heatlamp_on(False)
        if time.time() - time_elapsed > 7200:
            time_elapsed = time.time()
            print("measure humidity")
            data = humidity_sensor()
            memory[time.time()] = data
            m.save()
            if data < 40:
                water_pump()
            i.communicate(str(data))


# connect button to callback event function.

button.callback(Pin.IRQ_FALLING, button_event_callback)


# Here we run the code
main()
