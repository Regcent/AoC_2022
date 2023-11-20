import time
from typing import Union
import re

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
    on = set()
    for command in raw_data.split('\n'):
        vals = [int(i) for i in re.findall("-?\d+", command)]
        x0 = min(vals[0], vals[1])
        x1 = max(vals[0], vals[1])
        y0 = min(vals[2], vals[3])
        y1 = max(vals[2], vals[3])
        z0 = min(vals[4], vals[5])
        z1 = max(vals[4], vals[5])
        turn_on = "n" == command[1]
        print(turn_on)
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                for z in range(z0, z1 + 1):
                    if turn_on:
                        on.add((x, y, z))
                    else:
                        if (x, y , z) in on:
                            on.remove((x, y, z))
    return len(on)

if __name__ == "__main__":
    print(run_script("input.txt"))