import re

def get_column_indexes(operators: str) -> list[int]:
    indexes = [0]

    for i in range(1, len(operators)):
        if operators[i] == '+' or operators[i] == '*':
            indexes.append(i - 1)
            
    indexes.append(len(operators))
    return indexes

def get_horizontal_values(values: list[str], col_indexes: list[int]) -> list[list[int]]:
    horizontal_values = []

    for i in range(0, len(col_indexes) - 1):
        current_row = []
        for j in range(0, len(values)):
            current_row.append(int(values[j][col_indexes[i]:col_indexes[i+1]].strip()))
        horizontal_values.append(current_row)

    return horizontal_values

def get_vertical_values(values: list[str], col_indexes: list[int]) -> list[list[int]]:
    vertical_values = []
    current_group = []
    current_index = len(col_indexes) - 1

    for i in range(len(values[0]) - 1, -1, -1):
        current_value = ""

        for j in range(0, len(values)):
            if values[j][i] != " ":
                current_value += values[j][i]
        if current_value:
            current_group.append(int(current_value))
        if i == col_indexes[current_index - 1]:
            current_index -= 1
            vertical_values.append(current_group)
            current_group = []
            current_value = ""

    return vertical_values

def prod(operands: list[int]) -> int:
    result = 1
    for n in operands:
        result *= n
    return result

def part1(values: list[str], operators: list[str], col_indexes: list[int]) -> int:
    total = 0
    horizontal_values = get_horizontal_values(values, col_indexes)

    for i, op in enumerate(operators):
        if op == '+':
            total += sum(horizontal_values[i])
        else:
            total += prod(horizontal_values[i])
    return total

def part2(values: list[str], operators: list[str], col_indexes: list[int]) -> int:
    total = 0
    vertical_values = get_vertical_values(values, col_indexes)

    for i, op in enumerate(reversed(operators)):
        if op == '+':
            total += sum(vertical_values[i])
        else:
            total += prod(vertical_values[i])
    return total

values = []

with open("input.txt") as f:
    for current in f:
        if re.search(r"[\d]", current):
            values += [current.replace("\n", "")]
        else:
            operators = current

col_indexes = get_column_indexes(operators)
operators = operators.split()
print(part1(values, operators, col_indexes))
print(part2(values, operators, col_indexes))