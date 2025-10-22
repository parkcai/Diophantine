from ..config import *
from ..SysY.printf import *
from ..big_int import *


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
    int res;
    {big_int_declare("RES")}
    {big_int_set_int("RES", "m / d")}
    {big_int_mul_int("RES", "RES", "n")}
    if ({big_int_gt_int("RES", "2147483647")} || {big_int_lt_int("RES", "-2147483648")}) {{
        {big_int_release("RES")}
        {make_assertion("0", "[Runtime Error] function least_common_multiple encounters an int32 overflow!", 2, True)}
    }}
    {big_int_export_to_int("res", "RES")}
    {big_int_release("RES")}
    return res;
}}
"""


_get_power_cycle_mod_code_naive = f"""int get_power_cycle_mod(int n, int m) {{
    {make_assertion("n >= 2 && m >= 1", "Invalid input of get_power_cycle_mod!", 1, True)}
    {make_assertion("greatest_common_divisor(n,m) == 1", "Invalid input of get_power_cycle_mod!", 1, True)}
    m = m % n; if (m == 1) return 1;
    int result = 1;
    {big_int_declare("M")}
    {big_int_set_int("M", "m")}
    while ({big_int_ne_int("M", "1")}) {{
        {big_int_mul_int("M", "M", "m")}
        {big_int_mod_uint("M", "M", "n")}
        result = result + 1;
    }}
    {big_int_release("M")}
    return result;
}}
"""


_get_power_cycle_mod_code_fast = f"""int _gcd(int a, int b) {{
    while (b) {{
        int t = b;
        b = a % b;
        a = t;
    }}
    return a;
}}


int _modpow(int base, int exp, int mod) {{
    uint64_t result = 1;
    uint64_t b = base % mod;
    while (exp > 0) {{
        if (exp & 1) result = (result * b) % mod;
        b = (b * b) % mod;
        exp >>= 1;
    }}
    return (int) result;
}}


int _euler_phi(int m) {{
    int result = m;
    for (int i = 2; i * i <= m; i++) {{
        if (m % i == 0) {{
            while (m % i == 0) m /= i;
            result -= result / i;
        }}
    }}
    if (m > 1) result -= result / m;
    return result;
}}


int _factorize(int n, int* primes, int max_factors) {{
    int cnt = 0;
    for (int i = 2; i * i <= n && cnt < max_factors; i++) {{
        if (n % i == 0) {{
            primes[cnt++] = i;
            while (n % i == 0) n /= i;
        }}
    }}
    if (n > 1 && cnt < max_factors) primes[cnt++] = n;
    return cnt;
}}


int get_power_cycle_mod(int n, int m) {{
    if (_gcd(m, n) != 1) return -1;

    int phi = _euler_phi(n);
    int factors[32];
    int nf = _factorize(phi, factors, 32);

    int order = phi;
    for (int i = 0; i < nf; i++) {{
        int p = factors[i];
        while (order % p == 0) {{
            if (_modpow(m, order / p, n) == 1) {{
                order /= p;
            }} else {{
                break;
            }}
        }}
    }}
    return order;
}}
"""


get_power_cycle_mod_code = _get_power_cycle_mod_code_naive \
    if is_toy else _get_power_cycle_mod_code_fast


_get_power_position_mod_code_naive = f"""int get_power_position_mod(int n, int m, int k) {{
    {make_assertion("n >= 2 && m >= 1 && k >= 0", "Invalid input of get_power_position_mod!", 1, True)}
    {make_assertion("greatest_common_divisor(n,m) == 1", "Invalid input of get_power_position_mod!", 1, True)}    
    k = k % n; if (k == 1) return 0;
    m = m % n;
    int result = 1;
    {big_int_declare("M")}
    {big_int_set_int("M", "m")}
    while ({big_int_ne_int("M", "1")}) {{
        if ({big_int_eq_int("M", "k")}) {{
            {big_int_release("M")}
            return result;
        }}
        {big_int_mul_int("M", "M", "m")}
        {big_int_mod_uint("M", "M", "n")}
        result = result + 1;
    }}
    {big_int_release("M")}
    return -1;
}}
"""


_get_power_position_mod_code_baby_giant_step = f"""#define MAX_HASH 100003


typedef struct {{
    int key;
    int val;
    int used;
}} HashEntry;


HashEntry hash_table[MAX_HASH];


int _hash(int x) {{
    return ((unsigned int)x) % MAX_HASH;
}}


void _hash_clear() {{
    memset(hash_table, 0, sizeof(hash_table));
}}


void _hash_insert(int key, int val) {{
    int idx = _hash(key);
    while (hash_table[idx].used && hash_table[idx].key != key) {{
        idx = (idx + 1) % MAX_HASH;
    }}
    hash_table[idx].key = key;
    hash_table[idx].val = val;
    hash_table[idx].used = 1;
}}


