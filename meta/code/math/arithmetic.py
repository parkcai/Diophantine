from meta.SysY.printf import *


__all__ = [
    "greatest_common_divisor_code",
    "least_common_multiple_code",
    "get_power_cycle_mod_code",
    "get_power_position_mod_code",
    "is_prime_code",
    "power_code",
    "contain_undividable_prime_part_code",
    "get_power_times_over_code",
    "get_degree_wrt_code",
    "is_power_of_code",
    "get_value_mod_code",
]


greatest_common_divisor_code = f"""int greatest_common_divisor(int n, int m) {{
{make_assertion("n >= 1 && m >= 1", "Invalid input of greatest_common_divisor!", 1, True)}
    int temp;
    while (m != 0) {{
        temp = m;
        m = n % m;
        n = temp;
    }}
    return n;
}}
"""


least_common_multiple_code = f"""int least_common_multiple(int n, int m) {{
{make_assertion("n >= 1 && m >= 1", "Invalid input of least_common_multiple!", 1, True)}
    int d = greatest_common_divisor(n, m);
    return n * (m / d);
}}
"""


get_power_cycle_mod_code = f"""int get_power_cycle_mod(int n, int m) {{
{make_assertion("n >= 2 && m >= 1", "Invalid input of get_power_cycle_mod!", 1, True)}
{make_assertion("greatest_common_divisor(n,m) == 1", "Invalid input of get_power_cycle_mod!", 1, True)}
    m = m % n;
    int m0 = m;
    if (m == 1) return 1;
    int result = 1;
    while (m != 1) {{
        m = (m * m0) % n;
        result = result + 1;
    }}
    return result;
}}
"""


get_power_position_mod_code = f"""int get_power_position_mod(int n, int m, int k) {{
{make_assertion("n >= 2 && m >= 1 && k >= 0", "Invalid input of get_power_position_mod!", 1, True)}
{make_assertion("greatest_common_divisor(n,m) == 1", "Invalid input of get_power_position_mod!", 1, True)}
    k = k % n;
    if (k == 1) return 0;
    m = m % n;
    int m0 = m;
    int result = 1;
    while (m != 1) {{
        if (k == m) return result;
        m = (m * m0) % n;
        result = result + 1;
    }}
    return -1;
}}
"""


is_prime_code = f"""int is_prime(int n) {{
{make_assertion("n >= 1", "Invalid input of is_prime!", 1, True)}
    if (n == 1) return 0;
    if (n <= 3) return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;
    int i = 5;
    while (i * i <= n) {{
        if (n % i == 0 || n % (i + 2) == 0) {{
            return 0; 
        }}
        i = i + 6;
    }}
    return 1; 
}}
"""


power_code = f"""int power(int base, int exp, int mod) {{
{make_assertion("base >= 1 && exp >= 0 && (mod >= 2 || mod == -1)", "Invalid input of power!", 1, True)}
    int res = 1, i = 0;
    while (i < exp) {{
        if (res < 2147483647 / base) {{
            res = res * base;
        }}else{{
{make_assertion("0", "[Runtime Error] function power encounters an int32 overflow!", 3, True)}
        }}
        if (mod != -1) {{
            res = res % mod;
        }}
        i = i + 1;
    }}
    return res;
}}
"""


contain_undividable_prime_part_code = f"""int contain_undividable_prime_part(int d, int x) {{
{make_assertion("d >= 1 && x >= 1", "Invalid input of contain_undividable_prime_part!", 1, True)}
    int i = 2;
    while (i <= d) {{
        if (d % i == 0 && is_prime(i)) {{
            if (x % i != 0) {{
                return 1; 
            }}
        }}
        i = i + 1;
    }}
    return 0; 
}}
"""


get_power_times_over_code = f"""int get_power_times_over(int M, int a){{
{make_assertion("a >= 2 && M >= 1", "Invalid input of get_power_times_over!", 1, True)}
    int n = 1, a0 = a;
    while (a <= M) {{
        a = a * a0;
        n = n + 1;
    }}
    return n;
}}
"""


get_degree_wrt_code = f"""int get_degree_wrt(int p, int N) {{
    int res = 0;
    while (N % p == 0) {{
        N = N / p;
        res = res + 1;
    }}
    return res;
}}
"""


is_power_of_code = f"""int is_power_of(int a, int b) {{
    if (a == 0) {{
        return (b == 0) || (b == 1);
    }}else if (a == 1) {{
        return b == 1;
    }}else if (a >= 2) {{
        if (b <= 0) return 0;
        int n = get_power_times_over(b, a) - 1;
        return power(a, n, -1) == b;
    }}else{{
        if (!b) return 0;
        int abs_a = -a;
        int abs_b = b;
        if (b < 0) abs_b = -b;
        int n = get_power_times_over(abs_b, abs_a) - 1;
        return power(abs_a, n, -1) == abs_b && ((b > 0 && n % 2 == 0) || (b < 0 && n % 2));
    }}
}}
"""


get_value_mod_code = f"""int get_value_mod(int M, int N) {{
    while (N < 0) N = N + M;
    return N % M;
}}
"""