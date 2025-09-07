from .tune import *
from ..big_int import *
from ..config import *
from ..SysY.printf import *


__all__ = [
    "solver_v1_globals_code",
    "set_abc_v1_code",
    "set_xy_name_v1_code",
    "write_solution_v1_code",
    "read_solution_v1_code",
    "resume_solution_v1_code",
    "Solve_Diophantine1_II_disproof_A_code",
    "Solve_Diophantine1_II_disproof_C_code",
    "insert_disproof_evidence_code",
    "get_disproof_evidence_code",
    "tune_settings_code",
    "recover_settings_code",
    "Solve_Diophantine1_I_i_code",
    "Solve_Diophantine1_I_ii_code",
    "Solve_Diophantine1_I_iii_code",
    "Solve_Diophantine1_II_code",
    "Solve_Diophantine1_code",
    "exhaust_solution_v1_code",
    "print_solution_v1_code",
]


_disproof_list_length = 100 if is_toy else 1000


_solution_max_length_v1 = 200000 if is_toy else 10000000


_verbose_v1 = 1


solver_v1_globals_code = f"""int a_v1;
int b_v1;
int c_v1;
int abc_set_status_v1 = 0;
int x_name_v1[10] = {{120, 0}};
int y_name_v1[10] = {{121, 0}};
int xy_name_set_status_v1 = 1;
int solution_v1[{_solution_max_length_v1}];
int solution_v1_pointer;
int solution_v1_length;
int solution_max_length_v1 = {_solution_max_length_v1};
int solver_v1_success = 0;
int int_threshold = 2100000000;
// 这两个设小了可能会导致求解失败
// 设大了可能导致那些需要多试几个方案的方程在一个方案上耗费的时间过长
int mod_threshold_v1 = {10_0000_0000};
int max_trial_num_v1 = 25;
int max_trial_num_v1_backup;
int mod_threshold_v1_backup;
int disproof_priorlist_prime[{_disproof_list_length}];
int disproof_priorlist_power[{_disproof_list_length}];
int disproof_priorlist_type[{_disproof_list_length}]; // a = 1, c = 3
int disproof_prime;
int disproof_power;
int disproof_type;
int disproof_priorlist_length = 0;
int verbose_v1 = {_verbose_v1};
int disable_front_mode = 0;
int disable_back_mode = 0;
int hijack_settings = 0;
"""


set_abc_v1_code = f"""void set_abc_v1(int a, int b, int c) {{
    {make_assertion("a >= 2 && c >= 2 && b >= 1", "Invalid input of set_abc_v1!", 1)}
    a_v1 = a;
    b_v1 = b;
    c_v1 = c;
    abc_set_status_v1 = 1;
}}
"""


set_xy_name_v1_code = f"""void set_xy_name_v1(int x_name[], int y_name[], int x_name_len, int y_name_len) {{
    int index = 0;
    int temp;
    int x_encounter_zero = 0;
    int y_encounter_zero = 0;
    while (index < 10) {{
        if (!x_encounter_zero && index < x_name_len) {{
            temp = x_name[index];
            x_name_v1[index] = temp;
            if (!temp) x_encounter_zero = 1;
        }}
        if (!y_encounter_zero && index < y_name_len) {{
            temp = y_name[index];
            y_name_v1[index] = temp;
            if(!temp) y_encounter_zero = 1;
        }}
        index = index + 1;
    }}
    {make_assertion("x_encounter_zero && y_encounter_zero", "Invalid input of set_xy_name_v1!", 1)}
    xy_name_set_status_v1 = 1;
}}
"""


write_solution_v1_code = f"""void write_solution_v1(int x) {{
    {make_assertion("solution_v1_pointer >= 0 && solution_v1_pointer < solution_max_length_v1", "-- [Solver V1] solution pointer out of legal range!", 1)}
    solution_v1[solution_v1_pointer] = x;
    solution_v1_pointer = solution_v1_pointer + 1;
    solution_v1_length = solution_v1_length + 1;
    solution_v1[0] = solution_v1_length;
}}
"""


read_solution_v1_code = f"""int read_solution_v1() {{
    {make_assertion("solution_v1_pointer >= 0 && solution_v1_pointer < solution_max_length_v1", "-- [Solver V1] solution pointer out of legal range!", 1, True)}
    solution_v1_pointer = solution_v1_pointer + 1;
    return solution_v1[solution_v1_pointer-1];
}}
"""


resume_solution_v1_code = f"""void resume_solution_v1(int solution_v1_pointer_backup) {{
    solution_v1_length = solution_v1_length - (solution_v1_pointer - solution_v1_pointer_backup);
    solution_v1_pointer = solution_v1_pointer_backup;
}}
"""


