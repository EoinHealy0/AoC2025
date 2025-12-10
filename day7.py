def check_for_splitter(row: list[str], index: int) -> bool:
    if row[index] == "^":
        return True
    return False

def part1(input: list[list[str]], start: int) -> int:
    beams = [{start}]
    splits = 0
    
    for i in range(1, len(input) - 1):
        beams.append(set())

        for b in beams[i - 1]:
            if check_for_splitter(input[i + 1], b):
                beams[i].add(b - 1)
                beams[i].add(b + 1)
                splits += 1
            else:
                beams[i].add(b)
    return splits

def part2(input: list[list[str]], start: int) -> int:
    beams = [{start: 1}]
    
    for i in range(1, len(input) - 1):
        beams.append({})

        for b in beams[i - 1].keys():
            current_weight = beams[i - 1][b]
            
            if check_for_splitter(input[i + 1], b):
                if b - 1 in beams[i]:
                    beams[i][b - 1] += current_weight
                else:
                    beams[i][b - 1] = current_weight
                if b + 1 in beams[i]:
                    beams[i][b + 1] += current_weight
                else:
                    beams[i][b + 1] = current_weight
            else:
                if b in beams[i]:
                    beams[i][b] += current_weight
                else:
                    beams[i][b] = current_weight
    return sum(beams[len(beams) - 1].values())

with open("input.txt") as f:
    input = [list(line.strip()) for line in f]

start = input[0].index("S")
print(part1(input, start))
print(part2(input, start))
