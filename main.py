import appJar, clicker
from pynput.keyboard import Listener, Key

click_thread = ""
start_key = Key.f8
stop_key = Key.f9

def goPress(press):                                                                                                                                                                                                                                      
    global click_thread
    if press == "Go <F8>":
        button = app.getEntry("key")
        
        try:
          delay = float(app.getEntry("delay"))
        except:
          delay = 0.001

        if delay < 0.001:
            delay = 0.001

        if click_thread != "":
            click_thread.exit()

        if app.getEntry("key") == "":
            print("Please enter a character to spam")
            return False

        click_thread = clicker.Clicker(delay, button)
        click_thread.start()
            
        print("Spamming '" + button + "' with delay " + str(delay) + " seconds")
    elif press == "Stop <F9>":
        if click_thread != "":
            click_thread.exit()
            print("Spamming Stopped")
        else:
            print("The Autoclicker is not currently running")

def on_press(key):
    if key == start_key:
        goPress("Go <F8>")
    elif key == stop_key:
        goPress("Stop <F9>")
            
app = appJar.gui("Autoclicker")
app.setSize("400x300")

app.setSticky("new")
app.addLabel("Enter the key you want to spam", row=0)
app.addEntry("key", row=1)

app.setSticky("new")
app.addLabel("Enter the delay in seconds", row=3)
app.addEntry("delay", row=4)

app.setSticky("new")
app.addButton("Go <F8>", goPress, row=8)
app.addButton("Stop <F9>", goPress, row=9)

listener = Listener(on_press=on_press)
listener.start()
    
app.go()