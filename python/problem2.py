horizontal = 0
depth = 0

with open("../input/day2.txt", 'r') as file:
    lines = file.read().split("\n")

lines = lines[:-1]
for line in lines:
    direction_unit_list = line.split()
    print(direction_unit_list)
    direction = direction_unit_list[0]
    unit = direction_unit_list[1]

    if direction == 'forward':
        horizontal += int(unit)
    elif direction == 'down':
        depth += int(unit)
    else:
        depth -= int(unit)

print(horizontal * depth)