gamma_rate_bit_list = [0] * 12
epsilon_rate_bit_list = [0] * 12
one_counts = [0] * 12
zero_counts = [0] * 12

def bits_to_int(bits: list[int]) -> int:
    result = 0
    for bit in bits:
        result = (result << 1) | bit
    return result

with open("../input/day3.txt", 'r') as file:
    lines = file.read().split("\n")

lines = lines[:-1]

for line in lines:
    for i in range(12):
        bit = line[i]
        if bit == "1":
            one_counts[i] += 1
        elif bit == "0":
            zero_counts[i] += 1

print(one_counts)
print(zero_counts)

for i in range(12):
    gamma_rate_bit_list[i] = 1 if one_counts[i] > zero_counts[i] else 0
    epsilon_rate_bit_list[i] = gamma_rate_bit_list[i] ^ 1

print(gamma_rate_bit_list)
print(epsilon_rate_bit_list)
print(bits_to_int(gamma_rate_bit_list) * bits_to_int(epsilon_rate_bit_list))