int _hash_find(int key) {{
    int idx = _hash(key);
    while (hash_table[idx].used) {{
        if (hash_table[idx].key == key) return hash_table[idx].val;
        idx = (idx + 1) % MAX_HASH;
    }}
    return -1;
}}


int get_power_position_mod(int n, int m, int k) {{
    if (_gcd(m, n) != 1) return -1;
    if (k == 1) return 0;

    int order = get_power_cycle_mod(n, m);
    if (order == -1) return -1;

    int m_sqrt = 1;
    while (m_sqrt * m_sqrt < order) m_sqrt++;

    _hash_clear();

    int cur = 1;
    for (int j = 0; j < m_sqrt; j++) {{
        _hash_insert(cur, j);
        cur = (int)((uint64_t)cur * m % n);
    }}

    int inv = _modpow(m, order - m_sqrt, n);

    cur = k;
    for (int i = 0; i <= m_sqrt; i++) {{
        int j = _hash_find(cur);
        if (j != -1) {{
            int ans = i * m_sqrt + j;
            if (ans < order) return ans;
        }}
        cur = (int)((uint64_t)cur * inv % n);
    }}
    return -1;
}}
"""



get_power_position_mod_code = _get_power_position_mod_code_naive \
    if is_toy else _get_power_position_mod_code_baby_giant_step


_is_prime_code_naive = f"""int is_prime(int n) {{
    {make_assertion("n >= 1", "Invalid input of is_prime!", 1, True)}
    if (n == 1) return 0;
    if (n <= 3) return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;
    int i = 5;
    {big_int_declare("TMP")}
    while (1) {{
        {big_int_set_int("TMP", "i")}
        {big_int_mul("TMP", "TMP", "TMP")}
        if ({big_int_gt_int("TMP", "n")}) break;
        if (n % i == 0 || n % (i + 2) == 0) {{
            {big_int_release("TMP")}
            return 0; 
        }}
        i = i + 6;
    }}
    {big_int_release("TMP")}
    return 1; 
}}
"""


_is_prime_code_miller_rabin = f"""int is_prime(int n) {{
    
    int i, r, p, d, s, t;
    unsigned int a;
    unsigned long long x, pp;

    int num_small_primes = 12;
    int small_primes[12] = {{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}};
    
    int num_bases = 7;
    unsigned int bases[7] = {{2, 325, 9375, 28178, 450775, 9780504, 1795265022}};

    if (n < 2) return 0;
    
    for (i = 0; i < num_small_primes; i++) {{
        p = small_primes[i];
        if (n % p == 0) return n == p;
    }}
    
    d = n - 1;
    s = 0;
    while (d % 2 == 0) {{
        d >>= 1;
        s++;
    }}
    for (i = 0; i < num_bases; i++) {{
        a = bases[i];
        if (a >= (unsigned int)n) continue;
        x = 1;
        pp = a;
        t = d;
        while (t) {{
            if (t & 1) x = (x * pp) % n;
            pp = (pp * pp) % n;
            t >>= 1;
        }}
        if (x == 1 || x == (unsigned long long)(n - 1)) continue;
        for (r = 1; r < s; r++) {{
            x = (x * x) % n;
            if (x == (unsigned long long)(n - 1)) goto NEXT_WITNESS;
        }}
        return 0;
        NEXT_WITNESS:;
    }}
    return 1;
}}
"""


is_prime_code = _is_prime_code_naive if is_toy else _is_prime_code_miller_rabin


power_code = f"""int power(int base, int exp, int mod) {{
    {make_assertion("base >= 1 && exp >= 0 && (mod >= 2 || mod == -1)", "Invalid input of power!", 1, True)}
    int i = 0, res;
    {big_int_declare("RES")}
    {big_int_set_int("RES", "1")}
    while (i < exp) {{
        {big_int_mul_int("RES", "RES", "base")}
        if (mod != -1) {{
            {big_int_mod_uint("RES", "RES", "mod")}
        }}
        i = i + 1;
    }}
    if ({big_int_gt_int("RES", "2147483647")} || {big_int_lt_int("RES", "-2147483648")}) {{
        {big_int_release("RES")}
        {make_assertion("0", "[Runtime Error] function power encounters an int32 overflow!", 2, True)}
    }}
    {big_int_export_to_int("res", "RES")}
    {big_int_release("RES")}
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
    int n = 1;
    {big_int_declare("A")}
    {big_int_set_int("A", "a")}
    while ({big_int_le_int("A", "M")}) {{
        {big_int_mul_int("A", "A", "a")}
        n = n + 1;
    }}
    {big_int_release("A")}
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