Solve_Diophantine1_II_disproof_A_code = f"""void Solve_Diophantine1_II_disproof_A() {{
    solver_v1_success = 0;
    if (disable_back_mode) return;
    int M = power(disproof_prime, disproof_power, -1);
    if(!assertion) return;
    int R = b_v1 % M;
    // c ^ y = R (mod M)
    write_solution_v1(c_v1);
    if(!assertion) return;
    write_solution_v1(R);
    if(!assertion) return;
    write_solution_v1(M);
    if(!assertion) return;
    int k = get_power_cycle_mod(M, c_v1);
    if(!assertion) return;
    int yr = get_power_position_mod(M, c_v1, R);
    if(!assertion) return;
    // c ^ y = R (mod M) is impossible
    if (yr == -1) {{
        write_solution_v1(yr);
        if(!assertion) return;
        solver_v1_success = 1;

    // c ^ y = R (mod M) => y = yr (mod k)
    }}else{{
        // if (k == 1) return;
        if (k < 10) return;
        write_solution_v1(yr);
        if(!assertion) return;
        write_solution_v1(k);
        if(!assertion) return;
        int solution_v1_pointer_backup = solution_v1_pointer;
        int n = 1, P = n * k + 1;
        int trial_num = 0;
        while (P < mod_threshold_v1 && trial_num < max_trial_num_v1) {{
            if (is_prime(P) && a_v1 % P != 0 && c_v1 % P != 0) {{
                if (verbose_v1) {{
                    {printf("-- Trying prime %d...", ["P"], 5)}
                }}
                trial_num = trial_num + 1;
                int minus_b = -b_v1;
                while (minus_b < 0) minus_b = minus_b + P;
                resume_solution_v1(solution_v1_pointer_backup);
                int m = get_power_cycle_mod(P, c_v1);
                int d = greatest_common_divisor(m, k);
                if (d > 1) {{
                    write_solution_v1(P);
                    if(!assertion) return;
                    write_solution_v1(m);
                    if(!assertion) return;
                    write_solution_v1(m / d);
                    if(!assertion) return;
                    int i = 0;
                    while (i < m / d) {{
                        write_solution_v1((yr % d) + i * d);
                        if(!assertion) return;
                        i = i + 1;
                    }}
                    write_solution_v1(m / d);
                    if(!assertion) return;
                    i = 0;
                    while (i < m / d) {{
                        write_solution_v1(power(c_v1, (yr % d) + i * d, P));
                        if(!assertion) return;
                        i = i + 1;
                    }}
                    write_solution_v1(P);
                    if(!assertion) return;
                    write_solution_v1(m / d);
                    if(!assertion) return;
                    i = 0;
                    int condition = 1;
                    while ( i < m / d) {{
                        write_solution_v1((power(c_v1, (yr % d) + i * d, P) + minus_b) % P);
                        condition = condition && (get_power_position_mod(P, a_v1, (power(c_v1, (yr % d) + i * d, P) + minus_b) % P) == -1);
                        if(!assertion) return;
                        i = i + 1;
                    }}
                    write_solution_v1(P);
                    if(!assertion) return;
                    if (condition) {{
                        solver_v1_success = 1;
                        return;
                    }}
                }}
            }}
            n = n + 1;
            P = n * k + 1;
        }}
        solver_v1_success = 0;
    }}
}}
"""


Solve_Diophantine1_II_disproof_C_code = f"""void Solve_Diophantine1_II_disproof_C() {{
    solver_v1_success = 0;
    if(disable_front_mode) return;
    int M = power(disproof_prime, disproof_power, -1);
    if(!assertion) return;
    int R = (-b_v1) % M;
    while (R < 0) R = R + M;
    // a ^ x = R (mod M)
    write_solution_v1(a_v1);
    if(!assertion) return;
    write_solution_v1(R);
    if(!assertion) return;
    write_solution_v1(M);
    if(!assertion) return;
    int k = get_power_cycle_mod(M, a_v1);
    if(!assertion) return;
    int xr = get_power_position_mod(M, a_v1, R);
    if(!assertion) return;
    // a ^ x = R (mod M) is impossible
    if (xr == -1) {{
        write_solution_v1(xr);
        if(!assertion) return;
        solver_v1_success = 1;

    // a ^ x = R (mod M) => x = xr (mod k)
    }}else{{
        // if (k == 1) return;
        if (k < 10) return;
        write_solution_v1(xr);
        if(!assertion) return;
        write_solution_v1(k);
        if(!assertion) return;
        int solution_v1_pointer_backup = solution_v1_pointer;
        int n = 1, P = n * k + 1;
        int trial_num = 0;
        while (P < mod_threshold_v1 && trial_num < max_trial_num_v1) {{
            if (is_prime(P) && a_v1 % P != 0 && c_v1 % P != 0) {{
                if (verbose_v1) {{
                    {printf("-- Trying prime %d...", ["P"], 5)}
                }}
                trial_num = trial_num + 1;
                resume_solution_v1(solution_v1_pointer_backup);
                int m = get_power_cycle_mod(P, a_v1);
                int d = greatest_common_divisor(m, k);
                if (d > 1) {{
                    write_solution_v1(P);
                    if(!assertion) return;
                    write_solution_v1(m);
                    if(!assertion) return;
                    write_solution_v1(m / d);
                    if(!assertion) return;
                    int i = 0;
                    while (i < m / d) {{
                        write_solution_v1((xr % d) + i * d);
                        if(!assertion) return;
                        i = i + 1;
                    }}
                    write_solution_v1(m / d);
                    if(!assertion) return;
                    i = 0;
                    while (i < m / d) {{
                        write_solution_v1(power(a_v1, (xr % d) + i * d, P));
                        if(!assertion) return;
                        i = i + 1;
                    }}
                    write_solution_v1(P);
                    if(!assertion) return;
                    write_solution_v1(m / d);
                    if(!assertion) return;
                    i = 0;
                    int condition = 1;
                    while (i < m / d) {{
                        write_solution_v1((power(a_v1, (xr % d) + i * d, P) + b_v1) % P);
                        condition = condition && (get_power_position_mod(P, c_v1, (power(a_v1, (xr % d) + i * d, P) + b_v1) % P) == -1);
                        if(!assertion) return;
                        i = i + 1;
                    }}
                    write_solution_v1(P);
                    if(!assertion) return;
                    if (condition) {{
                        solver_v1_success = 1;
                        return;
                    }}
                }}
            }}
            n = n + 1;
            P = n * k + 1;
        }}
        solver_v1_success = 0;
    }}
}}
"""


