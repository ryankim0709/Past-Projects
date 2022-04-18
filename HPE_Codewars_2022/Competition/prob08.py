numSongs = int(input())

mins = 0
secs = 0
for i in range(numSongs):
    line = input().split(":")
    mins += int(line[0])
    secs += int(line[1])

if secs >= 60:
    mins += (secs//60)
    secs = secs%60

if secs < 10:
    secs = "0" + str(secs)
print(f"{mins}:{secs}")
