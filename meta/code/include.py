from ..config import is_toy


__all__ = [
    "include_stdio_code",
]


include_stdio_code = "#include <stdio.h>" if is_toy else "#include <stdio.h>\n#include <stdint.h>"