insert_disproof_evidence_code = f"""void insert_disproof_evidence(int prime, int _power, int type) {{
{make_assertion("disproof_priorlist_length < 100", "-- [Solver V1] disproof list needs more space!", 1)}
    disproof_priorlist_length = disproof_priorlist_length + 1;
    disproof_priorlist_prime[disproof_priorlist_length-1] = prime;
    disproof_priorlist_power[disproof_priorlist_length-1] = _power;
    disproof_priorlist_type[disproof_priorlist_length-1] = type;
    int list_index = disproof_priorlist_length-1;
    int A, B;
    while (list_index >= 1) {{
        A = power(disproof_priorlist_prime[list_index-1], disproof_priorlist_power[list_index-1], -1);
        B = power(disproof_priorlist_prime[list_index], disproof_priorlist_power[list_index], -1);
        {make_assertion("A!= B", "-- [Solver V1] unknown error encountered in insert_disproof_evidence!", 2)}
        if (A > B) {{
            int temp;
            temp = disproof_priorlist_prime[list_index-1];
            disproof_priorlist_prime[list_index-1] = disproof_priorlist_prime[list_index];
            disproof_priorlist_prime[list_index] = temp;

            temp = disproof_priorlist_power[list_index-1];
            disproof_priorlist_power[list_index-1] = disproof_priorlist_power[list_index];
            disproof_priorlist_power[list_index] = temp;

            temp = disproof_priorlist_type[list_index-1];
            disproof_priorlist_type[list_index-1] = disproof_priorlist_type[list_index];
            disproof_priorlist_type[list_index] = temp;
        }}else{{
            break;
        }}
        list_index = list_index - 1;
    }}
}}
"""


get_disproof_evidence_code = f"""void get_disproof_evidence() {{
    {make_assertion("disproof_priorlist_length", "-- [Solver V1] can't get disproof evidence: list is empty!", 1)}
    int list_index = 0;
    while (list_index < disproof_priorlist_length) {{
        if (list_index == 0) {{
            disproof_prime = disproof_priorlist_prime[list_index];
            disproof_power = disproof_priorlist_power[list_index];
            disproof_type = disproof_priorlist_type[list_index];
        }}else{{
            disproof_priorlist_prime[list_index-1] = disproof_priorlist_prime[list_index];
            disproof_priorlist_power[list_index-1] = disproof_priorlist_power[list_index];
            disproof_priorlist_type[list_index-1] = disproof_priorlist_type[list_index];
        }}
        list_index = list_index + 1;
    }}
    disproof_priorlist_length = disproof_priorlist_length - 1;
    disproof_priorlist_prime[disproof_priorlist_length] = 0;
    disproof_priorlist_power[disproof_priorlist_length] = 0;
    disproof_priorlist_type[disproof_priorlist_length] = 0;
}}
"""


Solve_Diophantine1_I_i_code = f"""void Solve_Diophantine1_I_i() {{
    solution_v1[0] = solution_v1_length;
    solver_v1_success = 1;
}}
"""


Solve_Diophantine1_I_ii_code = f"""void Solve_Diophantine1_I_ii() {{
    solution_v1[0] = solution_v1_length;
    solver_v1_success = 1;
}}
"""


