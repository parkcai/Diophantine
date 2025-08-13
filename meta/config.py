from scripts.utils import get_boolean_input


__all__ = [
    "is_toy",
]


is_toy: bool = get_boolean_input("is_toy", False)