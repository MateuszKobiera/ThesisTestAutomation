import random
import string


def create_random_string(number_of_characters: int) -> str:
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(number_of_characters))
