import math

def area_of_circle(radius: float) -> float:
    return math.pi * radius ** 2

def circumference_of_circle(radius: float) -> float:
    return 2 * math.pi * radius

def area_of_rectangle(length: float, width: float) -> float:
    return length * width

def perimeter_of_rectangle(length: float, width: float) -> float:
    return 2 * (length + width)

def area_of_triangle(base: float, height: float) -> float:
    return 0.5 * base * height

def volume_of_cube(side: float) -> float:
    return side ** 3
