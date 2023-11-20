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
    elves = raw_data.split("\n\n")
    calories = []
    for elf in elves:
        elf_cal = sum([int(i) for i in elf.split("\n")])
        calories.append(elf_cal)
    print(f"Part 1: {max(calories)}")
    print(sorted(calories))
    print(f"Part 2: {sum(sorted(calories)[-3:])}")

if __name__ == "__main__":
    print(run_script("input.txt"))