Solve_Diophantine1_I_iii_code = f"""void Solve_Diophantine1_I_iii() {{
    int N = solution_v1[solution_v1_pointer-1];
    N = get_power_times_over(b_v1, N);
    if(!assertion) return;
    write_solution_v1(N);
    if(!assertion) return;
    int array_pointer = solution_v1_pointer;
    if (N > 1) {{
        write_solution_v1(0);
        if(!assertion) return;
        {big_int_declare("A")}
        {big_int_declare("B")}
        {big_int_declare("C")}
        {big_int_declare("TMP")}
        {big_int_set_int("A", "a_v1")}
        {big_int_set_int("B", "b_v1")}
        {big_int_set_int("C", "c_v1")}
        int a0 = a_v1, c0 = c_v1, x = 1, y = 1;
        while (x < N || y < N) {{
            {big_int_add("TMP", "A", "B")}
            {big_int_sub("TMP", "C", "TMP")}
            if ({big_int_gt_int("TMP", "0")}) {{
                if ({"A > int_threshold / a0" if is_toy else "0"}) {{
                    {printf(f"-- [Solver V1] Runtime Warning: exceeding range of int32; try the non-toy version to solve this case!", [], 5)}
                    return;
                }}
                {big_int_mul_int("A", "A", "a0")}
                x = x + 1;
            }}else{{
                if ({big_int_eq_int("TMP", "0")}) {{
                    write_solution_v1(x);
                    if(!assertion) return;
                    write_solution_v1(y);
                    if(!assertion) return;
                    solution_v1[array_pointer] = solution_v1[array_pointer] + 1;
                    if ({"C > int_threshold / c0" if is_toy else "0"}) {{
                        {printf(f"-- [Solver V1] Runtime Warning: exceeding range of int32; try the non-toy version to solve this case!", [], 6)}
                        return;
                    }}
                    {big_int_mul_int("C", "C", "c0")}
                    y = y + 1;
                }}else{{
                    if ({"C > int_threshold / c0" if is_toy else "0"}) {{
                        {printf(f"-- [Solver V1] Runtime Warning: exceeding range of int32; try the non-toy version to solve this case!", [], 6)}
                        return;
                    }}
                    {big_int_mul_int("C", "C", "c0")}
                    y = y + 1;
                }}
            }}
        }}
        {big_int_release("A")}
        {big_int_release("B")}
        {big_int_release("C")}
        {big_int_release("TMP")}
        solution_v1[0] = solution_v1_length;
        solver_v1_success = 1;
    }}else{{
        // -1表示不用枚举，“x < 1或y < 1”一出来，方程肯定就无解了
        write_solution_v1(-1);
        solution_v1[0] = solution_v1_length;
        solver_v1_success = 1;
    }}
}}
"""


_enter = "\n"


tune_settings_code = f"""void tune_settings(int a, int b, int c) {{
    if (hijack_settings) return;
    max_trial_num_v1_backup = max_trial_num_v1;
    mod_threshold_v1_backup = mod_threshold_v1;
    // 点状设置（优先生效）
{f"{_enter}".join([
    f"    if (a == {a} && b == {b} && c == {c}) {{ max_trial_num_v1 = {x}; mod_threshold_v1 = {y}; return; }}" 
    for a, b, c, x, y in special_trial_num_list
])}
    // 面状设置
    if (a <= 125 && b <= 125 && c <= 125) {{
        max_trial_num_v1 = 5; mod_threshold_v1 = {10_0000_0000};
        return;
    }}
    if (a <= 250 && b <= 250 && c <= 250) {{
        max_trial_num_v1 = 25; mod_threshold_v1 = {10_0000_0000};
        return;
    }}
    if (a <= 500 && b <= 500 && c <= 500) {{
        max_trial_num_v1 = 15; mod_threshold_v1 = {5000_0000};
        return;
    }}
}}
"""


recover_settings_code = f"""void recover_settings() {{
    if (hijack_settings) return;
    max_trial_num_v1 = max_trial_num_v1_backup;
    mod_threshold_v1 = mod_threshold_v1_backup;
}}
"""


