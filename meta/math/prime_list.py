import sympy
from ..config import *


__all__ = [
    "prime_list_code",
]


prime_upper_bound = 3000 if is_toy else 200000
prime_list = list(sympy.primerange(2, prime_upper_bound))
prime_list_length = len(prime_list)
prime_list_code = f"""const int prime_list[{prime_list_length}] = {{{", ".join(str(p) for p in prime_list)}}};
"""
