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
    rows = raw_data.split("\n")
    grid = []
    for row in rows:
        grid.append([int(i) for i in row])
    neighbors = prepare_neighbors(grid)
    flashes_count = 0
    for i in range(100):
        flashes = []
        next_turn(grid, neighbors, flashes)
        flashes_count += len(flashes)
        if len(flashes) == len(grid) * len(grid):
            print(f"Part 2: {i}")
    print(f"Part 1: {flashes_count}")
    idx = 100
    while True:
        idx += 1
        flashes = []
        next_turn(grid, neighbors, flashes)
        if len(flashes) == len(grid) * len(grid):
            print(f"Part 2: {idx}")
            break


def prepare_neighbors(grid: list) -> list:
    neighbors = []
    for y in range(len(grid)):
        row = []
        for x in range(len(grid)):
            local = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
            to_remove = []
            for coord in local:
                if coord[0] < 0 or coord[0] >= len(grid):
                    to_remove.append(coord)
                    continue
                if coord[1] < 0 or coord[1] >= len(grid):
                    to_remove.append(coord)
            for coord in to_remove:
                local.remove(coord)
            row.append(list(local))
        neighbors.append(list(row))
    return neighbors

def next_turn(grid: list, neighbors: list, flashes: list) -> int:
    for y in range(len(grid)):
        for x in range(len(grid)):
            if (x, y) in flashes:
                continue
            grid[y][x] += 1
            if grid[y][x] == 10:
                flashes.append((x, y))
                grid[y][x] = 0
                flash_neighbors(grid, neighbors, flashes, x, y)

def flash_neighbors(grid: list, neighbors: list, flashes: list, x: int, y: int):
    for coord in neighbors[y][x]:
        if coord in flashes:
            continue
        grid[coord[1]][coord[0]] += 1
        if grid[coord[1]][coord[0]] == 10:
            flashes.append(coord)
            grid[coord[1]][coord[0]] = 0
            flash_neighbors(grid, neighbors, flashes, coord[0], coord[1])
                
if __name__ == "__main__":
    print(run_script("input.txt"))