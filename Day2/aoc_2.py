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
    print(f"Part 1 : {part_1(raw_data)}")
    print(f"Part 2 : {part_2(raw_data)}")

def part_1(raw_data: str) -> int:
    rounds = raw_data.split("\n")
    total_p1, total_p2 = 0, 0
    for turn in rounds:
        p1, p2 = turn.split()
        p1 = resolve_symbol(p1)
        p2 = resolve_symbol(p2)
        p1, p2 = resolve_round(p1, p2)
        total_p1 += p1
        total_p2 += p2
    return total_p2

def part_2(raw_data: str) -> int:
    rounds = raw_data.split("\n")
    total_p1, total_p2 = 0, 0
    for turn in rounds:
        p1, p2 = turn.split()
        p1 = resolve_symbol(p1)
        score = resolve_round_2(p1, p2)
        total_p2 += score
    return total_p2

def resolve_symbol(symbol: str) -> int:
    if symbol in "AX":
        return 1
    elif symbol in "BY":
        return 2
    else:
        return 3

def resolve_round(p1: int, p2: int):
    if p1 == p2:
        p1 += 3
        p2 += 3
    elif p1 == 1:
        if p2 == 2:
            p2 += 6
        else:
            p1 += 6
    elif p1 == 2:
        if p2 == 3:
            p2 += 6
        else:
            p1 += 6
    else:
        if p2 == 1:
            p2 += 6
        else:
            p1 += 6
    return p1, p2

def resolve_round_2(p1: int, p2: str) -> int:
    if p2 == "Z":
        if p1 == 1:
            return 6 + 2
        elif p1 == 2:
            return 6 + 3
        else:
            return 6 + 1
    elif p2 == "Y":
        return 3 + p1
    else:
        if p1 == 1:
            return 3
        elif p1 == 2:
            return 1
        else:
            return 2

if __name__ == "__main__":
    print(run_script("example.txt"))
    print(run_script("input.txt"))