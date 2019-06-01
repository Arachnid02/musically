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

def determineRelevantAmountofSongs(threshold):
    relevantSongsCount = 0
    for diff in diffLib:
        if diff < threshold:
            relevantSongsCount += 1
    return relevantSongsCount

def findReleventSong(Lib):
    for x in range(195 - determineRelevantAmountofSongs(10)):
        Lib.remove(max(Lib))
        return Lib

songLib = formatMusic("songLib.tsv")
userInput = [5,3,4,7,8,7,8] #made up user input
diffLib = findDiff(songLib,userInput)
releventSongs = findReleventSong(diffLib)
