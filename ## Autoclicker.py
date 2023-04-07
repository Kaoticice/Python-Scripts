## Autoclicker
# Press "a" to sta

# Importing shit, time and threading
import time
import threading
from pynput.mouse import Button, Controller


# watch keyboard events for start and stop of auto-clicker
from pynput.keyboard import Listener, KeyCode

# variable assignments 
delay = 0.001
button = Button.left
startStopKey = KeyCode(char='a')
stopKey = KeyCode(char='b')
stopLoop = False # Stop variable, used to stop a loop

while stopLoop == False:

    # Threading used to conatrol clicks 
    class ClickMouse(threading.Thread):

        # Delay and button click are both in class
        def __init__(self, delay, button):
            super(ClickMouse, self).__init__()
            self.delay = delay
            self.button = button
            self.running = False
            self.program_running = True

        def startClicking(self):
            self.running = True
        
        def stopClicking(self):
            self.running = False
        
        def exit(self):
            self.stopClicking()
            self.program_running = False

        # Now define a method to check, run loop until
        # If method is true another loop will check
        # If it is set to true or not
        # for mouse click set to button and delay
        def run(self):
            while self.program_running:
                while self.running:
                    mouse.click(self.button)
                    time.sleep(self.delay)
                time.sleep(0.001)

    # mouse controller instance
    mouse = Controller()
    click_thread = ClickMouse(delay, button)
    click_thread.start()

        # New method on_press, taking key as argument

    def on_press(key): 

        # startStopKey will stop clicking if 
        # running flag is set to true

        if key == startStopKey:
            if click_thread.running:
                click_thread.stopClicking()
            else:
                click_thread.startClicking()

        # Exit method called, terminates auto
        # clicker when keya is pressed. 

        elif key == stopKey:
            click_thread.exit()
            listener.stop()
            stopLoop = True

    with Listener(on_press=on_press) as listener:
        listener.join()