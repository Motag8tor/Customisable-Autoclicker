import pyautogui, time, threading

# ----------- Spam class -----------

class Clicker(threading.Thread):
    def __init__(self, delay, button):
        super(Clicker, self).__init__()
        self.delay = delay
        self.button = button
        self.running = True

    def exit(self):
        self.running = False # Set to False to stop loop

    def run(self):
        pyautogui.PAUSE = 0 # Remove built-in pyautogui delay
        while self.running: # Infinite loop to spam character
            pyautogui.press(self.button)
            time.sleep(self.delay)
