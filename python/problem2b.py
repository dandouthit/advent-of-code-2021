horizontal = 0
depth = 0
aim = 0

with open("../input/day2.txt", 'r') as file:
    lines = file.read().split("\n")

lines = lines[:-1]
for line in lines:
    direction_unit_list = line.split()
    direction = direction_unit_list[0]
    unit = int(direction_unit_list[1])

    if direction == 'forward':
        horizontal += unit
        depth += (aim * unit)
    elif direction == 'down':
        aim += unit
    elif direction == "up":
        aim -= unit

print(horizontal * depth)