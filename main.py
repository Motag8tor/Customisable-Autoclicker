import appJar, clicker
from pynput.keyboard import Listener, Key

click_thread = ""
start_key = Key.f6
stop_key = Key.f6

# ----------- Spam function -----------

def onPress(press):                                                                                                                                                                                                                                      
    global click_thread
    if press == "Go":
        removeThread()

        button = app.getEntry("key")
        if button == "":
            print("Please enter a character to spam")
            return

        try:
            delay = float(app.getEntry("delay"))
        except: 
            delay = 0.001

        if delay < 0.001: # Do not allow delays of less than 0.001s
            delay = 0.001

        click_thread = clicker.Clicker(delay, button) # Handle spam in another thread to keep the GUI from freezing
        click_thread.start()

        app.hideButton("Go")
        app.showButton("Stop")
        print("Spamming '" + button + "' with delay " + str(delay) + " seconds")
    elif press == "Stop":
        if click_thread != "":
            removeThread()
            print("Spamming Stopped")
        else:
            print("The Autoclicker is not currently running")

# ----------- Remove the current thread -----------

def removeThread():
    global click_thread
    if click_thread != "":
        click_thread.exit()
        click_thread = ""
        app.hideButton("Stop")
        app.showButton("Go")

# ----------- Detect Hotkey presses -----------

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

# ----------- Update Hotkeys -----------

def updateHotkeys():
    global start_key, stop_key

    key = app.getOptionBox("Start Hotkey")
    start_key = checkKey(key)
    app.setButton("Go", "Go <" + key + ">")
    print("Start Hotkey has been set to " + key)

    key = app.getOptionBox("Stop Hotkey")
    stop_key = checkKey(key)
    app.setButton("Stop", "Stop <" + key + ">")
    print("Stop Hotkey has been set to " + key)

# ----------- Update Hotkeys -----------

def checkKey(key):
    if key == "F1":
        return Key.f1
    elif key == "F2":
        return Key.f2
    elif key == "F3":
        return Key.f3
    elif key == "F4":
        return Key.f4
    elif key == "F5":
        return Key.f5
    elif key == "F6":
        return Key.f6
    elif key == "F7":
        return Key.f7
    elif key == "F8":
        return Key.f8
    elif key == "F9":
        return Key.f9
    elif key == "F10":
        return Key.f10
    elif key == "F11":
        return Key.f11
    elif key == "F12":
        return Key.f12
    else:
        return Key.f6 # Default Hotkey

# ----------- appJar Interface -----------
            
app = appJar.gui("Autoclicker")
app.setSize("400x300")

app.setSticky("new")
app.addLabel("Enter the key you want to spam", row=0)
app.addEntry("key", row=1)
app.setEntryDefault("key", "Key")
app.setEntryMaxLength("key", 10)

app.addLabel("Enter the delay in seconds", row=3)
app.addNumericEntry("delay", row=4)
app.setEntryDefault("delay", "Delay")

app.addLabel("Change Hotkeys", row=6)
hotkeys = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"] # Hotkeys array

app.addLabelOptionBox("Start Hotkey", hotkeys, row=7)
app.addLabelOptionBox("Stop Hotkey", hotkeys, row=8)
app.setOptionBox("Start Hotkey", 5)
app.setOptionBox("Stop Hotkey", 5)
app.addNamedButton("Confirm Hotkeys", "hotkeyStop", updateHotkeys, row=9)

app.addNamedButton("Go <F6>", "Go", onPress, row=11)
app.addNamedButton("Stop <F6>", "Stop", onPress, row=11)
app.hideButton("Stop")

listener = Listener(on_press=hotkey) # Call the hotkey function when keys are pressed
listener.start() # Begin listening for keypresses

app.go() # Run the app