Solve_Diophantine1_II_code = f"""void Solve_Diophantine1_II() {{
    if (verbose_v1) {{
        {printf("-- Verbose mode on.", [], 2)}
    }}
    {big_int_declare("A")}
    {big_int_declare("B")}
    {big_int_declare("C")}
    {big_int_declare("TMP")}
    {big_int_declare("THRESHOLD")}
    {big_int_set_int("A", "a_v1")}
    {big_int_set_int("B", "b_v1")}
    {big_int_set_int("C", "c_v1")}
    {f'THRESHOLD = 1{"0"*9};' if is_toy else f'mpz_set_str(THRESHOLD, "1{"0"*100}", 10);'}
    int a0 = a_v1, c0 = c_v1, x0 = 0, x = 1, y0 = 0, y = 1;
    while (1) {{
        {big_int_add("TMP", "A", "B")}
        {big_int_sub("TMP", "C", "TMP")}
        if ({big_int_gt_int("TMP", "0")}) {{
            {big_int_sub("TMP", "THRESHOLD", "B")}
            {big_int_div_int("TMP", "TMP", "a0")}
            if ({big_int_gt("A", "TMP")}) break;
            {big_int_mul_int("A", "A", "a0")}
            x = x + 1;
        }}else{{
            if ({big_int_eq_int("TMP", "0")}) {{
                x0 = x;
                y0 = y;
                {big_int_div_int("TMP", "THRESHOLD", "c0")}
                if ({big_int_gt("C", "TMP")}) break;
                {big_int_mul_int("C", "C", "c0")}
                y = y + 1;
            }}else{{
                {big_int_div_int("TMP", "THRESHOLD", "c0")}
                if ({big_int_gt("C", "TMP")}) break;
                {big_int_mul_int("C", "C", "c0")}
                y = y + 1;
            }}
        }}
    }}
    {big_int_release("A")}
    {big_int_release("B")}
    {big_int_release("C")}
    {big_int_release("TMP")}
    {big_int_release("THRESHOLD")}
    // 从“反设x >= x0” / “反设y >= y0”开始归谬
    x0 = x0 + 1;
    y0 = y0 + 1;
    int prime_list_index = 0;
    // 希望对所有小于500的a, b, c顺利求解，这里开得稍大一点
    while (prime_list[prime_list_index] < 600) {{
        if (c_v1 % prime_list[prime_list_index] == 0) {{
            {make_assertion("a_v1 % prime_list[prime_list_index] != 0", "-- [Solver V1] unknown error encountered in situation II!", 3)}
            insert_disproof_evidence(prime_list[prime_list_index], y0, 2);
        }}
        if (a_v1 % prime_list[prime_list_index] == 0) {{
            {make_assertion("c_v1 % prime_list[prime_list_index] != 0", "-- [Solver V1] unknown error encountered in situation II!", 3)}
            insert_disproof_evidence(prime_list[prime_list_index], x0, 1);
        }}
        prime_list_index = prime_list_index + 1;
    }}
    int solution_v1_pointer_backup = solution_v1_pointer;
    while (disproof_priorlist_length) {{
        resume_solution_v1(solution_v1_pointer_backup);
        get_disproof_evidence();
        if(!assertion) return;
        write_solution_v1(disproof_prime);
        if(!assertion) return;
        write_solution_v1(disproof_power);
        if(!assertion) return;
        write_solution_v1(disproof_type);
        if(!assertion) return;
        if (verbose_v1) {{
            if (disproof_type == 1) {{
                {printf("-- Trying to disprove x >= %d with prime factor %d of %d ...", ["disproof_power", "disproof_prime", "a0"], 4)}
            }}else if (disproof_type == 2) {{
                {printf("-- Trying to disprove y >= %d with prime factor %d of %d ...", ["disproof_power", "disproof_prime", "c0"], 4)}
            }}else{{
                {make_assertion("0", "-- [Solver V1] unknown error encountered in situation II!", 3)} 
            }}
        }}
        if (disproof_type == 1) {{
            Solve_Diophantine1_II_disproof_A();
            if(!assertion) return;
            if (solver_v1_success) {{
                if (verbose_v1) {{
                    {printf("-- Succeeded.", [], 5)}
                }}
                if (disproof_power > 1) {{
                    solution_v1_pointer_backup = solution_v1_pointer;
                    write_solution_v1(0);
                    if(!assertion) return;
                    // 归谬完成，枚举x的有限个取值
                    {big_int_declare("A")}
                    {big_int_declare("B")}
                    {big_int_declare("C")}
                    {big_int_declare("TMP")}
                    {big_int_set_int("A", "a_v1")}
                    {big_int_set_int("B", "b_v1")}
                    {big_int_set_int("C", "c_v1")}
                    int x = 1, y = 1;
                    int a0 = a_v1, c0 = c_v1;
                    while (x < disproof_power) {{
                        {big_int_add("TMP", "A", "B")}
                        {big_int_sub("TMP", "C", "TMP")}
                        if ({big_int_gt_int("TMP", "0")}) {{
                            if ({"A > int_threshold / a0" if is_toy else "0"}) {{
                                {printf(f"-- [Solver V1] Runtime Warning: exceeding range of int32; try the non-toy version to solve this case!", [], 8)}
                                solver_v1_success = 0;
                                return;
                            }}
                            {big_int_mul_int("A", "A", "a0")}
                            x = x + 1;
                        }}else{{
                            if ({big_int_eq_int("TMP", "0")}) {{
                                write_solution_v1(x);
                                if(!assertion) return;
                                write_solution_v1(y);
                                if(!assertion) return;
                                solution_v1[solution_v1_pointer_backup] = solution_v1[solution_v1_pointer_backup]+1;
                                if ({"C > int_threshold / c0" if is_toy else "0"}) {{
                                    {printf(f"-- [Solver V1] Runtime Warning: exceeding range of int32; try the non-toy version to solve this case!", [], 9)}
                                    solver_v1_success = 0;
                                    return;
                                }}
                                {big_int_mul_int("C", "C", "c0")}
                                y = y + 1;
                            }}else{{
                                if ({"C > int_threshold / c0" if is_toy else "0"}) {{
                                    {printf(f"-- [Solver V1] Runtime Warning: exceeding range of int32; try the non-toy version to solve this case!", [], 9)}
                                    solver_v1_success = 0;
                                    return;
                                }}
                                {big_int_mul_int("C", "C", "c0")}
                                y = y + 1;
                            }}
                        }}
                    }}
                    {big_int_release("A")}
                    {big_int_release("B")}
                    {big_int_release("C")}
                    {big_int_release("TMP")}
                    solution_v1[0] = solution_v1_length;
                    return;
                }}else{{
                    // -1表示不用枚举
                    write_solution_v1(-1);
                    solution_v1[0] = solution_v1_length;
                    return;
                }}
            }}
        }}else if (disproof_type == 2) {{
            Solve_Diophantine1_II_disproof_C();
            if(!assertion) return;
            if (solver_v1_success) {{
                if (verbose_v1) {{
                    {printf("-- Succeeded.", [], 5)}
                }}
                if (disproof_power > 1) {{
                    solution_v1_pointer_backup = solution_v1_pointer;
                    write_solution_v1(0);
                    if(!assertion) return;
                    // 归谬完成，枚举y的有限个取值
                    {big_int_declare("A")}
                    {big_int_declare("B")}
                    {big_int_declare("C")}
                    {big_int_declare("TMP")}
                    {big_int_set_int("A", "a_v1")}
                    {big_int_set_int("B", "b_v1")}
                    {big_int_set_int("C", "c_v1")}
                    int x = 1, y = 1;
                    int a0 = a_v1, c0 = c_v1;
                    while (y < disproof_power) {{
                        {big_int_add("TMP", "A", "B")}
                        {big_int_sub("TMP", "C", "TMP")}
                        if ({big_int_gt_int("TMP", "0")}) {{
                            if ({"A > int_threshold / a0" if is_toy else "0"}) {{
                                {printf(f"-- [Solver V1] Runtime Warning: exceeding range of int32; try the non-toy version to solve this case!", [], 8)}
                                solver_v1_success = 0;
                                return;
                            }}
                            {big_int_mul_int("A", "A", "a0")}
                            x = x + 1;
                        }}else{{
                            if ({big_int_eq_int("TMP", "0")}) {{
                                write_solution_v1(x);
                                if(!assertion) return;
                                write_solution_v1(y);
                                if(!assertion) return;
                                solution_v1[solution_v1_pointer_backup] = solution_v1[solution_v1_pointer_backup]+1;
                                if ({"C > int_threshold / c0" if is_toy else "0"}) {{
                                    {printf(f"-- [Solver V1] Runtime Warning: exceeding range of int32; try the non-toy version to solve this case!", [], 9)}
                                    solver_v1_success = 0;
                                    return;
                                }}
                                {big_int_mul_int("C", "C", "c0")}
                                y = y + 1;
                            }}else{{
                                if ({"C > int_threshold / c0" if is_toy else "0"}) {{
                                    {printf(f"-- [Solver V1] Runtime Warning: exceeding range of int32; try the non-toy version to solve this case!", [], 9)}
                                    solver_v1_success = 0;
                                    return;
                                }}
                                {big_int_mul_int("C", "C", "c0")}
                                y = y + 1;
                            }}
                        }}
                    }}
                    {big_int_release("A")}
                    {big_int_release("B")}
                    {big_int_release("C")}
                    {big_int_release("TMP")}
                    solution_v1[0] = solution_v1_length;
                    return;
                }}else{{
                    // -1表示不用枚举
                    write_solution_v1(-1);
                    solution_v1[0] = solution_v1_length;
                    return;
                }}
            }}
        }}else{{ 
            {make_assertion("0", "-- [Solver V1] unknown error encountered in situation II!", 3)}
        }}
        if (power(disproof_prime, disproof_power, -1) < mod_threshold_v1 / disproof_prime) {{
            insert_disproof_evidence(disproof_prime, disproof_power+1, disproof_type);
            if(!assertion) return;
        }}
    }}
    solver_v1_success = 0;
}}
"""


