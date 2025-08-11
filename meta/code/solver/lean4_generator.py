from meta.SysY.printf import *


__all__ = [
    "print_Lean4_prop_v1_code",
    "print_Lean4_int_array_code",
    "generate_Lean4_code_v1_code",
]


_slash = "\\"


print_Lean4_prop_v1_code = f"""void print_Lean4_prop_v1 (int nsolutions_pointer, int bracket_multiple) {{
    int nsolutions = solution_v1[nsolutions_pointer];
    // 有 -1 和 0 两种情况（-1用于向 print_solution_v1 函数传递信息，解的个数也为 0）
    if (nsolutions <= 0) {{
        {print_word("False", 2)}
        return;
    }}
    if (bracket_multiple) putch(left_parenthesis);
    {print_word("List.Mem (x, y) [", 1)}
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
    {print_word("]", 1)}
    if (bracket_multiple) putch(right_parenthesis);
}}
"""


print_Lean4_int_array_code = f"""void print_Lean4_int_array (int nsolutions_pointer) {{
    int nint = solution_v1[nsolutions_pointer];
    int offset = 1;
    while (offset <= nint) {{
        if (offset >= 2) {{
            putch(comma);
            putch(space);
        }}
        putint(solution_v1[nsolutions_pointer+offset]);
        offset = offset + 1;
    }}
}}
"""


