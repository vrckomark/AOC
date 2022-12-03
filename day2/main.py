# PLAYER 1:
# A - ROCK
# B - PAPER
# C - SCISSORS

# PLAYER 2:
# X - ROCK
# Y - PAPER
# Z - SCISSORS


options = {
    "A": {
        "counter": "Y",
        "counters": "Z",
        "type": "rock"
    },
    "B": {
        "counter": "Z",
        "counters": "X",
        "type": "paper"
    },
    "C": {
        "counter": "X",
        "counters": "Y",
        "type": "scissors"
    },
    "X": {
        "type": "rock"
    },
    "Y": {
        "type": "paper"
    },
    "Z": {
        "type": "scissors"
    },
}

points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

instructions = {
    "X": {
        "do": "lose",
        "points": 0
    },
    "Y": {
        "do": "draw",
        "points": 3
    },
    "Z": {
        "do": "win",
        "points": 6
    },
}

strategy = []
score = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        strategy = line.strip("\n").split(" ")
        # if strategy[1] == options[strategy[0]]["counter"]: PART 1
        #     score += 6
        # if options[strategy[0]]["type"] == options[strategy[1]]["type"]:
        #     score += 3
        # score += options[strategy[1]]["points"]
        if instructions[strategy[1]]["do"] == "win":  # PART 2
            score += points[options[options[strategy[0]]["counter"]]["type"]]
        if instructions[strategy[1]]["do"] == "draw":
            score += points[options[strategy[0]]["type"]]
        if instructions[strategy[1]]["do"] == "lose":
            score += points[options[options[strategy[0]]["counters"]]["type"]]
        score += instructions[strategy[1]]["points"]


print(score)
