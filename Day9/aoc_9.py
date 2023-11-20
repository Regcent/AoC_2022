import time
from typing import Union

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
    points = []
    rows = raw_data.split("\n")
    for row in rows:
        points.append([int(i) for i in row])
    lowest = find_lowest_points(points)
    print(lowest)
    total_risk = 0
    for position in lowest:
        total_risk += 1 + points[position[1]][position[0]]
    print(f"Part 1: {total_risk}")
    # TODO : Filling algorithm, mark cells already visited and when meeting a 9, just stop
    return 0

def find_lowest_points(points: list) -> list:
    lowest = []
    for y in range(len(points)):
        for x in range(len(points[0])):
            if is_lowest(points, x, y):
                lowest.append((x, y))
    return lowest

def is_lowest(points: list, x: int, y: int):
    if x > 0:
        if points[y][x] >= points[y][x - 1]:
            return False
    if x < len(points[0]) - 1:
        if points[y][x] >= points[y][x + 1]:
            return False
    if y > 0:
        if points[y][x] >= points[y - 1][x]:
            return False
    if y < len(points) - 1:
        if points[y][x] >= points[y + 1][x]:
            return False
    return True

if __name__ == "__main__":
    print(run_script("input.txt"))