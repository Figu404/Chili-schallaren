import machine
from network import WLAN

from mqtt import MQTTClient

# A class named internet so that it is easy to make new connections to the internet and MQTT servers if we need it.
class Internet:
    def __init__(self, sub_cb = False, internet_name = False, internet_password = False, outhtype = False, internet_timeout = False, internet_auth= False, server = False,  device_id = False, user = False, password = False, port = False, topic = False):
        # All the varibles you need to connect to the internet and the MQTT servers.
        # all of them have a defualt value, but you can change them if you create a new object.
        # Internet(user = "Kalle", "topic" = "Kalle/feeds/Test") Then the user and where the information
        # is sent is changed, Easy and practical, i hope.
        self.message = None
        self.wlan = WLAN(mode=WLAN.STA)
        self.server = server if server is not False else "io.adafruit.com"
        self.device_id = device_id if device_id is not False else "device_id"
        self.user = user if user is not False else "Figu"
        self.password = password if password is not False else "aio_wwpF34UaWdf3AenaFfum0C4I1B5a"
        self.port = port if port is not False else 1883
        self.topic = topic if topic is not False else "Figu/feeds/humidity"
        self.internet_name = internet_name if internet_name is not False else "LNU-iot"
        self.internet_password = internet_password if internet_password is not False else "modermodemet"
        self.outhtype = outhtype if outhtype is not False else WLAN.WPA2 
        self.internet_auth = internet_auth if internet_auth is not False else (self.outhtype, self.internet_password)
        self.internet_timeout = internet_timeout if internet_timeout is not False else 5000

    def sub_cb(topic, msg):
        # Just returns the message that was found
        print("collected data:", msg)
        return msg

    def communicate(self, message = False):
        # This part is where all can go wrong, It can be stuck here and never end.
        # So maybe we will need to alert the user if it can not connect to the internet?
        # Or maybe just skip it if it have tried for too long. Becuese while it is tryeing
        # it can not check the humidity or turn on the pump or the heatlamp. So we dont
        # want it stuck here for ever trying to connect.
        adafruitconnected = False
        while True:
            try:
                if not self.wlan.isconnected():
                    print("Connecting to WiFi")
                    self.wlan.connect(self.internet_name, auth=self.internet_auth, timeout=self.internet_timeout)
                    while not self.wlan.isconnected():  
                        machine.idle()
                    print("Connected to WiFi\n")
                elif not adafruitconnected:
                    client = MQTTClient(self.device_id, self.server , user = self.user,password = self.password, port = self.port)
                    client.set_callback(self.sub_cb)
                    client.connect()
                    client.subscribe(topic=self.topic)
                    adafruitconnected = True
                    print("Connected to the server")
                elif message is not None:
                    client.publish(topic=self.topic, msg=message)
                    print("Sent:", message)
                    message = None
                    break
                else:
                    return client.check_msg()
            except OSError as er:
                print("failed: " + str(er))
                if not str(er) == "Connection to AP Timeout!":
                    client.disconnect()
                adafruitconnected = False
        