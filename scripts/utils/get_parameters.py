from typing import Tuple
from .interaction import get_boolean_input
from .interaction import get_integer_input


__all__ = [
    "get_diophantine_parameters",
]


def get_diophantine_parameters(
)-> Tuple[int, int, int, int, int, int, int, int, bool]:
    
    print("Please enter parameter values for diophantine (press Enter to use the default):")
    a_max = get_integer_input("a_max", 500)
    a_min = get_integer_input("a_min", 2)
    b_max = get_integer_input("b_max", 500)
    b_min = get_integer_input("b_min", 1)
    c_max = get_integer_input("c_max", 500)
    c_min = get_integer_input("c_min", 2)
    a_start = get_integer_input("a_start", a_min)
    b_start = get_integer_input("b_start", b_min)
    exclude_trivial = get_boolean_input("exclude_trivial", True)
    
    return a_max, a_min, b_max, b_min, c_max, c_min, a_start, b_start, exclude_trivial