songLib = open("songLib.tsv","r")
songLib_data = []
for line in songLib:
    number_songs = line.split("\t")
    songs = [n for n in number_songs]
    songLib_data.append(songs)

songLib_data_tuple = tuple(songLib_data)
print(songLib_data_tuple[6][15])
