#musically.py- Kaylee N
from graphics import *

musicWin = GraphWin("Musically", 700, 700)
musicWin.setCoords(0,0,700,700)

#Text
intro = Text(Point(350, 500), "Welcome to our Music Program!")
intro.setSize(20)
intro.setStyle("bold")
intro.setTextColor("black")
intro.draw(musicWin)

direct = Text(Point(350, 450), "We are gonna ask you a couple questions about YOUR favorite song!")
direct.setSize(20)
direct.setStyle("bold")
direct.setTextColor("black")
direct.draw(musicWin)

#music note image
#mnoteImage = Image(Point(350,650), "music notes.png")
#mnoteImage.draw(musicWin)

#next button
nextRec = Rectangle(Point(500,100),Point(650,200))
nextRec.setFill(color_rgb(0,255,0))
nextRec.draw(musicWin)


              
