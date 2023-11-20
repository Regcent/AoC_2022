import time
from typing import Union
from copy import deepcopy

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
    pairs = raw_data.split("\n")
    full_overlapping_pairs = []
    for pair in pairs:
        elf1, elf2 = pair.split(",")
        elf1_min, elf1_max = [int(i) for i in elf1.split("-")]
        elf2_min, elf2_max = [int(i) for i in elf2.split("-")]
        if elf1_min <= elf2_min and elf1_max >= elf2_max:
            full_overlapping_pairs.append(pair)
            continue
        if elf2_min <= elf1_min and elf2_max >= elf1_max:
            full_overlapping_pairs.append(pair)
    print(f"Part 1: {len(full_overlapping_pairs)}")
    part_overlapping_pairs = []
    for pair in pairs:
        if pair in full_overlapping_pairs:
            continue
        elf1, elf2 = pair.split(",")
        elf1_min, elf1_max = [int(i) for i in elf1.split("-")]
        elf2_min, elf2_max = [int(i) for i in elf2.split("-")]
        if elf1_max < elf2_min:
            continue
        if elf1_min > elf2_max:
            continue
        part_overlapping_pairs.append(pair)
    print(f"Part 2: {len(full_overlapping_pairs)} + {len(part_overlapping_pairs)}")


if __name__ == "__main__":
    print(run_script("example.txt"))
    print(run_script("input.txt"))