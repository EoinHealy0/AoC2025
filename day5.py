def count_fresh(ranges: list[tuple]) -> int:
    fresh = 0

    for r in ranges:
        fresh += r[1] - r[0] + 1

    return fresh

def part1(ranges: list[tuple], ids: list[int]) -> int:
    count = 0

    for ingredient in ids:
        for r in ranges:
            if r[0] > ingredient:
                break
            if ingredient <= r[1]:
                count += 1
                break

    return count

def part2(ranges: list[tuple]) -> int:
    merged_ranges = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged_ranges[-1]

        if start <= last_end:
            merged_ranges[-1] = (last_start, max(last_end, end))
        else:
            merged_ranges.append((start, end))

    return count_fresh(merged_ranges)

with open("input.txt") as f:
    ranges = []

    while True:
        current = f.readline().strip()
        if not current:
            break
        else:
            ranges.append(tuple(map(int, current.split("-"))))

    ranges = sorted(ranges, key=lambda x: x[0]) # Sorting simplifies part2 merging significantly
    ids = [int(line.strip()) for line in f]

print(part1(ranges, ids))
print(part2(ranges))