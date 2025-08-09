from .config import *
from .SysY.basic import *
from .SysY.utils import *
from .code.docstring import *
from .code.include import *
from .code.math.arithmetic import *
from .code.math.prime_list import *
from .code.solver.api import *
from .code.solver.solver_v1 import *
from .code.solver.lean4_generator import *
from .SysY.printf import *


section_comment_decorator = "------------------------------"


main_code = f"""int main() {{
    while (1) {{
        int usage = getint();
        if (usage == 0) {{
            Solve_Diophantine1_info();
        }}else if (usage == 1) {{
            Solve_Diophantine1_shell();
        }}else if (usage == 2) {{
            Solve_Diophantine1_research();
        }}else if (usage == 3) {{
            Solve_Diophantine1_document();
        }}else if (usage == -1) {{
            Solve_Diophantine1_backdoor();
            continue;
        }}else{{
{printf("Unknown usage %d, try ./diophantine 0/1/2/3!", ["usage"], 3)}
        }}
        return 0;
    }}
    
}}
"""


def main():
     
    diophantine_code_path = "diophantine.c"
    
    if not is_toy:
        
        SysY_header_code = f"""
{include_stdio_code}

// {section_comment_decorator} SysY basic section {section_comment_decorator}

{putch_code}

{putint_code}

{getint_code}"""

    else:
        
        SysY_header_code = ""

    diophantine_code = f"""{docstring_code}   
{SysY_header_code}
// {section_comment_decorator} SysY utils section {section_comment_decorator}

{SysY_utils_globals_code}
// {section_comment_decorator} SysY printf section {section_comment_decorator}

{print_line_code}
// {section_comment_decorator} arithmetic section {section_comment_decorator}

{greatest_common_divisor_code}

{least_common_multiple_code}

{get_power_cycle_mod_code}

{get_power_position_mod_code}

{is_prime_code}

{power_code}

{contain_undividable_prime_part_code}

{get_power_times_over_code}

{get_degree_wrt_code}

{is_power_of_code}

{get_value_mod_code}
// {section_comment_decorator} prime list section {section_comment_decorator}

{prime_list_code}
// {section_comment_decorator} solver v1 section {section_comment_decorator}

{solver_v1_globals_code}

{set_abc_v1_code}

{set_xy_name_v1_code}

{write_solution_v1_code}

{read_solution_v1_code}

{resume_solution_v1_code}

{Solve_Diophantine1_II_disproof_A_code}

{Solve_Diophantine1_II_disproof_C_code}

{insert_disproof_evidence_code}

{get_disproof_evidence_code}

{Solve_Diophantine1_I_i_code}

{Solve_Diophantine1_I_ii_code}

{Solve_Diophantine1_I_iii_code}

{Solve_Diophantine1_II_code}

{Solve_Diophantine1_code}

{exhaust_solution_v1_code}

{print_solution_v1_code}

{print_Lean4_prop_v1_code}

{print_Lean4_int_array_code}

{generate_Lean4_code_v1_code}
// {section_comment_decorator} api section {section_comment_decorator}

{Solve_Diophantine1_generate_Lean4_code}

{Solve_Diophantine1_backdoor_code}

{Solve_Diophantine1_info_code}

{Solve_Diophantine1_shell_code}

{Solve_Diophantine1_research_code}

{Solve_Diophantine1_document_code}
// {section_comment_decorator} program entrance {section_comment_decorator}

{main_code}
"""

    with open(
        file = diophantine_code_path,
        mode = "w",
        encoding = "UTF-8",
    ) as file:

        file.write(diophantine_code)


if __name__ == "__main__":
    
    main()