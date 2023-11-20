import time
from typing import Union

class Node:

    def __init__(self, path: list, position: str, double: bool):
        self.path = list(path)
        self.path.append(position)
        self.double = double

    def __str__(self):
        print(self.path)

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
    links = raw_data.split("\n")
    big = {}
    small = {}
    for link in links:
        a, b = link.split("-")
        add_to_caves(a, b, big, small)
        add_to_caves(b, a, big, small)
    #print(big)
    #print(small)
    paths = find_all_paths("start", "end", big, small)
    print(len(paths))

def add_to_caves(start: str, end: str, big: dict, small: dict) -> None:
    if start.isupper():
        if start not in big:
            big[start] =  [end]
        else:
            big[start].append(end)
    else:
        if start not in small:
            small[start] = [end]
        else:
            small[start].append(end)

def find_all_paths(start: str, end: str, big: dict, small: dict) -> list:
    potential = [Node([], start, False)]
    paths = []
    while len(potential) != 0:
        current = potential.pop()
        position = current.path[-1]
        if position.isupper():
            for cave in big[position]:
                if cave == end:
                    paths.append(Node(current.path, end, current.double))
                else:
                    if cave.islower() and cave in current.path and current.double:
                        continue
                    if cave == "start":
                        continue
                    if cave in current.path and cave.islower():
                        potential.append(Node(current.path, cave, True))
                    else:
                        potential.append(Node(current.path, cave, current.double))
        else:
            for cave in small[position]:
                if cave == end:
                    paths.append(Node(current.path, end, current.double))
                else:
                    if cave.islower() and cave in current.path and current.double:
                        continue
                    if cave == "start":
                        continue
                    if cave in current.path and cave.islower():
                        potential.append(Node(current.path, cave, True))
                    else:
                        potential.append(Node(current.path, cave, current.double))
    return paths

if __name__ == "__main__":
    print(run_script("input.txt"))