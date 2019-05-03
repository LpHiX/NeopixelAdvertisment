import globalvariables

import time
import board
import neopixel

pixpin = board.A3
numpix = 128

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)

def lookupColor(color, i):
    #black
    if color == 0:
        strip[i] = (0, 0, 0)
    #cyan
    elif color == 1:
        strip[i] = (0, 255, 255)
    #white
    elif color == 2:
        strip[i] = (255, 255, 255)
    #red
    elif color == 3:
        strip[i] = (255, 0, 0)
    #green
    elif color == 4:
        strip[i] = (0, 255, 0)
    #yellow
    elif color == 5:
        strip[i] = (255, 255, 0)

def showMessage(nextMessage,duration,myMessage):
    # start - fixed message 4
    # remember to change globalvariables.message#
    i = 0
    for r in range(0,8):
        for c in range(0,8):
            color = myMessage[r][c]
            lookupColor(color,i)
            i += 1
    for r in range(0,8):
        for c in range(8,16):
            color = myMessage[r][c]
            lookupColor(color,i)
            i += 1
    strip.write()
    time.sleep(duration)

    # switch to next message
    globalvariables.messageID = nextMessage
# ----------------------------------------------------------------------------------------------------
# START DO NOT MODIFY THE CODE BETWEEN THE ---
# ----------------------------------------------------------------------------------------------------


def showMessageL(nextMessage,duration,myMessage,startingPoint):
    # start - show Message
    if globalvariables.myStart == 0:
        globalvariables.myStart = 1
        globalvariables.countToMaxLength = startingPoint

    i = 0
    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength,globalvariables.countToMaxLength+8):
            temp = c % len(myMessage[0])
            color = myMessage[r][temp]
            lookupColor(color,i)
            i += 1

    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength+8,globalvariables.countToMaxLength+16):
            temp = c % len(myMessage[0])
            color = myMessage[r][temp]
            lookupColor(color,i)
            i += 1

    strip.write()

    globalvariables.countToMaxLength += 1
    globalvariables.durationCounter += 1
    if globalvariables.countToMaxLength > duration:
        globalvariables.countToMaxLength = 0
        globalvariables.myStart = 0
        globalvariables.durationCounter = 0
        globalvariables.messageID = nextMessage


# ----------------------------------------------------------------------------------------------------
# END DO NOT MODIFY THE CODE BETWEEN THE ---
# ----------------------------------------------------------------------------------------------------

while True:

    for r in range(0,13):
        # set brightness to a high value.  1.0 is the maximum value, 0.0 is the lowest
        strip.brightness = 0.05
        if globalvariables.messageID == 0:
            # showMessage(nextMessage,messageDuration,message)
            showMessage(1,0.1,globalvariables.message0)
        elif globalvariables.messageID == 1:
            showMessage(2,0.1,globalvariables.message1)
        elif globalvariables.messageID == 2:
            showMessage(3,0.1,globalvariables.message2)
        elif globalvariables.messageID == 3:
            showMessage(4,0.1,globalvariables.message3)
        elif globalvariables.messageID == 4:
            showMessage(5,0.1,globalvariables.message4)
        elif globalvariables.messageID == 5:
            showMessage(0,0.1,globalvariables.message5)

    showMessage(6,1,globalvariables.message6)
    strip.write()
