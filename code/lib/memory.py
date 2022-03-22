import json
import pycom

# Saves data in a dict

class Memory():
    def __init__(self):
        # Loads the memory from the pycom
        # This cache memory is only memory for the object and not same for every intenses.
        # i dont know if we want it or if we want like a class varieble instead
        self.load()
        
    def load(self):
        # reads the memory from the pycom
        memory = {}
        try:
            file = open("data.txt", "r")
            memory= json.loads(file.read())
        except:
            print("ERROR: File not accessible")
        self.local_memory = memory

    def save(self):
        # Saves memory to storage 
        # the memory is saved in json in the file data.txt on the pycom
        file = open("data.txt", "w")
        file.write(json.dumps(self.local_memory))
        file.close()

    def upload():
        # Maybe we can uppload the data to the servers?
        pass



