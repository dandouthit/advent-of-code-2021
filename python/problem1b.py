increased = 0
prev = 0
three_window_sums = []

with open("../input/day1.txt", 'r') as file:
    lines = file.read().split("\n")

lines = lines[:-1]

for i in range(len(lines)):
    if i <= 1997:
        three_window_sums.append(int(lines[i]) + int(lines[i+1]) + int(lines[i+2]))

for line in three_window_sums:
    new_val = int(line)
    if new_val > prev:
        increased = increased + 1
    prev = new_val

print(increased - 1)