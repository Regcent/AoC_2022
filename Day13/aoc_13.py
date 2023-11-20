import time
from typing import List, Union

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
    parts = raw_data.split("\n\n")
    points = parse_points(parts[0])
    folds = parse_folds(parts[1])
    points = fold(folds.pop(0), points)
    print(f"Part 1: {len(points)}")
    for fold_val in folds:
        points = fold(fold_val, points)
    max_x = 0
    max_y = 0
    for point in points:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]
    code = []
    for y in range(max_y + 1):
        line = ""
        for x in range(max_x + 1):
            if (x, y) in points:
                line += "##"
            else:
                line += "  "
        code.append(str(line))
    print("\n".join(code))

def fold(fold: tuple, points: list) -> list:
    if fold[0] != 0:
        return fold_x(fold[0], points)
    else:
        return fold_y(fold[1], points)

def fold_x(axis: int, points: list) -> list:
    print(f"Folding along x={axis}")
    new_points = []
    for point in points:
        if point[0] < axis:
            if point not in new_points:
                new_points.append(point)
        elif point[0] == axis:
            continue
        else:
            distance = point[0] - axis
            new_x = axis - distance
            new_point = (new_x, point[1])
            if new_point not in new_points:
                new_points.append(new_point)
    return new_points

def fold_y(axis: int, points: list) -> list:
    print(f"Folding along y={axis}")
    new_points = []
    for point in points:
        if point[1] < axis:
            if point not in new_points:
                new_points.append(point)
        elif point[1] == axis:
            continue
        else:
            distance = point[1] - axis
            new_y = axis - distance
            new_point = (point[0], new_y)
            if new_point not in new_points:
                new_points.append(new_point)
    return new_points

def parse_points(points_str: str) -> list:
    points = []
    for point_str in points_str.split("\n"):
        coord = [int(i) for i in point_str.split(",")]
        points.append((coord[0], coord[1]))
    return points

def parse_folds(folds_str: str) -> list:
    folds = []
    for fold_str in folds_str.split("\n"):
        instructions = fold_str.split("=")
        value = int(instructions[1])
        if "x" in instructions[0]:
            folds.append((value, 0))
        elif "y" in instructions[0]:
            folds.append((0, value))
        else:
            print(f"Strange issue, {instructions[0]}")
    return folds

if __name__ == "__main__":
    print(run_script("input.txt"))