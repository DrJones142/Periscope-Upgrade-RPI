
def raisePopUp(PopUpNum):
    print("Popup ",PopUpNum, " raised!")

def lowerPopUp(PopUpNum):
    print("Popup ",PopUpNum, " lowered!")

def setPWMValue(channel,dutyCycle):
    print("Channel ",channel, ":",dutyCycle)

def selectRelay(relayInt):
    print("Pi: ",relayInt)

def forward():
    print("Pi:Forward")

def sendToGUI(message):
    print(message)