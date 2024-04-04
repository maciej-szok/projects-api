import random
import string


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def dict_is_subset(subset: dict, superset: dict) -> bool:
    return subset.items() >= superset.items()
