from ..config import is_toy


__all__ = [
    "big_int_declare",
    "big_int_release",
    "big_int_set",
    "big_int_add",
    "big_int_sub",
    "big_int_mul",
    "big_int_div",
    "big_int_mod",
    "big_int_gt",
    "big_int_ge",
    "big_int_eq",
    "big_int_le",
    "big_int_lt",
    "big_int_ne",
    "big_int_set_int",
    "big_int_add_int",
    "big_int_sub_int",
    "big_int_mul_int",
    "big_int_div_int",
    "big_int_mod_uint",
    "big_int_gt_int",
    "big_int_ge_int",
    "big_int_eq_int",
    "big_int_le_int",
    "big_int_lt_int",
    "big_int_ne_int",
    "big_int_export_to_int",
]


def big_int_declare(
    big_int: str,
    indent: int = 0,
)-> str:
    
    code: str = ""
    
    if is_toy:
        code += 4 * indent * " "
        code += f"int {big_int}; /* toy version big int declaration */"
    
    else:
        code += 4 * indent * " "
        code += f"mpz_t {big_int}; mpz_init({big_int});"
    
    return code


def big_int_release(
    big_int: str,
    indent: int = 0,
)-> str:
    
    code: str = ""
    
    if is_toy:
        code += 4 * indent * " "
        code += f"/* toy version big int resource release of {big_int} (do nothing) */"
    
    else:
        code += 4 * indent * " "
        code += f"mpz_clear({big_int});"
    
    return code


def big_int_set(
    dest_big_int: str,
    value_big_int: str,
    indent: int = 0,
)-> str:
    
    code: str = ""
    
    if is_toy:
        code += 4 * indent * " "
        code += f"{dest_big_int} = {value_big_int}; /* toy version big int assignment */"
    
    else:
        code += 4 * indent * " "
        code += f"mpz_set({dest_big_int}, {value_big_int});"
    
    return code


def big_int_add(
    res_big_int: str,
    lhs_big_int: str,
    rhs_big_int: str,
    indent: int = 0,
)-> str:
    
    code: str = ""
    
    if is_toy:
        code += 4 * indent * " "
        code += f"{res_big_int} = {lhs_big_int} + {rhs_big_int}; /* toy version big int operation */"
    
    else:
        code += 4 * indent * " "
        code += f"mpz_add({res_big_int}, {lhs_big_int}, {rhs_big_int});"
    
    return code


def big_int_sub(
    res_big_int: str,
    lhs_big_int: str,
    rhs_big_int: str,
    indent: int = 0,
)-> str:
    
    code: str = ""
    
    if is_toy:
        code += 4 * indent * " "
        code += f"{res_big_int} = {lhs_big_int} - {rhs_big_int}; /* toy version big int operation */"
    
    else:
        code += 4 * indent * " "
        code += f"mpz_sub({res_big_int}, {lhs_big_int}, {rhs_big_int});"
    
    return code


def big_int_mul(
    res_big_int: str,
    lhs_big_int: str,
    rhs_big_int: str,
    indent: int = 0,
)-> str:
    
    code: str = ""
    
    if is_toy:
        code += 4 * indent * " "
        code += f"{res_big_int} = {lhs_big_int} * {rhs_big_int}; /* toy version big int operation */"
    
    else:
        code += 4 * indent * " "
        code += f"mpz_mul({res_big_int}, {lhs_big_int}, {rhs_big_int});"
    
    return code


def big_int_div(
    res_big_int: str,
    lhs_big_int: str,
    rhs_big_int: str,
    indent: int = 0,
)-> str:
    
    code: str = ""
    
    if is_toy:
        code += 4 * indent * " "
        code += f"{res_big_int} = {lhs_big_int} / {rhs_big_int}; /* toy version big int operation */"
    
    else:
        code += 4 * indent * " "
        code += f"mpz_tdiv_q({res_big_int}, {lhs_big_int}, {rhs_big_int});"
    
    return code


def big_int_mod(
    res_big_int: str,
    lhs_big_int: str,
    rhs_big_int: str,
    indent: int = 0,
)-> str:
    
    code: str = ""
    
    if is_toy:
        code += 4 * indent * " "
        code += f"{res_big_int} = {lhs_big_int} % {rhs_big_int}; /* toy version big int operation */"
    
    else:
        code += 4 * indent * " "
        code += f"mpz_tdiv_r({res_big_int}, {lhs_big_int}, {rhs_big_int});"
    
    return code


