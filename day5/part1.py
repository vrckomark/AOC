crates = []
instructions = []
for i in range(9):
    crates.append([])


def getInitialSetup():
    with open("input.txt", "r") as f:
        for idx, line in enumerate(f.readlines()):
            if idx < 8:
                row = ""
                for idx, char in enumerate(line):
                    if (idx+1) % 4 != 0:
                        row += char
                temp = []
                for index in range(0, len(row), 3):
                    temp.append(row[index: index + 3])
                for index, i in enumerate(temp):
                    if i != "   ":
                        temp[index] = i[1]
                    else:
                        temp[index] = i.strip()
                for idx, i in enumerate(temp):
                    if i != "":
                        crates[idx].append(i)

        f.close()


temp = []


def getInstructions():
    with open("input.txt", "r") as f:
        for idx, line in enumerate(f.readlines()):
            if idx >= 10:
                line = line.replace("move ", "").replace(
                    "from ", "").replace("to ", "").strip("\n")
                temp = [int(i) for i in line.split(" ")]
                instructions.append(temp)


getInitialSetup()
getInstructions()

for idx, ins in enumerate(instructions):
    instructions[idx][1] -= 1
    instructions[idx][2] -= 1

for i in crates:
    i = i.reverse()

# for i in crates:
#     print(i)

# 7,2,8
# 2,4,1
for i in instructions:
    for j in range(i[0]):
        crates[i[2]].append(crates[i[1]][-1])
        crates[i[1]].pop()

for i in crates:
    print(i[-1], end="")
