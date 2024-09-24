def reverse_string(s: str) -> str:
    return s[::-1]

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def to_uppercase(s: str) -> str:
    return s.upper()

def to_lowercase(s: str) -> str:
    return s.lower()

def capitalize_words(s: str) -> str:
    return " ".join([word.capitalize() for word in s.split()])

def count_vowels(s: str) -> int:
    return sum(1 for char in s.lower() if char in 'aeiou')
