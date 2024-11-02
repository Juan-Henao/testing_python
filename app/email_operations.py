""" asd """


def validate_email(email: str) -> bool:
    """ asd """

    return '@' in email and '.' in email.split('@')[1]


def obfuscate_email(email: str) -> str:
    """ asd """

    username, domain = email.split('@')
    return username[0] + '*' * (len(username) - 1) + '@' + domain


def extract_domain(email: str) -> str:
    """ asd """

    return email.split('@')[1]


def is_gmail(email: str) -> bool:
    """ asd """

    return email.endswith('@gmail.com')


def is_company_email(email: str, company: str) -> bool:
    """ asd """

    return email.endswith(f'@{company}.com')