def big_int_gt(
    lhs_big_int: str,
    rhs_big_int: str,
)-> str:
    
    code = ""
    
    if is_toy:
        code += f"({lhs_big_int} > {rhs_big_int} /* toy version big int comparison */ )"
    
    else:
        code += f"(mpz_cmp({lhs_big_int}, {rhs_big_int}) > 0)"
    
    return code


def big_int_ge(
    lhs_big_int: str,
    rhs_big_int: str,
)-> str:
    
    code = ""
    
    if is_toy:
        code += f"({lhs_big_int} >= {rhs_big_int} /* toy version big int comparison */ )"
    
    else:
        code += f"(mpz_cmp({lhs_big_int}, {rhs_big_int}) >= 0)"
    
    return code


def big_int_eq(
    lhs_big_int: str,
    rhs_big_int: str,
)-> str:
    
    code = ""
    
    if is_toy:
        code += f"({lhs_big_int} == {rhs_big_int} /* toy version big int comparison */ )"
    
    else:
        code += f"(mpz_cmp({lhs_big_int}, {rhs_big_int}) == 0)"
    
    return code


def big_int_le(
    lhs_big_int: str,
    rhs_big_int: str,
)-> str:
    
    code = ""
    
    if is_toy:
        code += f"({lhs_big_int} <= {rhs_big_int} /* toy version big int comparison */ )"
    
    else:
        code += f"(mpz_cmp({lhs_big_int}, {rhs_big_int}) <= 0)"
    
    return code


def big_int_lt(
    lhs_big_int: str,
    rhs_big_int: str,
)-> str:
    
    code = ""
    
    if is_toy:
        code += f"({lhs_big_int} < {rhs_big_int} /* toy version big int comparison */ )"
    
    else:
        code += f"(mpz_cmp({lhs_big_int}, {rhs_big_int}) < 0)"
    
    return code


def big_int_ne(
    lhs_big_int: str,
    rhs_big_int: str,
)-> str:
    
    code = ""
    
    if is_toy:
        code += f"({lhs_big_int} != {rhs_big_int} /* toy version big int comparison */ )"
    
    else:
        code += f"(mpz_cmp({lhs_big_int}, {rhs_big_int}) != 0)"
    
    return code


def big_int_set_int(
    dest_big_int: str,
    value_int: str,
    indent: int = 0,
)-> str:
    
    code: str = ""
    
    if is_toy:
        code += 4 * indent * " "
        code += f"{dest_big_int} = {value_int}; /* toy version big int assignment */"
    
    else:
        code += 4 * indent * " "
        code += f"mpz_set_si({dest_big_int}, {value_int});"
    
    return code


def big_int_add_int(
    res_big_int: str,
    lhs_big_int: str,
    rhs_int: str,
    indent: int = 0,
)-> str:
    
    code: str = ""
    
    if is_toy:
        code += 4 * indent * " "
        code += f"{res_big_int} = {lhs_big_int} + {rhs_int}; /* toy version big int operation */"
    
    else:
        code += 4 * indent * " "
        code += f"mpz_add_si({res_big_int}, {lhs_big_int}, {rhs_int});"
    
    return code


def big_int_sub_int(
    res_big_int: str,
    lhs_big_int: str,
    rhs_int: str,
    indent: int = 0,
)-> str:
    
    code: str = ""
    
    if is_toy:
        code += 4 * indent * " "
        code += f"{res_big_int} = {lhs_big_int} - {rhs_int}; /* toy version big int operation */"
    
    else:
        code += 4 * indent * " "
        code += f"mpz_sub_si({res_big_int}, {lhs_big_int}, {rhs_int});"
    
    return code


def big_int_mul_int(
    res_big_int: str,
    lhs_big_int: str,
    rhs_int: str,
    indent: int = 0,
)-> str:
    
    code: str = ""
    
    if is_toy:
        code += 4 * indent * " "
        code += f"{res_big_int} = {lhs_big_int} * {rhs_int}; /* toy version big int operation */"
    
    else:
        code += 4 * indent * " "
        code += f"mpz_mul_si({res_big_int}, {lhs_big_int}, {rhs_int});"
    
    return code


