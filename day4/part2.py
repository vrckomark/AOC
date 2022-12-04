

def doesOverlap(assignment):
    elf1 = [int(i) for i in assignment[0].split("-")]
    elf1 = set(range(elf1[0], elf1[1]+1))
    elf2 = [int(i) for i in assignment[1].split("-")]
    elf2 = set(range(elf2[0], elf2[1]+1))
    if len(elf1.intersection(elf2)) > 0:
        return True
    return False


output = 0

with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip("\n")
        assignment = line.split(",")
        if doesOverlap(assignment):
            output += 1

print(output)
# '51-88,52-87\n'
