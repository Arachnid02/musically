from RNgraphics import *

def getWindowSize():
    print("Size of Window?")

    while True:
        Size = input()
        try:
            Size = int(Size)
            if Size <= 0:
                print("Value entered less than or equal to 0")
            else:
                break
        except ValueError:
            print("You entered a string, you apes")
    return Size

def WindowInit(windowName,Size):
    global playerWin
    playerWin = GraphWin(windowName,Size,Size)
    playerWin.setCoords(0,0,Size,Size)

def draw_text(tX,tY,string,color,win):
    message = Text(Point(tX,tY), string)
    message.setTextColor(color)
    message.draw(win)
def draw_ci(cX, cY, size, color, win,circle = None):
    #circle = boardState[incX][incY]
    circle = Circle(Point(cX, cY),size)
    circle.setFill(color)
    circle.draw(win)

def musicPlayerButtonsCir(color):
    draw_ci(windowSize/2,windowSize/5,windowSize/10,color,playerWin)
    draw_ci((windowSize/2) - windowSize/4,windowSize/5,windowSize/11,color,playerWin)
    draw_ci((windowSize/2) + windowSize/4,windowSize/5,windowSize/11,color,playerWin)
    draw_text(windowSize/2,windowSize/5,"Play","black",playerWin)
    draw_text((windowSize/2) - windowSize/4,windowSize/5,"Back","black",playerWin)
    draw_text((windowSize/2) + windowSize/4,windowSize/5,"Skip","black",playerWin)
windowSize = getWindowSize()

def checkMouseStatus():
    (mouseX,mouseY) = playerWin.getMouse()
    print("Mouse is over position (%s,%s)" % (mouseX,mouseY))

WindowInit("Music Player",windowSize)
draw_text(windowSize/2,windowSize/1.5,"Music Player","red",playerWin)
musicPlayerButtonsCir("white")


while True:
    checkMouseStatus()