def big_int_div_int(
    res_big_int: str,
    lhs_big_int: str,
    rhs_int: str,
    indent: int = 0,
)-> str:
    
    code: str = ""
    
    if is_toy:
        code += 4 * indent * " "
        code += f"{res_big_int} = {lhs_big_int} / {rhs_int}; /* toy version big int operation */"
    
    else:
        code += 4 * indent * " "
        code += (
            f"if ({rhs_int} >= 0) {{"
            f"mpz_tdiv_q_ui({res_big_int}, {lhs_big_int}, (unsigned int) {rhs_int});"
            f"}}else {{"
            f"mpz_tdiv_q_ui({res_big_int}, {lhs_big_int}, (unsigned int) (-{rhs_int}));"
            f"mpz_neg({res_big_int}, {res_big_int});"
            f"}}"
        )
        
    return code


def big_int_mod_uint(
    res_big_int: str,
    lhs_big_int: str,
    rhs_uint: str,
    indent: int = 0,
)-> str:
    
    code: str = ""
    
    if is_toy:
        code += 4 * indent * " "
        code += f"{res_big_int} = {lhs_big_int} % {rhs_uint}; /* toy version big int operation */"
    
    else:
        code += 4 * indent * " "
        code += f"mpz_tdiv_r_ui({res_big_int}, {lhs_big_int}, (unsigned int) ({rhs_uint}));"
    
    return code


def big_int_gt_int(
    lhs_big_int: str,
    rhs_int: str,
)-> str:
    
    code = ""
    
    if is_toy:
        code += f"({lhs_big_int} > {rhs_int} /* toy version big int comparison */ )"
    
    else:
        code += f"(mpz_cmp_si({lhs_big_int}, {rhs_int}) > 0)"
    
    return code


def big_int_ge_int(
    lhs_big_int: str,
    rhs_int: str,
)-> str:
    
    code = ""
    
    if is_toy:
        code += f"({lhs_big_int} >= {rhs_int} /* toy version big int comparison */ )"
    
    else:
        code += f"(mpz_cmp_si({lhs_big_int}, {rhs_int}) >= 0)"
    
    return code


def big_int_eq_int(
    lhs_big_int: str,
    rhs_int: str,
)-> str:
    
    code = ""
    
    if is_toy:
        code += f"({lhs_big_int} == {rhs_int}) /* toy version big int comparison */ "
    
    else:
        code += f"(mpz_cmp_si({lhs_big_int}, {rhs_int}) == 0)"
    
    return code


def big_int_le_int(
    lhs_big_int: str,
    rhs_int: str,
)-> str:
    
    code = ""
    
    if is_toy:
        code += f"({lhs_big_int} <= {rhs_int} /* toy version big int comparison */ )"
    
    else:
        code += f"(mpz_cmp_si({lhs_big_int}, {rhs_int}) <= 0)"
    
    return code


def big_int_lt_int(
    lhs_big_int: str,
    rhs_int: str,
)-> str:
    
    code = ""
    
    if is_toy:
        code += f"({lhs_big_int} < {rhs_int}) /* toy version big int comparison */ "
    
    else:
        code += f"(mpz_cmp_si({lhs_big_int}, {rhs_int}) < 0)"
    
    return code


def big_int_ne_int(
    lhs_big_int: str,
    rhs_int: str,
)-> str:
    
    code = ""
    
    if is_toy:
        code += f"({lhs_big_int} != {rhs_int}) /* toy version big int comparison */ "
    
    else:
        code += f"(mpz_cmp_si({lhs_big_int}, {rhs_int}) != 0)"
    
    return code


def big_int_export_to_int(
    dest_int: str,
    value_big_int: str,
    indent: int = 0,
)-> str:
    
    code: str = ""
    
    if is_toy:
        code += 4 * indent * " "
        code += f"{dest_int} = {value_big_int}; /* toy version big int export */"
    
    else:
        code += 4 * indent * " "
        code += f"{dest_int} = (int) mpz_get_si({value_big_int});"
    
    return code