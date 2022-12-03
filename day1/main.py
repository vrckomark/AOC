max = 0
tempSum = 0
sums = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        if line != "\n":
            tempSum += int(line)
        else:
            sums.append(tempSum)
            if max < tempSum:
                max = tempSum
            tempSum = 0
sums.sort(reverse=True)  # part 2
print(sum(sums[0:3]))  # part 2
print(sums[0])  # part 1