generate_Lean4_code_v1_code = f""" void generate_Lean4_code_v1 () {{
    {make_assertion("solver_v1_success && xy_name_set_status_v1", "[Solver V1] solver failed or name not set, can't generate Lean4 code!", 1)}
    int a = solution_v1[1];
    int b = solution_v1[2];
    int c = solution_v1[3];
    int class = solution_v1[4];
    if (class == 1) {{
        int type = solution_v1[5];
        // a ^ x = 0 (mod M) is impossible
        // e.g. 3 ^ x + 6 = 8 ^ y
        if (type == 1) {{
            {printf("/-", [], 3)}
            {printf("(Class I, Type i)   %d ^ x + %d = %d ^ y", ["a", "b", "c"], 3)}
            print_solution_v1();
            {printf("-/", [], 3)}
            int M = solution_v1[6];
            {printf("theorem diophantine1_%d_%d_%d (x : Nat) (y : Nat) (h1 : x >= 1) (h2 : y >= 1) (h3 : %d ^ x + %d = %d ^ y) :", ["a", "b", "c", "a", "b", "c"], 3)}
            {printf("  False", [], 3)}
            {printf("  := by", [], 3)}
            {printf("  have h4 : x % 1 = 0 := by omega", [], 3)}
            {printf("  have h5 : y % 1 = 0 := by omega", [], 3)}   
            {printf(f"  have h6 := Claim (%d ^ y {_slash}% %d = 0) [", ["c", "M"], 3)}   
            {printf("    {prop := y % 1 = 0, proof := h5},", [], 3)}
            {printf("    {prop := y >= 1, proof := h2},", [], 3)}   
            {printf('  ] "pow_mod_eq_zero"', [], 3)}   
            {printf(f"  have h7 : %d ^ x {_slash}% %d = 0 := by omega", ["a", "M"], 3)}   
            {printf("  have h8 := Claim False [", [], 3)}   
            {printf("    {prop := x % 1 = 0, proof := h4},", [], 3)}
            {printf("    {prop := x >= 1, proof := h1},", [], 3)}   
            {printf(f"    {{prop := %d ^ x {_slash}% %d = 0, proof := h7}},", ["a", "M"], 3)}
            {printf('  ] "observe_mod_cycle"', [], 3)}
            {printf("  exact h8", [], 3)}
        // c ^ y = 0 (mod M) is impossible
        // e.g. 3 ^ x + 6 = 11 ^ y
        }}else if (type == 2) {{
           {printf("/-", [], 3)}
            {printf("(Class I, Type ii)   %d ^ x + %d = %d ^ y", ["a", "b", "c"], 3)}
            print_solution_v1();
            {printf("-/", [], 3)}
            int M = solution_v1[6];
            {printf("theorem diophantine1_%d_%d_%d (x : Nat) (y : Nat) (h1 : x >= 1) (h2 : y >= 1) (h3 : %d ^ x + %d = %d ^ y) :", ["a", "b", "c", "a", "b", "c"], 3)}
            {printf("  False", [], 3)}
            {printf("  := by", [], 3)}
            {printf("  have h4 : x % 1 = 0 := by omega", [], 3)}
            {printf("  have h5 : y % 1 = 0 := by omega", [], 3)}   
            {printf(f"  have h6 := Claim (%d ^ x {_slash}% %d = 0) [", ["a", "M"], 3)}   
            {printf("    {prop := x % 1 = 0, proof := h4},", [], 3)}
            {printf("    {prop := x >= 1, proof := h1},", [], 3)}   
            {printf('  ] "pow_mod_eq_zero"', [], 3)}   
            {printf(f"  have h7 : %d ^ y {_slash}% %d = 0 := by omega", ["c", "M"], 3)}   
            {printf("  have h8 := Claim False [", [], 3)}   
            {printf("    {prop := y % 1 = 0, proof := h5},", [], 3)}
            {printf("    {prop := y >= 1, proof := h2},", [], 3)}   
            {printf(f"    {{prop := %d ^ y {_slash}% %d = 0, proof := h7}},", ["c", "M"], 3)}
            {printf('  ] "observe_mod_cycle"', [], 3)}
            {printf("  exact h8", [], 3)}
        // x >= n and y >= n => b = 0 (mod P ^ n) (×), so x < n or y < n
        // e.g. 2 ^ x + 4 = 6 ^ y
        }}else if (type == 3) {{
            {printf("/-", [], 3)}
            {printf("(Class I, Type iii)   %d ^ x + %d = %d ^ y", ["a", "b", "c"], 3)}
            print_solution_v1();
            {printf("-/", [], 3)}
            {printf("theorem diophantine1_%d_%d_%d (x : Nat) (y : Nat) (h1 : x >= 1) (h2 : y >= 1) (h3 : %d ^ x + %d = %d ^ y) :", ["a", "b", "c", "a", "b", "c"], 3)}
            {print_word("  ", 3)}
            print_Lean4_prop_v1(8, 0);
            print_line(newline);
            {printf("  := by", [], 3)}
            {printf("  have h4 : x % 1 = 0 := by omega", [], 3)}
            {printf("  have h5 : y % 1 = 0 := by omega", [], 3)}  
            int gcd = solution_v1[6];
            int dp_power = solution_v1[7];
            {printf("  by_cases h6 : And (x >= %d) (y >= %d)", ["dp_power", "dp_power"], 3)}
            {printf(f"  have h7 := Claim (%d ^ x {_slash}% %d = 0) [", ["a", "power(gcd, dp_power, -1)"], 3)}   
            {printf("    {prop := x % 1 = 0, proof := h4},", [], 3)}
            {printf("    {prop := x >= %d, proof := h6.left},", ["dp_power"], 3)}   
            {printf('  ] "pow_mod_eq_zero"', [], 3)}   
            {printf(f"  have h8 := Claim (%d ^ y {_slash}% %d = 0) [", ["c", "power(gcd, dp_power, -1)"], 3)}   
            {printf("    {prop := y % 1 = 0, proof := h5},", [], 3)}
            {printf("    {prop := y >= %d, proof := h6.right},", ["dp_power"], 3)}   
            {printf('  ] "pow_mod_eq_zero"', [], 3)} 
            {printf("  omega", [], 3)}
            {printf("  have h7 : Or (x <= %d) (y <= %d) := by omega", ["dp_power-1, dp_power-1"], 3)}
            {print_word("  have h8 := Claim ", 3)}
            print_Lean4_prop_v1(8, 1);
            {printf(" [", [], 3)}
            {printf("    {prop :=  x % 1 = 0, proof := h4},", [], 3)}
            {printf("    {prop :=  x >= 1, proof := h1},", [], 3)}
            {printf("    {prop :=  y % 1 = 0, proof := h5},", [], 3)}
            {printf("    {prop :=  y >= 1, proof := h2},", [], 3)}
            {printf("    {prop := %d ^ x + %d = %d ^ y, proof := h3},", ["a", "b", "c"], 3)}
            {printf("    {prop := Or (x <= %d) (y <= %d), proof := h7},", ["dp_power-1, dp_power-1"], 3)}
            {printf('  ] "diophantine1_double_enumeration"', [], 3)}
            {printf("  exact h8", [], 3)}
        }}else{{
            {make_assertion("0", "[Solver V1] solution vector format is incorrect for unknown reason!", 3)}
        }}    
    }}else if (class == 2){{
        int dp_prime = solution_v1[5];
        int dp_power = solution_v1[6];
        int dp_type = solution_v1[7];
        solution_v1_pointer = 8;
        // Back Mode: Obtain y = yr (mod k) by disproof assumption and search series {{n*k + 1}} for an appropriate prime number
        if (dp_type == 1) {{
            read_solution_v1();
            //If x >= dp_power, c ^ y = R (mod M).
            int R = read_solution_v1();
            int M = read_solution_v1();
            int yr = read_solution_v1();
            //However, c ^ y = R (mod M) is impossible.
            // e.g. 2 ^ x + 5 = 11 ^ y
            if (yr == -1) {{
                {printf("/-", [], 4)}
                {printf("(Class II, Back Mode, no magic prime)   %d ^ x + %d = %d ^ y", ["a", "b", "c"], 4)}
                print_solution_v1();
                {printf("-/", [], 4)}
                {printf("theorem diophantine1_%d_%d_%d (x : Nat) (y : Nat) (h1 : x >= 1) (h2 : y >= 1) (h3 : %d ^ x + %d = %d ^ y) :", ["a", "b", "c", "a", "b", "c"], 4)}
                {print_word("  ", 4)}
                print_Lean4_prop_v1(12, 0);
                print_line(newline);
                {printf("  := by", [], 4)}
                {printf("  have h4 : x % 1 = 0 := by omega", [], 4)}
                {printf("  have h5 : y % 1 = 0 := by omega", [], 4)}  
                {printf("  by_cases h6 : x >= %d", ["dp_power"], 4)}
                {printf(f"  have h7 := Claim (%d ^ x {_slash}% %d = 0) [", ["a", "M"], 4)}   
                {printf("    {prop := x % 1 = 0, proof := h4},", [], 4)}
                {printf("    {prop := x >= %d, proof := h6},", ["dp_power"], 4)}   
                {printf('  ] "pow_mod_eq_zero"', [], 4)} 
                {printf(f"  have h8 : %d ^ y {_slash}% %d = %d := by omega", ["c", "M", "R"], 4)}
                {printf("  have h9 := Claim False [", [], 4)}   
                {printf("    {prop := y % 1 = 0, proof := h5},", [], 4)}
                {printf("    {prop := y >= 1, proof := h2},", [], 4)}   
                {printf(f"    {{prop := %d ^ y {_slash}% %d = %d, proof := h8}},", ["c", "M", "R"], 4)}
                {printf('  ] "observe_mod_cycle"', [], 4)}
                {printf("  apply False.elim h9", [], 4)}
                {printf("  have h7 : x <= %d := by omega", ["dp_power-1"], 4)}
                {print_word("  have h8 := Claim ", 4)}
                print_Lean4_prop_v1(12, 1);
                {printf(" [", [], 4)}
                {printf("    {prop :=  x % 1 = 0, proof := h4},", [], 4)}
                {printf("    {prop :=  x >= 1, proof := h1},", [], 4)}
                {printf("    {prop :=  y % 1 = 0, proof := h5},", [], 4)}
                {printf("    {prop :=  y >= 1, proof := h2},", [], 4)}
                {printf("    {prop := %d ^ x + %d = %d ^ y, proof := h3},", ["a", "b", "c"], 4)}
                {printf("    {prop := x <= %d, proof := h7},", ["dp_power-1"], 4)}
                {printf('  ] "diophantine1_front_enumeration"', [], 4)}
                {printf("  exact h8", [], 4)}
            // c ^ y = R (mod M) => y = yr (mod k)
            // e.g. 2 ^ x + 1 = 17 ^ y
            }}else{{
                int k = read_solution_v1();
                int P = read_solution_v1(); // magic prime
                int m = read_solution_v1(); // y = yr (mod k) => y = y1, y2, ..., y_npossibilities (mod m)
                int npossibilities = read_solution_v1();
                int i = 0;
                while (i < npossibilities) {{
                    read_solution_v1();
                    i = i + 1;
                }}
                int pointer1 = solution_v1_pointer;
                read_solution_v1();
                i = 0;
                while (i < npossibilities) {{
                    read_solution_v1();
                    i = i + 1;
                }}
                read_solution_v1();
                int pointer2 = solution_v1_pointer;
                read_solution_v1();
                i = 0;
                while (i < npossibilities) {{
                    read_solution_v1();
                    i = i + 1;
                }}
                read_solution_v1();
                {printf("/-", [], 4)}
                {printf("(Class II, Back Mode, with magic prime %d)   %d ^ x + %d = %d ^ y", ["P", "a", "b", "c"], 4)}
                print_solution_v1();
                {printf("-/", [], 4)}
                {printf("theorem diophantine1_%d_%d_%d (x : Nat) (y : Nat) (h1 : x >= 1) (h2 : y >= 1) (h3 : %d ^ x + %d = %d ^ y) :", ["a", "b", "c", "a", "b", "c"], 4)}
                {print_word("  ", 4)}
                print_Lean4_prop_v1(solution_v1_pointer, 0);
                print_line(newline);
                {printf("  := by", [], 4)}
                {printf("  have h4 : x % 1 = 0 := by omega", [], 4)}
                {printf("  have h5 : y % 1 = 0 := by omega", [], 4)}  
                {printf("  by_cases h6 : x >= %d", ["dp_power"], 4)}
                {printf(f"  have h7 := Claim (%d ^ x {_slash}% %d = 0) [", ["a", "M"], 4)}   
                {printf("    {prop := x % 1 = 0, proof := h4},", [], 4)}
                {printf("    {prop := x >= %d, proof := h6},", ["dp_power"], 4)}   
                {printf('  ] "pow_mod_eq_zero"', [], 4)} 
                {printf(f"  have h8 : %d ^ y {_slash}% %d = %d := by omega", ["c", "M", "R"], 4)}
                {printf(f"  have h9 := Claim (y {_slash}% %d = %d) [", ["k", "yr"], 4)}   
                {printf("    {prop := y % 1 = 0, proof := h5},", [], 4)}
                {printf("    {prop := y >= 1, proof := h2},", [], 4)}   
                {printf(f"    {{prop := %d ^ y {_slash}% %d = %d, proof := h8}},", ["c", "M", "R"], 4)}
                {printf('  ] "observe_mod_cycle"', [], 4)}

                {print_word("  have h10 := Claim (List.Mem (", 4)}
                putint(c);
                {print_word(" ^ y % ", 4)}
                putint(P);
                {print_word(") [", 4)}
                print_Lean4_int_array(pointer1);
                {printf("]) [", [], 4)}
                {printf("    {prop := y % 1 = 0, proof := h5},", [], 4)}
                {printf("    {prop := y >= 1, proof := h2},", [], 4)}
                {printf(f"    {{prop := y {_slash}% %d = %d, proof := h9}},", ["k", "yr"], 4)}
                {printf('  ] "utilize_mod_cycle"', [], 4)}

                {print_word("  have h11 := Claim (List.Mem (", 4)}
                putint(a);
                {print_word(" ^ x % ", 4)}
                putint(P);
                {print_word(") [", 4)}
                print_Lean4_int_array(pointer2);
                {printf("]) [", [], 4)}          
                {print_word("    {prop := List.Mem (", 4)}
                putint(c);
                {print_word(" ^ y % ", 4)}
                putint(P); 
                {print_word(") [", 4)}
                print_Lean4_int_array(pointer1); 
                {printf("], proof := h10},", [], 4)}
                {printf("    {prop := %d ^ x + %d = %d ^ y, proof := h3},", ["a", "b", "c"], 4)}
                {printf('  ] "compute_mod_sub"', [], 4)}

                {printf("  have h12 := Claim False [", [], 4)}
                {printf("    {prop := x % 1 = 0, proof := h4},", [], 4)}
                {printf("    {prop := x >= 1, proof := h1},", [], 4)}
                {print_word("    {prop := List.Mem (", 4)}
                putint(a);
                {print_word(" ^ x % ", 4)}
                putint(P);
                {print_word(") [", 4)}
                print_Lean4_int_array(pointer2);
                {printf("], proof := h11},", [], 4)}
                {printf('  ] "exhaust_mod_cycle"', [], 4)}

                {printf("  apply False.elim h12", [], 4)}
                {printf("  have h7 : x <= %d := by omega", ["dp_power-1"], 4)}
                {print_word("  have h8 := Claim ", 4)}
                print_Lean4_prop_v1(solution_v1_pointer, 1);
                {printf(" [", [], 4)}
                {printf("    {prop :=  x % 1 = 0, proof := h4},", [], 4)}
                {printf("    {prop :=  x >= 1, proof := h1},", [], 4)}
                {printf("    {prop :=  y % 1 = 0, proof := h5},", [], 4)}
                {printf("    {prop :=  y >= 1, proof := h2},", [], 4)}
                {printf("    {prop := %d ^ x + %d = %d ^ y, proof := h3},", ["a", "b", "c"], 4)}
                {printf("    {prop := x <= %d, proof := h7},", ["dp_power-1"], 4)}
                {printf('  ] "diophantine1_front_enumeration"', [], 4)}
                {printf("  exact h8", [], 4)}
            }}
        // Front Mode: Obtain x = xr (mod k) by disproof assumption and search series {{n*k + 1}} for an appropriate prime number
        }}else if (dp_type == 2) {{
            read_solution_v1();
            //If y >= dp_power, a ^ x = R (mod M).
            int R = read_solution_v1();
            int M = read_solution_v1();
            int xr = read_solution_v1();
            //However, a ^ x = R (mod M) is impossible.
            // e.g. 2 ^ x + 9 = 7 ^ y
            if (xr == -1) {{
                {printf("/-", [], 4)}
                {printf("(Class II, Front Mode, no magic prime)   %d ^ x + %d = %d ^ y", ["a", "b", "c"], 4)}
                print_solution_v1();
                {printf("-/", [], 4)}
                {printf("theorem diophantine1_%d_%d_%d (x : Nat) (y : Nat) (h1 : x >= 1) (h2 : y >= 1) (h3 : %d ^ x + %d = %d ^ y) :", ["a", "b", "c", "a", "b", "c"], 4)}
                {print_word("  ", 4)}
                print_Lean4_prop_v1(12, 0);
                print_line(newline);
                {printf("  := by", [], 4)}
                {printf("  have h4 : x % 1 = 0 := by omega", [], 4)}
                {printf("  have h5 : y % 1 = 0 := by omega", [], 4)}  
                {printf("  by_cases h6 : y >= %d", ["dp_power"], 4)}
                {printf(f"  have h7 := Claim (%d ^ y {_slash}% %d = 0) [", ["c", "M"], 4)}   
                {printf("    {prop := y % 1 = 0, proof := h5},", [], 4)}
                {printf("    {prop := y >= %d, proof := h6},", ["dp_power"], 4)}   
                {printf('  ] "pow_mod_eq_zero"', [], 4)} 
                {printf(f"  have h8 : %d ^ x {_slash}% %d = %d := by omega", ["a", "M", "R"], 4)}
                {printf("  have h9 := Claim False [", [], 4)}   
                {printf("    {prop := x % 1 = 0, proof := h4},", [], 4)}
                {printf("    {prop := x >= 1, proof := h1},", [], 4)}   
                {printf(f"    {{prop := %d ^ x {_slash}% %d = %d, proof := h8}},", ["a", "M", "R"], 4)}
                {printf('  ] "observe_mod_cycle"', [], 4)}
                {printf("  apply False.elim h9", [], 4)}
                {printf("  have h7 : y <= %d := by omega", ["dp_power-1"], 4)}
                {print_word("  have h8 := Claim ", 4)}
                                print_Lean4_prop_v1(12, 1);
                {printf(" [", [], 4)}
                {printf("    {prop :=  x % 1 = 0, proof := h4},", [], 4)}
                {printf("    {prop :=  x >= 1, proof := h1},", [], 4)}
                {printf("    {prop :=  y % 1 = 0, proof := h5},", [], 4)}
                {printf("    {prop :=  y >= 1, proof := h2},", [], 4)}
                {printf("    {prop := %d ^ x + %d = %d ^ y, proof := h3},", ["a", "b", "c"], 4)}
                {printf("    {prop := y <= %d, proof := h7},", ["dp_power-1"], 4)}
                {printf('  ] "diophantine1_back_enumeration"', [], 4)}
                {printf("  exact h8", [], 4)}
            // a ^ x = R (mod M) => x = xr (mod k)
            // e.g. 2 ^ x + 1 = 3 ^ y
            }}else{{
                int k = read_solution_v1();
                int P = read_solution_v1(); // magic prime
                int m = read_solution_v1(); // x = xr (mod k) => x = x1, x2, ..., x_npossibilities (mod m)
                int npossibilities = read_solution_v1();
                int i = 0;
                while (i < npossibilities) {{
                    read_solution_v1();
                    i = i + 1;
                }}
                int pointer1 = solution_v1_pointer;
                read_solution_v1();
                i = 0;
                while (i < npossibilities) {{
                    read_solution_v1();
                    i = i + 1;
                }}
                read_solution_v1();
                int pointer2 = solution_v1_pointer;
                read_solution_v1();
                i = 0;
                while (i < npossibilities) {{
                    read_solution_v1();
                    i = i + 1;
                }}
                read_solution_v1();
                {printf("/-", [], 4)}
                {printf("(Class II, Front Mode, with magic prime %d)   %d ^ x + %d = %d ^ y", ["P", "a", "b", "c"], 4)}
                print_solution_v1();
                {printf("-/", [], 4)}
                {printf("theorem diophantine1_%d_%d_%d (x : Nat) (y : Nat) (h1 : x >= 1) (h2 : y >= 1) (h3 : %d ^ x + %d = %d ^ y) :", ["a", "b", "c", "a", "b", "c"], 4)}
                {print_word("  ", 4)}
                print_Lean4_prop_v1(solution_v1_pointer, 0);
                print_line(newline);
                {printf("  := by", [], 4)}
                {printf("  have h4 : x % 1 = 0 := by omega", [], 4)}
                {printf("  have h5 : y % 1 = 0 := by omega", [], 4)}  
                {printf("  by_cases h6 : y >= %d", ["dp_power"], 4)}
                {printf(f"  have h7 := Claim (%d ^ y {_slash}% %d = 0) [", ["c", "M"], 4)}   
                {printf("    {prop := y % 1 = 0, proof := h5},", [], 4)}
                {printf("    {prop := y >= %d, proof := h6},", ["dp_power"], 4)}   
                {printf('  ] "pow_mod_eq_zero"', [], 4)} 
                {printf(f"  have h8 : %d ^ x {_slash}% %d = %d := by omega", ["a", "M", "R"], 4)}
                {printf(f"  have h9 := Claim (x {_slash}% %d = %d) [", ["k", "xr"], 4)}   
                {printf("    {prop := x % 1 = 0, proof := h4},", [], 4)}
                {printf("    {prop := x >= 1, proof := h1},", [], 4)}   
                {printf(f"    {{prop := %d ^ x {_slash}% %d = %d, proof := h8}},", ["a", "M", "R"], 4)}
                {printf('  ] "observe_mod_cycle"', [], 4)}

                {print_word("  have h10 := Claim (List.Mem (", 4)}
                putint(a);
                {print_word(" ^ x % ", 4)}
                putint(P);
                {print_word(") [", 4)}
                print_Lean4_int_array(pointer1);
                {printf("]) [", [], 4)}
                {printf("    {prop := x % 1 = 0, proof := h4},", [], 4)}
                {printf("    {prop := x >= 1, proof := h1},", [], 4)}
                {printf(f"    {{prop := x {_slash}% %d = %d, proof := h9}},", ["k", "xr"], 4)}
                {printf('  ] "utilize_mod_cycle"', [], 4)}

                {print_word("  have h11 := Claim (List.Mem (", 4)}
                putint(c);
                {print_word(" ^ y % ", 4)}
                putint(P);
                {print_word(") [", 4)}
                print_Lean4_int_array(pointer2);
                {printf("]) [", [], 4)}          
                {print_word("    {prop := List.Mem (", 4)}
                putint(a);
                {print_word(" ^ x % ", 4)}
                putint(P); 
                {print_word(") [", 4)}
                print_Lean4_int_array(pointer1); 
                {printf("], proof := h10},", [], 4)}
                {printf("    {prop := %d ^ x + %d = %d ^ y, proof := h3},", ["a", "b", "c"], 4)}
                {printf('  ] "compute_mod_add"', [], 4)}

                {printf("  have h12 := Claim False [", [], 4)}
                {printf("    {prop := y % 1 = 0, proof := h5},", [], 4)}
                {printf("    {prop := y >= 1, proof := h2},", [], 4)}
                {print_word("    {prop := List.Mem (", 4)}
                putint(c);
                {print_word(" ^ y % ", 4)}
                putint(P);
                {print_word(") [", 4)}
                print_Lean4_int_array(pointer2);
                {printf("], proof := h11},", [], 4)}
                {printf('  ] "exhaust_mod_cycle"', [], 4)}

                {printf("  apply False.elim h12", [], 4)}
                {printf("  have h7 : y <= %d := by omega", ["dp_power-1"], 4)}
                {print_word("  have h8 := Claim ", 4)}
                print_Lean4_prop_v1(solution_v1_pointer, 1);
                {printf(" [", [], 4)}
                {printf("    {prop :=  x % 1 = 0, proof := h4},", [], 4)}
                {printf("    {prop :=  x >= 1, proof := h1},", [], 4)}
                {printf("    {prop :=  y % 1 = 0, proof := h5},", [], 4)}
                {printf("    {prop :=  y >= 1, proof := h2},", [], 4)}
                {printf("    {prop := %d ^ x + %d = %d ^ y, proof := h3},", ["a", "b", "c"], 4)}
                {printf("    {prop := y <= %d, proof := h7},", ["dp_power-1"], 4)}
                {printf('  ] "diophantine1_back_enumeration"', [], 4)}
                {printf("  exact h8", [], 4)} 
            }} 
        }}else{{
            {make_assertion("0", "[Solver V1] solution vector format is incorrect for unknown reason!", 3)}
        }}
    }}else{{
        {make_assertion("0", "[Solver V1] solution vector format is incorrect for unknown reason!", 2)}
    }}
}}
"""