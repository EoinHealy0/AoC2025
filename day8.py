class Box:
    def __init__(self, x, y, z, index):
        self.index = index
        self.x = x
        self.y = y
        self.z = z

class Distance:
    def __init__(self, box1: Box, box2: Box, distance: float):
        self.box1 = box1
        self.box2 = box2
        self.distance = distance

def get_distance(box1: Box, box2: Box) -> float:
    return ((box2.x - box1.x) ** 2 + (box2.y - box1.y) ** 2 + (box2.z - box1.z) ** 2) ** 0.5

def get_all_distances(boxes: list[Box]) -> list[Distance]:
    finished_boxes = set()
    distances = []

    for b1 in boxes:
        finished_boxes.add(b1.index)

        for b2 in boxes:
            if b2.index not in finished_boxes:
                dist = get_distance(b1, b2)
                distances.append(Distance(b1, b2, dist))
    return distances

def find_sublist_index(circuits: list[list[int]], index: int) -> int:
    return next((i for i, c in enumerate(circuits) if index in c), -1)

def contains_single_full_circuit(circuits: list[list[int]], full_circuit: set[int]) -> bool:
    if len(circuits) != 1:
        return False
    elif len(circuits[0]) < len(full_circuit):
        return False
    return set(circuits[0]) == full_circuit

def part1(sorted_distances: list[Distance], connections: int) -> int:
    circuits = []

    for i in range(0, connections):
        index1 = find_sublist_index(circuits, sorted_distances[i].box1.index)
        index2 = find_sublist_index(circuits, sorted_distances[i].box2.index)

        if index1 == -1 == index2 == -1:
            circuits.append([sorted_distances[i].box1.index, sorted_distances[i].box2.index])
        elif index1 != -1 and index2 == -1:
            circuits[index1].append(sorted_distances[i].box2.index)
        elif index1 == -1 and index2 != -1:
            circuits[index2].append(sorted_distances[i].box1.index)
        elif index1 != index2:
            circuits[index1].extend(circuits[index2])
            circuits.pop(index2)

    circuits.sort(key = lambda c: len(c), reverse=True)
    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])

def part2(sorted_distances: list[Distance], num_boxes: int) -> int:
    circuits = []
    full_circuit = set(range(0, num_boxes))
    
    for d in sorted_distances:
        index1 = find_sublist_index(circuits, d.box1.index)
        index2 = find_sublist_index(circuits, d.box2.index)

        if index1 == -1 == index2 == -1:
            circuits.append([d.box1.index, d.box2.index])
        elif index1 != -1 and index2 == -1:
            circuits[index1].append(d.box2.index)
        elif index1 == -1 and index2 != -1:
            circuits[index2].append(d.box1.index)
        elif index1 != index2:
            circuits[index1].extend(circuits[index2])
            circuits.pop(index2)

        if contains_single_full_circuit(circuits, full_circuit):
            return d.box1.x * d.box2.x

    return None 

with open("input.txt") as f:
    points = [Box(*map(int, line.strip().split(",")), index=i) for i, line in enumerate(f)]

sorted_distances = sorted(get_all_distances(points), key=lambda d: d.distance)
print(part1(sorted_distances, 1000))
print(part2(sorted_distances, len(points)))