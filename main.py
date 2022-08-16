import time,math,random,sys
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, rotate=0)
RED = display.create_pen(255, 0, 0)
BLACK = display.create_pen(0, 0, 0)
stacks=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
MAX=255

def clear():
    display.set_pen(BLACK)
    display.clear()

def drawGauge(power):
    clear()
    for p in range(power):
        print(p)
        C=stacks[p]
        COLOUR=display.create_pen(int((C*MAX)/100),int((C*MAX)/-100),0)
        display.set_pen(COLOUR)
        display.rectangle(int((C*MAX)/100),10,10,110)
        display.update()

while True:
    v = sys.stdin.readline()
    print(v)
    drawGauge(int(v))
    #drawGauge(random.randint(0,len(stacks)-1))
    time.sleep(.1)

