

def doesContain(assignment):
    elf1 = [int(i) for i in assignment[0].split("-")]
    elf2 = [int(i) for i in assignment[1].split("-")]
    if elf1[0] >= elf2[0] and elf1[1] <= elf2[1] or elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:
        return True
    return False


output = 0

with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip("\n")
        assignment = line.split(",")
        if doesContain(assignment):
            output += 1

print(output)
# '51-88,52-87\n'
