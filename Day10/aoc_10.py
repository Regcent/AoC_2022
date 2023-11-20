import time
from typing import Union
from math import floor

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
    lines = raw_data.split("\n")
    invalid_characters = []
    incomplete_scores = []
    for line in lines:
        stack = []
        invalid = False
        for char in line:
            if char == "(":
                stack.append(char)
            elif char == "[":
                stack.append(char)
            elif char == "{":
                stack.append(char)
            elif char == "<":
                stack.append(char)
            elif char == ")":
                if stack.pop() != "(":
                    invalid_characters.append(char)
                    invalid = True
                    break
            elif char == "]":
                if stack.pop() != "[":
                    invalid_characters.append(char)
                    invalid = True
                    break
            elif char == "}":
                if stack.pop() != "{":
                    invalid_characters.append(char)
                    invalid = True
                    break
            elif char == ">":
                if stack.pop() != "<":
                    invalid_characters.append(char)
                    invalid = True
                    break
        if invalid:
            continue
        incomplete_scores.append(calculate_score(stack))
    calculate_part_1(invalid_characters)
    incomplete_scores.sort()
    print(len(incomplete_scores))
    print(f"Part 2: {incomplete_scores[floor((len(incomplete_scores) / 2))]}")

def calculate_score(stack: list) -> int:
    total = 0
    while len(stack) != 0:
        total *= 5
        last = stack.pop()
        if last == "(":
            total += 1
        elif last == "[":
            total += 2
        elif last == "{":
            total += 3
        elif last == "<":
            total += 4
    return total

def calculate_part_1(invalid_characters: list):
    total_part1 = 0
    for char in invalid_characters:
        if char == ")":
            total_part1 += 3
        if char == "]":
            total_part1 += 57
        if char == "}":
            total_part1 += 1197
        if char == ">":
            total_part1 += 25137
    print(f"Part 1: {total_part1}")

if __name__ == "__main__":
    print(run_script("input.txt"))