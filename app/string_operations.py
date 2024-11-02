""" asd """


def reverse_string(s: str) -> str:
    """ asd """

    return s[::-1]


def is_palindrome(s: str) -> bool:
    """ asd """

    return s == s[::-1]


def to_uppercase(s: str) -> str:
    """ asd """

    return s.upper()


def to_lowercase(s: str) -> str:
    """ asd """

    return s.lower()


def capitalize_words(s: str) -> str:
    """ asd """

    return " ".join([word.capitalize() for word in s.split()])


def count_vowels(s: str) -> int:
    """ asd """

    return sum(1 for char in s.lower() if char in 'aeiou')
