import random
import string


def get_user_id() -> int:
    return random.randint(1, 10000)


def get_user_name() -> str:
    return f"user{get_user_id()}"


def get_user_email(email: str) -> str:
    return f"{email}@example.com"


def check_user_password(input_pwd: str, password: str) -> bool:
    return input_pwd == password


def get_random_string(length: int) -> str:
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(length)
    )
