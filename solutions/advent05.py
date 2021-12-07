from numpy import right_shift, zeros

file=open("numbers.txt")
lines=file.readlines()
space=zeros((1000,1000))

def horizontal(x1,x2,y):
    left,right=(min([x1,x2]),max([x1,x2])+1)
    for x in range(left,right):
        space[x][y]+=1

def vertical(y1,y2,x):
    top,bottom=(min([y1,y2]),max([y1,y2])+1)
    for y in range(top,bottom):
        space[x][y]+=1

def diagonal(x1,x2,y1,y2):
    ran=abs(x1-x2)+1
    for i in range(ran):
        if x1<x2:
            if y1<y2:
                space[x1+i][y1+i]+=1
            else:
                space[x1+i][y1-i]+=1
        else:
            if y1<y2:
                space[x1-i][y1+i]+=1
            else:
                space[x1-i][y1-i]+=1

def count_twos():
    count=0
    for i in range(1000):
        for j in range(1000):
            if space[i][j]>1:
                count+=1
    return count

# the main loop
if __name__=="__main__":
        
    # turn them all into int lists
    for i,line in enumerate(lines):
        line=line.strip()
        lines[i]=line.split(" -> ")
        for j,entry in enumerate(lines[i]):
            lines[i][j]=entry.split(",")
            for k in range(2):
                lines[i][j][k]= int(lines[i][j][k])

    # check lines and add vertical or horizontal lines to space
    for line in lines:
        if line[0][0]==line[1][0]:
            vertical(line[0][1],line[1][1],line[0][0])
        elif line[0][1]==line[1][1]:
            horizontal(line[0][0],line[1][0],line[0][1])
        else:
            diagonal(line[0][0],line[1][0],line[0][1],line[1][1])

    print(count_twos())