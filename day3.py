def index_of_max(bank: list[int], start: int, remaining_numbers: int) -> int:
    current_max = bank[start]
    max_index = start
    bank_length = len(bank) - remaining_numbers + 1

    for i in range(start, bank_length):
        if bank[i] > current_max:
            current_max = bank[i]
            max_index = i
            if current_max == 9:
                break
    return max_index

def part1(input: list[list[int]]) -> int:
    joltage = 0

    for bank in input:
        max_index = index_of_max(bank, 0, 2)
        second_max_index = index_of_max(bank, max_index + 1, 1)
        joltage += bank[max_index] * 10 + bank[second_max_index]
    
    return joltage

def part2(input: list[list[int]]) -> int:
    joltage = 0

    for bank in input:
        last_max_index = -1

        for i in range(12, 0, -1):
            max_index = index_of_max(bank, last_max_index + 1, i)
            joltage += bank[max_index] * (10 ** (i - 1))
            last_max_index = max_index

    return joltage

with open("input.txt") as f:
    input = [list(map(int, line.strip())) for line in f]

print(part1(input))
print(part2(input))