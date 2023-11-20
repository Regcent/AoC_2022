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
    """
    Time to code! Write your code here to solve today's problem
    """
    rucksacks = raw_data.split("\n")
    priorities = []
    for sack in rucksacks:
        pocket1 = set(sack[:len(sack)//2])
        pocket2 = set(sack[len(sack)//2:])
        for item in pocket1:
            if item in pocket2:
                priorities.append(get_priority(item))
    print(f"Part 1: {sum(priorities)}")
    badges = []
    for i in range(len(rucksacks) // 3):
        pos = 3 * i
        sack1 = set(rucksacks[pos])
        sack2 = set(rucksacks[pos + 1])
        sack3 = set(rucksacks[pos + 2])
        for item in sack1:
            if item not in sack2:
                continue
            if item not in sack3:
                continue
            badges.append(get_priority(item))
            break
    print(f"Part 2: {sum(badges)}")

def get_priority(item: str) -> int:
    if item.isupper():
        return ord(item) - ord("A") + 27
    else:
        return ord(item) - ord("a") + 1

if __name__ == "__main__":
    print(run_script("input.txt"))