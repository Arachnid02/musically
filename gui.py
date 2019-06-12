#musically.py- Kaylee N
from graphics import *

musicWin = GraphWin("Musically", 700, 700)
musicWin.setCoords(0,0,700,700)

pg1 = False
pg2 = False
    

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

#next button
nextRec = Rectangle(Point(610,10),Point(690,60))
nextRec.setFill(color_rgb(0,255,0))
nextRec.draw(musicWin)
#next
nextTex = Text(Point(650, 35), "next page")
nextTex.setSize(15)
nextTex.setStyle("bold")
nextTex.setTextColor("black")
nextTex.draw(musicWin)


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
       
qOneWin = GraphWin("Musically Page 1", 700,700)
qOneWin.setCoords(0,0,700,700)

#Next Page Questions
quesOne = Text(Point(140, 670), "1. What's the title of the song?")
quesOne.setSize(18)
quesOne.setStyle("bold")
quesOne.setTextColor("black")
quesOne.draw(qOneWin)

inTitle = Entry(Point(150, 645), 20)
inTitle.setTextColor("black")
inTitle.draw(qOneWin)

quesTwo = Text(Point(253, 600), "2. How fast or slow is this song? Rate 1-10, 10 meaning it's super fast!")
quesTwo.setSize(16)
quesTwo.setStyle("bold")
quesTwo.setTextColor("black")
quesTwo.draw(qOneWin)

quesThree = Text(Point(360, 550), "3.How much this song make you want to dance? Rate 1-10, 10 meaning your body starts moving as soon as you hear it.")
quesThree.setSize(13)
quesThree.setStyle("bold")
quesThree.setTextColor("black")
quesThree.draw(qOneWin)

#next button
nextRec = Rectangle(Point(610,10),Point(690,60))
nextRec.setFill(color_rgb(0,255,0))
nextRec.draw(qOneWin)

nextTex = Text(Point(650, 35), "next page")
nextTex.setSize(15)
nextTex.setStyle("bold")
nextTex.setTextColor("black")
nextTex.draw(qOneWin)

uTitle = inTitle.getText()
print("User title = ", uTitle)

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
    
    
