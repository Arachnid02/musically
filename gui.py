#musically.py- Kaylee N
from RNgraphics import *
from formatMusic import *

pg1 = False
pg2 = False
rX = 100
rY = 100
text = "next page"
txSize = 15
rCol = color_rgb(0, 255, 0)
txCol = "black"
style = "bold"
askTitle = "1. What's the title of the song?"
askTempo = "2. How fast or slow is this song? Rate 1-10, 10 meaning it's super fast!"
askDdr = """3.How much this song make you want to dance? Rate 1-10, 10 meaning
              your body starts moving as soon as you hear it."""

def questions(tX, tY, text, size, style, color, win):
    question = Text(Point(tX, tY), text)
    question.setSize(size)
    question.setStyle(style)
    question.setTextColor(color)
    question.draw(win)

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

def questions(tX, tY, text, size, style, color, win):
    question = Text(Point(tX, tY), text)
    question.setSize(size)
    question.setStyle(style)
    question.setTextColor(color)
    question.draw(win)

pg1 = False
pg2 = False

#variables
rX = 100
rY = 100
text = "next page"
txSize = 15
rCol = color_rgb(0, 255, 0)
txCol = "black"
style = "bold"

#question variables
askTitle = "1. What's the title of the song?"
askTempo = "2. How fast or slow is this song? Rate 1-10, 10 meaning it's super fast!"
askDdr = "3.How much this song make you want to dance? Rate 1-10, 10 meaning your body starts moving as soon as you hear it."
askRhy = "4.How good does the rhythm flow with the rest of the song? Rate 1-10, 10 meaning it flows so well."
askMel = "5.How well does the melody flow? Rate 1-10, 10 meaning it goes along with the song well."
askLyr = "6.How good are the lyrics? Rate 1-10, 10 meaning those lyrics hit you on a whole other level."
askVoc = "7.Rate the vocals in this song from 1-10, 10 meaning the vocals were beautiful."
askIns = "8.What's the quality of the instrumental skill? Rate 1-10."

musicWin = GraphWin("Musically", 700, 700)
musicWin.setCoords(0,0,700,700)

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

#1.Ask User For Name of Their Song
questions(rX * 1.4, rY * 6.7, askTitle, 18, style, txCol, qOneWin)

#Get User Song Title
inTitle = Entry(Point(150, 640), 20)
inTitle.setTextColor("black")
inTitle.draw(qOneWin)

#2.Ask User For Tempo
questions(rX * 2.9, rY * 6.14, askTempo, 17, style, txCol, qOneWin)

#Get User Song Tempo
inTempo = Entry(Point(150, 580), 20)
inTempo.setTextColor("black")
inTempo.draw(qOneWin)

#3.Ask User For DDR
questions(rX * 3.33, rY * 5.4, askDdr, 12, style, txCol, qOneWin)

#Get User Song DDR
inDdr = Entry(Point(150, 500), 20)
inDdr.setTextColor("black")
inDdr.draw(qOneWin)

#4.Ask User For the Rate of the Rhythm to Their Song
questions(rX * 3.5, rY * 4.6, askRhy, 15, style, txCol, qOneWin)

#Get User Song Rhythm
inRhy = Entry(Point(150, 420), 20)
inRhy.setTextColor("black")
inRhy.draw(qOneWin)

#5.Ask User For How Good the Melody is in Their Song
questions(rX * 3.3, rY * 3.8, askMel, 16, style, txCol, qOneWin)

#Get User Song Melody
inMel = Entry(Point(150, 340), 20)
inMel.setTextColor("black")
inMel.draw(qOneWin)

#6.Ask User For the Quality of the Lyrics to Their Song
questions(rX * 3.4, rY * 3, askLyr, 16, style, txCol, qOneWin)

#Get User Song Lyrics
inLyr = Entry(Point(150, 260), 20)
inLyr.setTextColor("black")
inLyr.draw(qOneWin)

#7.Ask User For the Vocals of Their Song
questions(rX * 3.5, rY * 2.2, askVoc, 18, style, txCol, qOneWin)

#Get User Song Vocals
inVoc = Entry(Point(150, 180), 20)
inVoc.setTextColor("black")
inVoc.draw(qOneWin)

#8.Ask User For the Instrumental Skill of Their Song
questions(rX * 2.5, rY * 1.4, askIns, 18, style, txCol, qOneWin)

#Get User Song Melody
inIns = Entry(Point(150, 100), 20)
inIns.setTextColor("black")
inIns.draw(qOneWin)

#melody image
melImage = Image(Point(350,340), "melody.png")
melImage.draw(qOneWin)

#dance image
ddrImage = Image(Point(480,480), "dance.png")
ddrImage.draw(qOneWin)

#instruments image
insImage = Image(Point(560,120), "instruments.png")
insImage.draw(qOneWin)

#music note 2 image
mntImage = Image(Point(640,640), "MUSICNOTE.png")
mntImage.draw(qOneWin)

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

uTitle = inTitle.getText()
print("User title = ", uTitle)

uTempo = inTempo.getText()
print("User tempo =", uTempo)

uDdr = inDdr.getText()
print("User ddr = ", uDdr)

uRhy = inRhy.getText()
print("User rhythm = ", uRhy)

uMel = inMel.getText()
print("User melody = ", uMel)

uLyr = inLyr.getText()
print("User lyrics = ", uLyr)

uVoc = inVoc.getText()
print("User vocals = ", uVoc)

uIns = inIns.getText()
print("User ins skill = ", uIns)

songLib = formatMusic("songLib.tsv")
userInput = [uIns,uLyr,uVoc,uMel,uRhy,uDdr,uTempo]
print(userInput)
playableSongs = []
while len(playableSongs) == 0:
    count = 5
    diffLib = findDiff(songLib,userInput)
    relevantSongList = determineRelevantSongs(diffLib,count)
    playableSongs = determineQue(songLib,relevantSongList)
    count += 1
for x in playableSongs:
    print(x[:1])

#qOneWin.close()
