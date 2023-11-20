import time
from typing import Union
from dataclasses import dataclass
from copy import deepcopy
from itertools import combinations

@dataclass
class Valve:
    name: str
    pressure: int
    doors: list
    distance: dict

    def __str__(self):
        return f"{self.name} : Pressure {self.pressure}, Doors {self.doors}"

@dataclass
class DistanceNode:
    position: str
    previous: list

@dataclass
class SimulationNode:
    position: str
    not_opened: list
    total_pressure: int
    current_time: int

def run_script(filepath: str) -> Union[int, str, float, bool]:
    with open(filepath, "r") as f:
        raw_data = f.read()
    return main_function(raw_data)

def main_function(raw_data: str) -> Union[int, str, float, bool]:
    start_time = time.time()
    [1]
    result = your_script(raw_data)

    elapsed_time = time.time() - start_time
    print(f"Time elapsed : {elapsed_time}s")
    return result

def your_script(raw_data: str) -> Union[int, str, float, bool]:
    """
    Time to code! Write your code here to solve today's problem
    """
    lines = raw_data.split("\n")
    valves_with_pressure = ["AA"]
    valves = dict()
    for line in lines:
        line_data = line.split()
        name = line_data[1]
        rate = int(line_data[4].split("=")[1][:-1])
        doors = [door[:2] for door in line_data[9:]]
        valves[name] = Valve(name, rate, doors, {})
        if rate > 0:
            valves_with_pressure.append(name)
    fill_distances(valves, valves_with_pressure)
    valves_with_pressure.remove("AA")
    print(f"Part 1: {find_best(valves, valves_with_pressure, 30)}")   
    print(f"Part 2: {part_2(valves, valves_with_pressure)}")

def fill_distances(valves: dict, valves_with_pressure: list):
    targets = deepcopy(valves_with_pressure)
    for src in valves_with_pressure:
        targets.remove(src)
        calculate_distances(valves, src, targets)

def calculate_distances(valves: dict, src: str, targets: list):
    not_found = deepcopy(targets)
    elements = [DistanceNode(src, [src])]
    while not_found and elements:
        current = elements.pop(0)
        for door in valves[current.position].doors:
            if door in current.previous:
                continue
            if door in not_found:
                valves[src].distance[door] = len(current.previous)
                valves[door].distance[src] = len(current.previous)
                not_found.remove(door)
            elements.append(DistanceNode(door, current.previous + [door]))
    
def find_best(valves: dict, valves_to_open: list, max_time: int):
    variants = [SimulationNode("AA", valves_to_open, 0, 0)]
    maximum_pressure = 0
    while variants:
        curr = variants.pop(0)
        not_opened = curr.not_opened
        finished = True
        for valve in not_opened:
            dist = valves[curr.position].distance[valve]
            if curr.current_time + dist >= max_time:
                continue
            new_not_opened = list()
            for other in not_opened:
                if other == valve:
                    continue
                new_not_opened.append(other)
            added_pressure = ((max_time - curr.current_time) - dist - 1) * valves[valve].pressure
            variants.append(SimulationNode(valve, 
                                           new_not_opened,
                                           curr.total_pressure + added_pressure,
                                           curr.current_time + dist + 1))
            finished = False
        if finished:
            if curr.total_pressure > maximum_pressure:
                maximum_pressure = curr.total_pressure
    return maximum_pressure

def part_2(valves: dict, valves_with_pressure: list):
    limit = len(valves_with_pressure) // 2 + 1
    valves_with_pressure.sort()
    variants = [(valves_with_pressure, [])]
    best = 0
    while variants:
        curr = variants.pop(0)
        pressure = find_best(valves, curr[0], 26) + find_best(valves, curr[1], 26)
        if pressure > best:
            best = pressure
        for valve in curr[0]:
            new_self = list()
            new_elephant = curr[1] + [valve]
            for other in curr[0]:
                if other == valve:
                    continue
                new_self.append(other)
            if len(new_elephant) >= limit:
                continue
            new_self.sort()
            new_elephant.sort()
            if (new_self, new_elephant) not in variants:
                variants.append((new_self, new_elephant))
    return best

if __name__ == "__main__":
    print(run_script("input.txt"))