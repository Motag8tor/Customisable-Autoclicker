import pyautogui, time, threading

class Clicker(threading.Thread):
    def __init__(self, delay, button):
        super(Clicker, self).__init__()
        self.delay = delay
        self.button = button
        self.running = True

    def exit(self):
        self.running = False

    def run(self):
        pyautogui.PAUSE = 0
        while self.running:
            pyautogui.press(self.button)
            time.sleep(self.delay)