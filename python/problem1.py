increased = 0
prev = 0

with open("../input/day1.txt", 'r') as file:
    for line in file:
        new_val = int(line)
        if new_val > prev:
            increased = increased + 1
        prev = new_val

print(increased - 1)