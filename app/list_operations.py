def find_max(lst: list) -> int:
    return max(lst)

def find_min(lst: list) -> int:
    return min(lst)

def sum_list(lst: list) -> int:
    return sum(lst)

def product_list(lst: list) -> int:
    result = 1
    for num in lst:
        result *= num
    return result

def sort_list(lst: list) -> list:
    return sorted(lst)

def reverse_list(lst: list) -> list:
    return lst[::-1]
