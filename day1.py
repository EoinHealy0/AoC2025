START = 50
MAX = 100

def part1(rotations: list[str]) -> int:
    current = START
    password = 0
    
    for turn in rotations:
        dir, value = turn[0], int(turn[1:])
        new_position = 0

        if dir == 'L':
            value = -value
        
        new_position = current + value

        if new_position < 0:
            new_position = MAX + new_position
            
        current = new_position % MAX

        if current == 0:
            password += 1
    
    return password
        

def part2(rotations: list[str]) -> int:
    current = START
    password = 0
    
    for turn in rotations:
        dir, value = turn[0], int(turn[1:])
        new_position = 0

        password += value // 100 # over 100 means it fully rotated at least once regardless of the current position
        value = value % 100

        if dir == 'L':
            value = -value
        
        new_position = current + value

        if new_position < 0:
            new_position = MAX + new_position
            if current != 0:
                password += 1
        elif new_position > MAX:
            password += 1

        current = new_position % MAX

        if current == 0 and value != 0:
            password += 1
    
    return password

with open("input.txt") as f:
    input = [line.strip() for line in f]

print(part1(input))
print(part2(input))