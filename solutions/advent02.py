file=open("numbers.txt")
lines=file.readlines()
x=0
y=0
aim=0
for line in lines:
    line=line.strip()
    line=line.split(" ")
    num=int(line[1])
    if line[0]=="forward":
        x+=num
        y+=aim*num
    elif line[0]=="down":
        #y+=int(line[1])
        aim+=num
    elif line[0]=="up":
        #y-=int(line[1])
        aim-=num
print(x)
print(y)
print(x*y)