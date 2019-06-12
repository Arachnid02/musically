#musically.py- Kaylee N
from graphics import *

#if we make rX and rY == 100, we can easily compute it by multipying by a flaot (ex. 100 * 1.1 = 110)

def nextButton(rX, rY, text, txSize, rCol, txCol, style, win):
    nextRec = Rectangle(Point(rX * 6.1, rY * 0.1), Point(rX * 6.9, rY * 0.6))
    nextRec.setFill(rCol)
    nextRec.draw(win)

    nextTex = Text(Point(rX * 6.5, rY * 0.35), text)
    nextTex.setSize(txSize)
    nextTex.setStyle(style)
    nextTex.setTextColor(txCol)
    nextTex.draw(win)    

musicWin = GraphWin("Musically", 700, 700)
musicWin.setCoords(0,0,700,700)

pg1 = False
pg2 = False

rX = 100
rY = 100
text = "next page"
txSize = 15
rCol = color_rgb(0, 255, 0)
txCol = "black"
style = "bold"

#Text
intro = Text(Point(350, 570), "Welcome to our Music Program!")
intro.setSize(20)
intro.setStyle("bold")
intro.setTextColor("black")
intro.draw(musicWin)

direct = Text(Point(350, 520), "We are gonna ask you a couple questions about YOUR favorite song!")
direct.setSize(20)
direct.setStyle("bold")
direct.setTextColor("black")
direct.draw(musicWin)

#music note image
mnoteImage = Image(Point(350,210), "music notes.png")
mnoteImage.draw(musicWin)


#Next Page Button
nextButton(rX, rY, text, txSize, rCol, txCol, style, musicWin)

while pg1 == False:
    try:
        nextCl = musicWin.getMouse()#button
        nextClx = nextCl.getX()#x
        print(nextClx)
        nextCly = nextCl.getY()#y
        print(nextCly)
        if nextClx > 610 and nextClx < 690 and nextCly > 10 and nextCly < 60:
            pg1 = True
            
    except ValueError:
        print("Click error")

musicWin.close()

#Next Page Questions
qOneWin = GraphWin("Musically Page 1", 700,700)
qOneWin.setCoords(0,0,700,700)

#Ask User For Name of Their Song
askTitle = Text(Point(140, 670), "1. What's the title of the song?")
askTitle.setSize(18)
askTitle.setStyle("bold")
askTitle.setTextColor("black")
askTitle.draw(qOneWin)

#Get User Song Title
inTitle = Entry(Point(150, 645), 20)
inTitle.setTextColor("black")
inTitle.draw(qOneWin)
uTitle = inTitle.getText()
print("User title =", uTitle)

askTempo = Text(Point(253, 600), "2. How fast or slow is this song? Rate 1-10, 10 meaning it's super fast!")
askTempo.setSize(16)
askTempo.setStyle("bold")
askTempo.setTextColor("black")
askTempo.draw(qOneWin)

askDdr = Text(Point(360, 550), "3.How much this song make you want to dance? Rate 1-10, 10 meaning your body starts moving as soon as you hear it.")
askDdr.setSize(13)
askDdr.setStyle("bold")
askDdr.setTextColor("black")
askDdr.draw(qOneWin)

#Next Page Button
nextButton(rX, rY, text, txSize, rCol, txCol, style, qOneWin)

while pg2 == False:
    try:
        nextCl = qOneWin.getMouse()#button
        nextClx = nextCl.getX()#x
        print(nextClx)
        nextCly = nextCl.getY()#y
        print(nextCly)
        if nextClx > 610 and nextClx < 690 and nextCly > 10 and nextCly < 60:
            pg2 = True
            
    except ValueError:
        print("Click error")
        
qOneWin.close()

qTwoWin = GraphWin("Musically Page 2", 700,700)
qTwoWin.setCoords(0,0,700,700)
    
    
