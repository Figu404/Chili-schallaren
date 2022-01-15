# Chili schallaren
 
## Abstract
 
This is a project for the course "Introductory project". Our project is about a plant watering system that measures the moisture in the soil of a plant and if it reaches a certain level it automatically waters the plant. It also provides a heat lamp that is fully controlled from the Lopy4 by the press of a button.
 
## Background and idea
 
We're making a product that monitors the moisture level of the soil, and pumps water to water it when required. The idea comes from the over watering of plants all over the world and forgetful students who can't remember to water their plants. We do this to make sure that the right amount of water is used for the plants so the plant does not die.
 
## Method
To keep a consistent moisture level in the soil we check the soil every other hour and water the soil if the moisture level is too low. Every time we check the soil the moisture level is tested five times with five seconds of delay in between and the median of those test values is the value that´s used, this is to get more accurate measurements. We noticed that the moisture sensor was a bit inaccurate when taking measurements in rapid succession, thus the five second delay. The median returned from the tests is both saved locally on the microcontroller and uploaded to the internet through a wifi connection. Locally, the program checks if this value is lower than 40, and then the pump is turned on for five seconds.
 
### Pycom-Device
Controlling the project we’re using a [Lopy4-Microcontroller][Lopy4] and a [Expansion board v3.1][expansion board]. To the microcontroller there are two [relays][r] and a [soil moisture sensor][sensor]. One of the relays is connected to a plant lamp and the other one to a pump. Even though the pump is driven by a 3.3v signal the data ports on the LoPy did not supply sufficient electricity to run the pump, thus a relay had to be used.  
 
### Components
This is the [sensor](https://www.electrokit.com/uploads/productfile/41015/41015738_-_Soil_Moisture_Sensor.pdf)that we used.
This is the two [relays](https://www.electrokit.com/uploads/productfile/41015/41015704_-_5V_Relay_Module.pdf) that we used. We used this 
[lamp](https://www.kjell.com/se/produkter/hem-fritid/tradgard/vaxtlampor/vaxtlampa-led-e27-1200-lm-p64560?gclid=Cj0KCQiAieWOBhCYARIsANcOw0zotIo42_MUFOpcMuNYAMZnTFBfwb3OmhILSr8SXYybIhZ_YeAcE9UaAkHfEALw_wcB&gclsrc=aw.ds)
 
### Documents
- [Timelog](../doc/timelog.md)
- [Setup](../doc/setup.md)
- [hardware](../doc/hardware.md)
- [requirements](../doc/requirements.md)
- [test](../doc/test.md)
 
 
## Results
 
![Finished project](../img/20220114_091904.jpg)
In the end we got mostly everything as we wanted, all components are used in a way that we are pretty satisfied with even though we missed a few smaller details that could have been good to have or made some minor things more clear.
 
The moisture sensor works fine but could be optimized a little bit, because the percentage is a little bit misleading if not understood correctly. It is a value between the highest and lowest values we have gotten from testing the sensor, and not the actual moisture level in the soil but it does not change that much in the code as it still is usable to automatize the watering.
 
The lamp works perfectly as a component but it is not utilized as we wanted to because it does not turn on and off automatically at specific times during the day as well as it does not turn off automatically if the water has run out. We got the lamp to work last and after that we did not have much time left to do major additions to the project because finishing touches had to be prioritized to be done in time. Everything else with the lamp is working properly and that we are happy with.
 
We have a connection to MQTT and Adafruit where we upload data and make a graph from that data which was an important part of the project. We are happy with what we have but we would have liked to expand upon it a little bit more such as to message the user as well as the data in Adafruit but it isn’t that big of a problem, as the data is always available on the same page.
 
 
 
 
[expansion board]: https://pycom.io/product/expansion-board-3-0/
[sensor]: https://www.electrokit.com/uploads/productfile/41015/41015738_-_Soil_Moisture_Sensor.pdf
[Lopy4]: https://pycom.io/product/lopy4/
[r]: https://www.electrokit.com/uploads/productfile/41015/41015704_-_5V_Relay_Module.pdf
