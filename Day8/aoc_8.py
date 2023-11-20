import time
from typing import Union

# Might be kind of optimal, but inelegant as possible
# TODO : Try to clean that up when you have time, you approached it too bluntly at first...

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
    cases = raw_data.split("\n")
    total1478 = 0
    total = 0
    for case in cases:
        numbers = dict.fromkeys(list(range(10)))
        five_long = []
        six_long = []
        io = case.split(" | ")
        output = io[1].split(" ")
        for signal in output:
            if len(signal) == 2:
                total1478 += 1
            elif len(signal) == 3:
                total1478 += 1
            elif len(signal) == 4:
                total1478 += 1
            elif len(signal) == 7:
                total1478 += 1
        for signal in io[0].split(" "):
            if len(signal) == 2:
                numbers[1] = signal
            elif len(signal) == 3:
                numbers[7] = signal
            elif len(signal) == 4:
                numbers[4] = signal
            elif len(signal) == 5:
                five_long.append(signal)
            elif len(signal) == 6:
                six_long.append(signal)
            elif len(signal) == 7:
                numbers[8] = signal
        numbers[9] = find_nine(numbers, six_long)
        numbers[0] = find_zero(numbers, six_long)
        numbers[6] = find_six(numbers, six_long)
        numbers[3] = find_three(numbers, five_long)
        numbers[5] = find_five(numbers, five_long)
        numbers[2] = find_two(numbers, five_long)
        phrases = {}
        for i in range(10):
            phrases[numbers[i]] = str(i)
        final_number = ""
        for signal in output:
            possible = phrases.keys()
            key = ""
            for p in possible:
                wrong = False
                if len(signal) != len(p):
                    continue
                for char in signal:
                    if char not in p:
                        wrong = True
                        break
                if wrong:
                    continue
                key = p
                break
            final_number += phrases[key]
        total += int(final_number)
    print(f"Part 1: {total1478}")
    print(f"Part 2: {total}")

def find_nine(numbers: dict, six_long: list):
    for phrase in six_long:
        wrong = False
        for char in numbers[4]:
            if char not in phrase:
                wrong = True
                break
        if wrong:
            continue
        six_long.remove(phrase)
        return phrase

def find_zero(numbers: dict, six_long: list):
    for phrase in six_long:
        wrong = False
        for char in numbers[1]:
            if char not in phrase:
                wrong = True
                break
        if wrong: 
            continue
        six_long.remove(phrase)
        return phrase

def find_six(numbers: dict, six_long: list):
    return six_long[0]

def find_three(numbers: dict, five_long: list):
    for phrase in five_long:
        wrong = False
        for char in numbers[1]:
            if char not in phrase:
                wrong = True
                break
        if wrong:
            continue
        five_long.remove(phrase)
        return phrase

def find_five(numbers: dict, five_long: list):
    for phrase in five_long:
        wrong = False
        for char in phrase:
            if char not in numbers[6]:
                wrong = True
                break
        if wrong:
            continue
        five_long.remove(phrase)
        return phrase
        
def find_two(numbers: dict, five_long: list):
    return five_long[0]

if __name__ == "__main__":
    print(run_script("input.txt"))