Solve_Diophantine1_code = f"""void Solve_Diophantine1() {{
    {make_assertion("abc_set_status_v1", "-- [Solver V1] a, b, c not set, can't solve now!", 1)}

    solution_v1_pointer = 1;
    solution_v1_length = 1;
    solver_v1_success = 0;
    disproof_priorlist_length = 0;

    write_solution_v1(a_v1);
    if(!assertion) return;
    write_solution_v1(b_v1);
    if(!assertion) return;
    write_solution_v1(c_v1);
    if(!assertion) return;

    // 情况I - i
    int temp = greatest_common_divisor(b_v1, c_v1);
    if(!assertion) return;
    temp = contain_undividable_prime_part(temp, a_v1);
    if(!assertion) return;
    if (temp) {{
        write_solution_v1(1);
        if(!assertion) return;
        write_solution_v1(1);
        if(!assertion) return;
        temp = greatest_common_divisor(b_v1, c_v1);
        while (greatest_common_divisor(a_v1, temp) != 1) temp = temp / greatest_common_divisor(a_v1, temp);
        if(!assertion) return;
        write_solution_v1(temp);
        if(!assertion) return;
        Solve_Diophantine1_I_i();
        return;
    }}

    // 情况I - ii
    temp = greatest_common_divisor(a_v1, b_v1);
    if(!assertion) return;
    temp = contain_undividable_prime_part(temp, c_v1);
    if(!assertion) return;
    if (temp) {{
        write_solution_v1(1);
        if(!assertion) return;
        write_solution_v1(2);
        if(!assertion) return;
        temp = greatest_common_divisor(a_v1, b_v1);
        while (greatest_common_divisor(c_v1, temp) != 1) temp = temp / greatest_common_divisor(c_v1, temp);
        if(!assertion) return;
        write_solution_v1(temp);
        if(!assertion) return;
        Solve_Diophantine1_I_ii();
        return;
    }}

    // 情况I - iii
    temp = greatest_common_divisor(a_v1, c_v1);
    if(!assertion) return;
    if (temp > 1) {{
        write_solution_v1(1);
        if(!assertion) return;
        write_solution_v1(3);
        if(!assertion) return;
        write_solution_v1(temp);
        if(!assertion) return;
        Solve_Diophantine1_I_iii();
        return;
    }}

    // 情况II
    write_solution_v1(2);
    if(!assertion) return;
    tune_settings(a_v1, b_v1, c_v1);
    Solve_Diophantine1_II();
    if(!assertion) return;
    recover_settings(a_v1, b_v1, c_v1);
    return;
}}
"""

