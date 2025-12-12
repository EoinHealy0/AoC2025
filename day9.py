def check_loop() -> bool:
    pass

def fill_loop(matrix: list[bytearray]):
    pass

def part1(input: list[tuple[int]]) -> int:
    max_area = 0
    input_size = len(input)

    for i in range(input_size):
        x1, y1 = input[i]
        for j in range(i + 1, input_size):
            x2, y2 = input[j]
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > max_area:
                max_area = area

    return max_area

def part2(input: list[tuple[int]]) -> int:
    matrix = [bytearray(15) for _ in range(9)]
    input_size = len(input)

    for i in range(0, len(input)):
        x, y = input[i]
        nx, ny = input[i + 1] if i + 1 < input_size else (input[0])

        for j in range(min(y, ny), max(y, ny) + 1):
            for k in range(min(x, nx), max(x, nx) + 1):
                matrix[j][k] = 1
                
    fill_loop(matrix)
    for row in matrix:
        print(''.join(map(str, row)))
    return None

with open("input.txt") as f:
    input = [tuple(map(int, line.strip().split(","))) for line in f]

print(part1(input))
part2(input)