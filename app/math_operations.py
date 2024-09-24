def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a: int, b: int) -> int:
    return a ** b

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n-1)