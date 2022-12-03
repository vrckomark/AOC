
def getLetterNumber(letter):
    letterNumber = ord(letter)
    if letterNumber >= 65 and letterNumber <= 90:
        return letterNumber-65+27
    if letterNumber >= 97 and letterNumber <= 122:
        return letterNumber-96


output = 0
_temp = []
with open("input.txt", "r") as f:
    for index, line in enumerate(f.readlines()+["\n"]):
        line = line.strip("\n")
        if index % 3 == 0 and index != 0:
            priorityLetter = "".join(
                set(_temp[0]).intersection(set(_temp[1]), set(_temp[2])))
            output += getLetterNumber(priorityLetter)
            print(
                f"Index:{index}\nGroup: {_temp}\nletter: {priorityLetter}\nLetterNumber: {getLetterNumber(priorityLetter)}\nOutput: {output}\n\n")
            _temp = []
        _temp.append(line)

print(output)
