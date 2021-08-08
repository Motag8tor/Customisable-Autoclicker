import appJar, clicker
from pynput.keyboard import Listener, Key

click_thread = ""
start_key = Key.f6
stop_key = Key.f6

# ----------- Spam function -----------

def onPress(press):                                                                                                                                                                                                                                      
    global click_thread
    if press == "Go":
        if click_thread != "":
            click_thread.exit()
            click_thread = ""

        button = app.getEntry("key")
        if button == "":
            print("Please enter a character to spam")
            return

        try:
            delay = float(app.getEntry("delay"))
        except:
            delay = 0.001

        if delay < 0.001: # Do not allow delays less than 0.001s
            delay = 0.001

        click_thread = clicker.Clicker(delay, button) # Handle spam in another thread to keep the GUI from freezing
        click_thread.start() # Begin

        app.hideButton("Go")
        app.showButton("Stop")
        print("Spamming '" + button + "' with delay " + str(delay) + " seconds")
    elif press == "Stop":
        if click_thread != "":
            click_thread.exit()
            click_thread = ""
            app.hideButton("Stop")
            app.showButton("Go")
            print("Spamming Stopped")
        else:
            print("The Autoclicker is not currently running")

# ----------- Detect hotkey presses -----------

def hotkey(key):
    if start_key == stop_key and key == start_key:
        if click_thread != "":
            onPress("Stop")
        else:
            onPress("Go")
    else:
        if key == start_key:
            onPress("Go")
        elif key == stop_key:
            onPress("Stop")

# ----------- appJar Interface -----------
            
app = appJar.gui("Autoclicker")
app.setSize("400x300")

app.setSticky("new")
app.addLabel("Enter the key you want to spam", row=0)
app.addEntry("key", row=1)
app.setEntryDefault("key", "Key")
app.setEntryMaxLength("key", 10)

app.setSticky("new")
app.addLabel("Enter the delay in seconds", row=3)
app.addNumericEntry("delay", row=4)
app.setEntryDefault("delay", "Delay")

app.setSticky("new")
app.addNamedButton("Go <F6>", "Go", onPress, row=8)
app.addNamedButton("Stop <F6>", "Stop", onPress, row=8)
app.hideButton("Stop")

listener = Listener(on_press=hotkey) # Call the hotkey function when keys are pressed
listener.start() # Begin listening for keypresses

app.go() # Run the app
