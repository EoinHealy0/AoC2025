def count_surrounding(department: list[list[str]], row: int, col: int) -> int:
    rolls = 0

    for i in range(max(0, row - 1), min(len(department), row + 2)):
        for j in range(max(0, col - 1), min(len(department[i]), col + 2)):
            if (i, j) != (row, col) and department[i][j] == "@":
                rolls += 1
    return rolls

def part1(department: list[list[str]], remove: bool = False) -> int:
    removable_rolls = 0

    for i in range(len(department)):
        for j in range(len(department[i])):
            if department[i][j] == "@" and count_surrounding(department, i, j) < 4:
                if remove == True:
                    department[i][j] = "x"
                removable_rolls += 1
    return removable_rolls

def part2(department: list[list[str]]) -> int:
    removed_rolls = 0
    
    while True:
        changes_made = part1(department, True)     
        if changes_made == 0:
            break      
        removed_rolls += changes_made
    return removed_rolls

with open("input.txt") as f:
    input = [list(line.strip()) for line in f]

print(part1(input))
print(part2(input))