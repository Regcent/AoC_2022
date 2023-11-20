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
    positions = [int(i) for i in raw_data.split(",")]
    min_pos = min(positions)
    max_pos = max(positions)
    min_fuel = 1000000
    for tentative in range(min_pos, max_pos + 1):
        total = 0
        for pos in positions:
            total += abs(tentative - pos)
        if total < min_fuel:
            min_fuel = total
    print(f"Part 1 : {min_fuel}")
    min_fuel = 1000000000
    for tentative in range(min_pos, max_pos + 1):
        total = 0
        for pos in positions:
            n = abs(tentative - pos) 
            total += int(n * (n + 1) / 2)
        if total < min_fuel:
            min_fuel = total
    print(f"Part 2: {min_fuel}")

if __name__ == "__main__":
    print(run_script("input.txt"))