exhaust_solution_v1_code = f"""void exhaust_solution_v1(int nsolutions_pointer) {{
    int a = solution_v1[1];
    int b = solution_v1[2];
    int c = solution_v1[3];
    int nsolutions = solution_v1[nsolutions_pointer];
    if (nsolutions == -1) {{
        {printf("So %d ^ %s + %d = %d ^ %s is impossible.", ["a", "x_name_v1", "b", "c", "y_name_v1"], 2)}
    }}else if (nsolutions == 0) {{
        {printf("Further examination shows that %d ^ %s + %d = %d ^ %s is impossible.", ["a", "x_name_v1", "b", "c", "y_name_v1"], 2)}
    }}else{{
        {print_word("Further examination shows that ", 2)}
        putch(left_parenthesis);
        print_word(x_name_v1);
        putch(comma);
        putch(space);
        print_word(y_name_v1);
        putch(right_parenthesis);
        putch(space);
        putch(equals);
        putch(space);
        int offset = 1;
        while (offset / 2 < nsolutions) {{
            if (offset != 1) {{
                putch(comma);
                putch(space);
            }}
            putch(left_parenthesis);
            putint(solution_v1[nsolutions_pointer+offset]);
            putch(comma);
            putch(space);
            putint(solution_v1[nsolutions_pointer+offset+1]);
            putch(right_parenthesis);
            offset = offset + 2;
        }}
        putch(period);
        print_line(newline);
    }}
}}
"""


