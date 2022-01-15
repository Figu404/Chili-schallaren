### Tests
## Pump
To test the pump two containers were placed beside each other, one full of water the other one empty. The pump placed in the container filled with water with a tube was connected from the pump leading to the empty container. The pump was turned on for 60 seconds and the volume of water that had been moved was measured.

##### First test
The pump is connected to port 23 on the expansionbord.
Result:
Failed. The pump is not provided with a sufficient current to move any water through the entirety of the tube.

##### Second test
The pump is connected to a Low Dropout Voltage Regulator with is controlled by the LoPy.
###### Result:
Failed. The pump is not provided with sufficient current to move enough water, only 50 ml.

##### Third test:
The pump is connected to the 3v3 port on the expationbord with a relay to break and connect the current.
###### Result: 
Success. The pump moved 625 ml which equates to 10.4 ml/s.

## Soil moisture sensor

##### First test
The sensor was first placed in moist soil and tested then moved to dry soil and tested again.
###### Result: 
Success. The sensor returned a value of 1300 when placed in the moist soil and a value of 4095 when placed in the dry soil. 
This was the expected result. In the dry soil the sensor gave the maximum output value which is reasonably considering the condition of the soil. 

##### Second test
The sensor was placed in the soil of a plant, the moisture was tested, then the plant was watered and then the soil was tested again.
###### Result:
Success. The first test of the soil yielded a value of 1600 and the second test, after the plant had been watered, the sencor returned a value of 1400.

## Lamp
The lamp was connected to a 230v outlet with a relay controlled by the microcontroller connecting and disconnecting the circuit. The relay was engaged and disengaged to see if the lamp was turned on and off.
###### Result:
Success.

## The watering system
All components were connected, the network information was inputted, the moisture sensor was placed in the soil of a plant and the pump placed in water with a tube ringing to the plant.
##### First test
This test is run with a much lower cycling time of two seconds to see if the pump was turned on when the sensor is manipulated to give a low enough value.
###### Result:
Success. The pump was turned on as intended and the moisture level was uploaded to adafruit. 

Discovery: The sensor gave varying results even though the sensor was not manipulated.

Fix: Testing the soil five times with a five second delay in between and taking the median out of those tests.

##### Second test
This test was run for an entire day at the intended cycling time of two hours.
###### Result:
Success. The system worked as intended.
