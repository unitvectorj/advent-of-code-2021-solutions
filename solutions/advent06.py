file=open("numbers.txt")
starts=file.read().strip("\n").split(",")
#fishies=[]
#for s in starts:
#    fishies.append(int(s))
fishies=list(int(s) for s in starts)
del starts
day=0
days=[0]*9
for fish in fishies:
    days[fish]+=1
while day<256:
    print(f"day: {day}")
    day+=1
    breeders=days.pop(0)
    days.append(breeders)
    days[6]+=breeders
print(sum(days))