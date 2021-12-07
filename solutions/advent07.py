file = open("numbers.txt")
lines=file.read().strip("\n").split(",")
nums=list(int(line) for line in lines)
diffs=[]
for i in range(min(nums),max(nums)+1):
    numdiffs=[]
    for j in range(len(nums)):
        d=abs(nums[j]-i)
        # comment out the following line for part 1 solution
        d=(d*(d+1))/2
        numdiffs.append(d)
    diffs.append(sum(numdiffs))
k=diffs.index(min(diffs))
print(diffs[k])