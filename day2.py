import math

def is_valid_repeating_number_new(number: int, min_subnum_length: int) -> bool:
    num_length = math.floor(math.log10(number)) + 1
                  
    for subnum_len in range((num_length // 2), min_subnum_length - 1, - 1):
        current_number = number

        if num_length % subnum_len == 0:
            divisor = 10 ** subnum_len
            sub_num = number % divisor
            is_match = True

            while current_number > 0:
                if current_number % divisor != sub_num:
                    is_match = False
                    break
                current_number //= divisor

            if is_match:
                return True
    
    return False

def part1(input: list[tuple]) -> int:
    total = 0

    for min, max in input:
        # Skip ranges where all numbers have an odd number of digits
        minlen = math.floor(math.log10(min)) + 1
        maxlen = math.floor(math.log10(max)) + 1

        if not(minlen == maxlen and minlen % 2 == 1):
            for number in range(min, max + 1):
                if is_valid_repeating_number_new(number, (math.floor(math.log10(number)) // 2) + 1):
                    total += number
    return total

def part2(input: list[tuple]) -> int:
    total = 0
    
    for min, max in input:
        for number in range(min, max + 1):
            if is_valid_repeating_number_new(number, 1):
                total += number
    return total

with open("input.txt") as f:
    input = f.readline().strip().split(",")
    ranges = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in input]

print(part1(ranges))
print(part2(ranges))