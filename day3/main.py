
output = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip("\n")
        rucksack = [line[0:len(line)//2], line[len(line)//2:len(line)]]
        priorityLetter = "".join(
            set(rucksack[0]).intersection(set(rucksack[1])))
        letterNumber = ord(priorityLetter)
        if letterNumber >= 65 and letterNumber <= 90:
            output += letterNumber-65+27
        if letterNumber >= 97 and letterNumber <= 122:
            output += letterNumber-96
print(output)