print_solution_v1_code = f"""void print_solution_v1() {{
    {make_assertion("solver_v1_success && xy_name_set_status_v1", "-- [Solver V1] solver failed or name not set, can't print solution!", 1)}
    int a = solution_v1[1];
    int b = solution_v1[2];
    int c = solution_v1[3];
    {printf("For positive integers %s, %s satisfying %d ^ %s + %d = %d ^ %s,", ["x_name_v1", "y_name_v1", "a", "x_name_v1", "b", "c", "y_name_v1"], 1)}
    int i;
    if (solution_v1[4] == 1) {{
        if (solution_v1[5] == 1) {{
            {printf("this is impossible, because it implies that %d ^ %s = 0 (mod %d).", ["a", "x_name_v1", "solution_v1[6]"], 3)}
        }}else if (solution_v1[5] == 2) {{
            {printf("this is impossible, because it implies that %d ^ %s = 0 (mod %d).", ["c", "y_name_v1", "solution_v1[6]"], 3)}
        }}else if (solution_v1[5] == 3) {{
            {printf("if %s >= %d and %s >= %d,", ["x_name_v1", "solution_v1[7]", "y_name_v1", "solution_v1[7]"], 3)}
            {printf("%d = 0 (mod %d), which is impossible.", ["b", "power(solution_v1[6], solution_v1[7], -1)"], 3)}
            {printf("Therefore, %s < %d or %s < %d.", ["x_name_v1", "solution_v1[7]", "y_name_v1", "solution_v1[7]"], 3)}
            int nsolutions_pointer = 8;
            exhaust_solution_v1(nsolutions_pointer);
        }}else {{
            {make_assertion("0", "-- [Solver V1] solution vector format is incorrect for unknown reason!", 3)}
        }}
    }}else if (solution_v1[4] == 2) {{
        // disproof prime, power and type
        // int dp_prime = solution_v1[5];  (not used)
        int dp_power = solution_v1[6];
        int dp_type = solution_v1[7];
        solution_v1_pointer = 8;
        // Back Mode: Obtain y = yr (mod k) by disproof assumption and search series {{n*k + 1}} for an appropriate prime number
        if (dp_type == 1) {{
            read_solution_v1();
            int R = read_solution_v1();
            int M = read_solution_v1();
            {printf("if %s >= %d, %d ^ %s = %d (mod %d).", ["x_name_v1", "dp_power", "c", "y_name_v1", "R", "M"], 3)}
            int yr = read_solution_v1();
            if (yr == -1) {{
                {printf("However, this is impossible.", [], 4)}
                {printf("Therefore, %s < %d.", ["x_name_v1", "dp_power"], 4)}
                exhaust_solution_v1(solution_v1_pointer);
            }}else{{
                int k = read_solution_v1();
                int P = read_solution_v1();
                int m = read_solution_v1();
                int npossibilities = read_solution_v1();
                // k m 不等，x = xr (mod k) 推出多个关于m的可能余数
                if (k != m) {{
                    {printf("So %s = %d (mod %d), ", ["y_name_v1", "yr", "k"], 5)}
                    {print_word("which implies ", 5)}
                    print_word(y_name_v1);
                    putch(space);
                    putch(equals);
                    putch(space);
                    i = 0;
                    while (i < npossibilities) {{
                        if (i) {{
                            putch(comma);
                            putch(space);
                        }} 
                        putint(read_solution_v1());
                        i = i + 1;
                    }}
                    {printf(" (mod %d).", ["m"], 5)}
                // k m 相等，npossibilities = 1
                }}else {{
                    {printf("So %s = %d (mod %d), ", ["y_name_v1", "yr", "k"], 5)}
                    read_solution_v1();
                }}
                read_solution_v1();
                {print_word("Therefore, ", 4)}
                putint(c);
                putch(space);
                putch(hat);
                putch(space);
                print_word(y_name_v1);
                putch(space);
                putch(equals);
                putch(space);
                i = 0;
                while (i < npossibilities) {{
                    if (i) {{
                        putch(comma);
                        putch(space);
                    }} 
                    putint(read_solution_v1());
                    i = i + 1;
                }}
                {printf(" (mod %d).", ["P"], 4)}
                read_solution_v1();
                read_solution_v1();
                {print_word("So ", 4)}
                putint(a);
                putch(space);
                putch(hat);
                putch(space);
                print_word(x_name_v1);
                putch(space);
                putch(equals);
                putch(space);
                i = 0;
                while (i < npossibilities) {{
                    if (i) {{
                        putch(comma);
                        putch(space);
                    }} 
                    putint(read_solution_v1());
                    i = i + 1;
                }}
                {printf(" (mod %d), but this is impossible.", ["P"], 4)}
                {printf("Therefore, %s < %d.", ["x_name_v1", "dp_power"], 4)}
                read_solution_v1();
                exhaust_solution_v1(solution_v1_pointer);
            }}
        // Front Mode: Obtain x = xr (mod k) by disproof assumption and search series {{n*k + 1}} for an appropriate prime number
        }}else if (dp_type == 2){{
            read_solution_v1();
            int R = read_solution_v1();
            int M = read_solution_v1();
            {printf("if %s >= %d, %d ^ %s = %d (mod %d).", ["y_name_v1", "dp_power", "a", "x_name_v1", "R", "M"], 3)}
            int xr = read_solution_v1();
            if (xr == -1) {{
                {printf("However, this is impossible.", [], 4)}
                {printf("Therefore, %s < %d.", ["y_name_v1", "dp_power"], 4)}
                exhaust_solution_v1(solution_v1_pointer);
            }}else{{
                int k = read_solution_v1();
                int P = read_solution_v1();
                int m = read_solution_v1();
                int npossibilities = read_solution_v1();
                // k m 不等，x = xr (mod k) 推出多个关于m的可能余数
                if (k != m) {{
                    {printf("So %s = %d (mod %d), ", ["x_name_v1", "xr", "k"], 5)}
                    {print_word("which implies ", 5)}
                    print_word(x_name_v1);
                    putch(space);
                    putch(equals);
                    putch(space);
                    i = 0;
                    while (i < npossibilities) {{
                        if (i) {{
                            putch(comma);
                            putch(space);
                        }} 
                        putint(read_solution_v1());
                        i = i + 1;
                    }}
                    {printf(" (mod %d).", ["m"], 5)}
                // k m 相等，npossibilities = 1
                }}else {{
                    {printf("So %s = %d (mod %d).", ["x_name_v1", "xr", "k"], 5)}
                    read_solution_v1();
                }}
                read_solution_v1();
                {print_word("Therefore, ", 4)}
                putint(a);
                putch(space);
                putch(hat);
                putch(space);
                print_word(x_name_v1);
                putch(space);
                putch(equals);
                putch(space);
                i = 0;
                while (i < npossibilities) {{
                    if (i) {{
                        putch(comma);
                        putch(space);
                    }} 
                    putint(read_solution_v1());
                    i = i + 1;
                }}
                {printf(" (mod %d).", ["P"], 4)}
                read_solution_v1();
                read_solution_v1();
                {print_word("So ", 4)}
                putint(c);
                putch(space);
                putch(hat);
                putch(space);
                print_word(y_name_v1);
                putch(space);
                putch(equals);
                putch(space);
                i = 0;
                while (i < npossibilities) {{
                    if (i) {{
                        putch(comma);
                        putch(space);
                    }} 
                    putint(read_solution_v1());
                    i = i + 1;
                }}
                {printf(" (mod %d), but this is impossible.", ["P"], 4)}
                {printf("Therefore, %s < %d.", ["y_name_v1", "dp_power"], 4)}
                read_solution_v1();
                exhaust_solution_v1(solution_v1_pointer);
            }}
        }}else{{
        {make_assertion("0", "-- [Solver V1] solution vector format is incorrect for unknown reason!", 3)}
        }}
    }}else{{
        {make_assertion("0", "-- [Solver V1] solution vector format is incorrect for unknown reason!", 2)}
    }}
}}
"""

