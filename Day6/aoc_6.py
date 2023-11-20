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
    print(f"Part 1: {detect_different(raw_data, 4)}")
    print(f"Part 1: {detect_different(raw_data, 14)}")


def detect_different(raw_data: str, number: int):
    l = list(raw_data[:number])
    curr_pos = number
    while True:
        if len(set(l)) < number:
            l.pop(0)
            l.append(raw_data[curr_pos])
            curr_pos += 1
        else:
            break
    return curr_pos

if __name__ == "__main__":
    print(run_script("input.txt"))