max = 0
sum = 0

with open("input.txt", "r") as f:
    inputValue = f.readlines()
    for line in inputValue:
        if line != "\n":
            sum += int(line)
        else:
            if max < sum:
                max = sum
            sum = 0

print(max)
