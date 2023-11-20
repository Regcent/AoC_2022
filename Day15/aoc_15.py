import time
from typing import Union
from queue import PriorityQueue

class Node:
    
    def __init__(self, position, score, distance):
        self.position = position
        self.score = score
        self.distance = distance

    def __lt__(self, other):
        if self.score + self.distance < other.score + other.distance :
            return True
        elif self.distance < other.distance:
            return True
        else:
            return False

def run_script(filepath: str) -> Union[int, str, float, bool]:
    with open(filepath, "r") as f:
        raw_data = f.read()
    return main_function(raw_data)

def main_function(raw_data: str) -> Union[int, str, float, bool]:
    start_time = time.time()
    
    result = your_script(raw_data)

    elapsed_time = time.time() - start_time
    print(f"Time elapsed : {elapsed_time}s")
    return result

def your_script(raw_data: str) -> Union[int, str, float, bool]:
    map = []
    for str_line in raw_data.split("\n"):
        new_line = [int(i) for i in str_line]
        map.append(new_line)
    best_path = a_star((0, 0), (len(map) - 1, len(map[0]) - 1), map)
    print(f"Part 1: {best_path.score}")
    part_2_map = create_part_2_map(map)
    """str_lines = []
    for line in part_2_map:
        str_lines.append("".join([str(i) for i in line]))
    print("\n".join(str_lines))
    """
    best_path = a_star((0, 0), (len(part_2_map) - 1, len(part_2_map[0]) - 1), part_2_map)
    print(f"Part 2: {best_path.score}")
    return 0

def create_part_2_map(map: list) -> list:
    new_map = []
    for y in range(len(map) * 5):
        line = []
        for x in range(len(map) * 5):
            new_val = map[y % len(map)][x % len(map)] + x // len(map) + y // len(map)
            if new_val > 9:
                new_val -= 9
            line.append(new_val)
        new_map.append(list(line))
    return new_map


def a_star(start: tuple, end: tuple, map: list) -> Node:
    start_node = Node(start, 0, distance(start, end))
    pq = PriorityQueue()
    pq.put((0, start_node))
    visited = []
    while not pq.empty():
        current_node = pq.get()
        current_node = current_node[1]
        if current_node not in visited:
            visited.append(current_node.position)
        if current_node.position == end:
            return current_node
        for neighbor in get_neighbors(current_node.position, map):
            if neighbor in visited:
                continue
            new_node = Node(neighbor, current_node.score + get_score(neighbor, map), distance(neighbor, end))
            pq.put((new_node.score + new_node.distance, new_node))

def get_neighbors(pos: tuple, map: list) -> list:
    neighbors = []
    if pos[0] > 0:
        neighbors.append((pos[0] - 1, pos[1]))
    if pos[0] < len(map[0]) - 1:
        neighbors.append((pos[0] + 1, pos[1]))
    if pos[1] > 0:
        neighbors.append((pos[0], pos[1] - 1))
    if pos[1] < len(map) - 1:
        neighbors.append((pos[0], pos[1] + 1))
    return neighbors

def distance(start: tuple, end: tuple) -> int:
    return abs(end[1] - start[1]) + abs(end[0] - start[0])

def get_score(pos: tuple, map: list) -> int:
    return map[pos[1]][pos[0]]

if __name__ == "__main__":
    print(run_script("input.txt"))