import machine
import time
realtime = machine.RTC()



print(realtime.now())
time.sleep(2)
print(realtime.now())