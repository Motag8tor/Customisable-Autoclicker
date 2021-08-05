import pyautogui, appJar, clicker

click_thread = ""

def goPress(press):                                                                                                                                                                                                                                      
    global click_thread
    if(press == "Go"):
        button = app.getEntry("key")
        
        try:
          delay = float(app.getEntry("delay"))
        except:
          delay = 0.01

        if delay < 0.001:
            delay = 0.001

        if click_thread != "":
            click_thread.exit()

        click_thread = clicker.Clicker(delay, button)
        click_thread.start()
            
        print("Spamming '" + button + "' with delay " + str(delay) + " seconds")
    else:
        if click_thread != "":
            click_thread.exit()
            print("Spamming Stopped")
            
app = appJar.gui("Autoclicker")
app.setSize("400x300")

app.setSticky("new")
app.addLabel("Enter the key you want to spam", row=0)
app.addEntry("key", row=1)

app.setSticky("new")
app.addLabel("Enter the delay in seconds", row=3)
app.addEntry("delay", row=4)

app.setSticky("new")
app.addButton("Go", goPress, row=8)
app.addButton("Stop", goPress, row=9)

app.go()