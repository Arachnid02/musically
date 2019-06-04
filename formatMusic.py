from pytube import YouTube
import os

def formatMusic(fileName):
    songLib = open(fileName,"r")
    songLib_data = []
    for line in songLib:
        number_songs = line.split("\t")
        songs = [n for n in number_songs]
        songLib_data.append(songs)
    for song in songLib_data:
        song[16] = (song[16][:1])
    songLib_data_tuple = tuple(songLib_data)
    return songLib_data_tuple

def findDiff(lib,userInput):
    DiffHold = []
    for song in lib:
        diff = 0

        for x in range(6):
            try:
                diffbuff = abs(int(song[(x) + 10]) - int(userInput[x]))
                diff = diffbuff + diff
            except ValueError:
                pass
        DiffHoldbuffer = [diff]
        DiffHold = DiffHold + DiffHoldbuffer
    return DiffHold

def determineRelevantSongs(lib,threshold):
    newlib = []
    for x in range(len(lib)):
        if lib[x] < threshold:
            newlib.append(1)
        else:
            newlib.append(0)
    return newlib

def determineQue(songLib,revLib):
    songQue = []
    if len(songLib) == len(revLib):
        for x in range(len(songLib)):
            if revLib[x] == 1:
                songQue.append(songLib[x])
    else:
        print("something is wrong")
    return songQue
    
def getSongs(link,lib):
    YouTube(link).streams.first().download("songs",lib[0])

if not os.path.exists("songs"):  #creates dir "images" if dosn't exist
    os.mkdir("songs")

songLib = formatMusic("songLib.tsv")
userInput = [5,3,4,7,8,7,8] #made up user input
diffLib = findDiff(songLib,userInput)
relevantSongList = determineRelevantSongs(diffLib,10)
playableSongs = determineQue(songLib,relevantSongList)
print(playableSongs) #playablesongs is what we que into our music player
