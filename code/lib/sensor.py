
# Code in c++? for this specific sensor

# int sensorPin = A5; // select the input pin for the potentiometer
# int sensorValue = 0; // variable to store the value coming from the sensor
# int sensorVCC = 13;
# void setup()
# {
#  Serial.begin(9600);
#  pinMode(sensorVCC, OUTPUT); // declare the ledPin as an OUTPUT:
#  digitalWrite(sensorVCC, LOW);
# }
# void loop()
# {
#  digitalWrite(sensorVCC, HIGH); // power the sensor
#  delay(100); //make sure the sensor is powered
#  sensorValue = analogRead(sensorPin); // read the value from the sensor:
#  digitalWrite(sensorVCC, LOW); //stop power
#  delay(60*1000); //wait
#  Serial.print("sensor = " );
#  Serial.println(sensorValue);


# Code from lab 2 with analog digital sensor

# Read an analog input
# https://docs.pycom.io/firmwareapi/pycom/machine/adc/

import machine
import time
from math import log

adc = machine.ADC()             # create an ADC object
apin = adc.channel(pin='P16', attn=adc.ATTN_11DB)   # create an analog pin: P16

# Valid pins are P13 to P20.


def ThermistorNTC(raw_adc):
    # https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation
    r1 = 10000
    vref = 3.3
    measure = (raw_adc / 4096) * vref
    ntc_ohm = ((r1 * vref) / measure) - r1
    A, B, C = 0.001129148, 0.000234125, 0.0000000876741  # Variables from manufact. Steinhart (constants*?)
    temp = 1/(A + B*(log(ntc_ohm)) + C*(log(ntc_ohm))**3) - 273.15
    return temp


while True:
    val = apin()                    # read an analog value
    print(ThermistorNTC(val))
    time.sleep(1)
