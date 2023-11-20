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
    parts = raw_data.split("\n\n")
    algorithm = [True if c == "#" else False for c in parts[0]]
    image = []
    for line in parts[1].split("\n"):
        for c in line:
            if c != "#" and c != ".":
                print("ISSUE")
        image.append([True if c == "#" else False for c in line])
    for count in range(2):
        image = add_borders(image, count, algorithm)
        image = create_new_image(image, algorithm)
    print(f"Part 1: {count_light_pixels(image)}")
    for count in range(48):
        image = add_borders(image, count, algorithm)
        image = create_new_image(image, algorithm)
    print(f"Part 2: {count_light_pixels(image)}")

def count_light_pixels(image: list) -> int:
    light_pixels = 0
    for y in range(len(image)):
        for x in range(len(image[0])):
            if image[y][x]:
                light_pixels += 1
    return light_pixels

def add_borders(image: list, count: int, algorithm: list) -> list:
    new_image = []
    padding = False
    if algorithm[0] == True and count % 2 == 1:
        padding = True
    new_image.append([padding] * (len(image[0]) + 4))
    new_image.append([padding] * (len(image[0]) + 4))
    for line in image:
        new_image.append([padding, padding] + line + [padding, padding])
    new_image.append([padding] * (len(image[0]) + 4))
    new_image.append([padding] * (len(image[0]) + 4))  
    return new_image

def create_new_image(image: list, algorithm: list) -> list:
    new_image = []
    for y in range(1, len(image) - 1):
        line = []
        for x in range(1, len(image[0]) - 1):
            line.append(get_pixel(image, algorithm, x, y))
        new_image.append(list(line))
    return new_image

def get_pixel(image: list, algorithm: list, x: int, y: int) -> bool:
    total = 0
    if image[y - 1][x - 1]:
        total += 256
    if image[y - 1][x]:
        total += 128
    if image[y - 1][x + 1]:
        total += 64
    if image[y][x - 1]:
        total += 32
    if image[y][x]:
        total += 16
    if image[y][x + 1]:
        total += 8
    if image[y + 1][x - 1]:
        total += 4
    if image[y + 1][x]:
        total += 2
    if image[y + 1][x + 1]:
        total += 1
    return algorithm[total]

if __name__ == "__main__":
    print(run_script("input.txt"))