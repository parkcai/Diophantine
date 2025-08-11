from typing import List
from typing import Set
from meta.uid.uid_generator import *


__all__ = [
    "print_line_code",
    "printf",
    "print_word",
    "make_assertion",
]


string_uid_generator: UIDGenerator = UIDGenerator(seed = 42)


print_line_code_header = r"""void print_line(int line[]){
    if (!line[0]) return;
    int i = 0;
    while (line[i] != endl) { 
        putch(line[i]);   
        i = i + 1;   
    }
    putch(endl);
}


void print_word(int word[]) {
    int i = 0;
    while (word[i]) { 
        putch(word[i]);   
        i = i + 1;   
    }
}


void assert(int expr, int err_info[]) {
    assertion = expr;
    if (!assertion) {
        print_line(err_info);
    }
}
"""


print_line_code = print_line_code_header


print_line_func_type_recorder: Set[str] = set()

def printf(
    fstring: str,
    params: List[str],
    indent: int,
    generate_comment: bool = True,
    uid_length: int = 6,
)-> str:
    
    global print_line_code
    global string_uid_generator
    global print_line_func_type_recorder
    
    print_line_func_type = ""
    
    fstring_index = 0
    
    while fstring_index < len(fstring):
        
        if fstring[fstring_index] == "%":
            
            if fstring_index + 1 < len(fstring):
                
                if fstring[fstring_index + 1] in ["d", "s"]:
                    
                    print_line_func_type += fstring[fstring_index + 1]
                    fstring_index += 1
                    
        fstring_index += 1
        
    printf_code = ""
    printf_code_uid = string_uid_generator.generate(uid_length)
    
    if generate_comment:
        # printf_code += 4 * indent * " "
        printf_code += f'// "{fstring}"\n'
    
    ascii_values = [ord(char) for char in fstring]
    ascii_values.append(10)
    if generate_comment: printf_code += 4 * indent * " "
    printf_code += f"int string_{printf_code_uid}[{len(ascii_values)}] = {{{', '.join(map(str, ascii_values))}}};\n"
    
    printf_code += 4 * indent * " "
    if print_line_func_type != "":
        printf_code += f"print_line_with_{print_line_func_type}(string_{printf_code_uid}, {', '.join(params)});"
    else:
        printf_code += f"print_line(string_{printf_code_uid});"
    
    if print_line_func_type != "" and print_line_func_type not in print_line_func_type_recorder:
        print_line_func_type_recorder.add(print_line_func_type)
        print_line_code = get_print_line_code()
        
    return printf_code


def get_print_line_func_code(
    print_line_func_type: str
) -> str:
    
    print_line_code: str = ""

    print_line_code += f"void print_line_with_{print_line_func_type}(int line[]"
    for arg_no in range(1, len(print_line_func_type)+1):
        if print_line_func_type[arg_no - 1] == "s":
            print_line_code += f", int arg{arg_no}[]"
        else:
            print_line_code += f", int arg{arg_no}"
    print_line_code += ") {\n"
    print_line_code += "    if (!line[0]) return;\n"
    print_line_code += "    int i = 0;\n"
    print_line_code += "    int count = 1;\n"
    print_line_code += "    while (line[i] != endl) {\n"
    print_line_code += "        if (line[i] != percentage) {\n"
    print_line_code += "            if (line[i] != backslash) {\n"
    print_line_code += "                putch(line[i]);\n"
    print_line_code += "                i = i + 1;\n"
    print_line_code += "            }else{\n"
    print_line_code += "                putch(line[i+1]);\n"
    print_line_code += "                i = i + 2;\n"
    print_line_code += "            }\n"
    print_line_code += "        }else{\n"
    
    for arg_no in range(1, len(print_line_func_type)+1):
        if arg_no == 1:
            print_line_code += f"            if (count == {arg_no}) {{\n"
        else:
            print_line_code += f"            else if (count == {arg_no}) {{\n"
        
        if print_line_func_type[arg_no - 1] == "d":
            print_line_code += f"                putint(arg{arg_no});\n"
        else:
            print_line_code += f"                print_word(arg{arg_no});\n"
        print_line_code += "            }\n"

    print_line_code += "            i = i + 2;\n"
    print_line_code += "            count = count + 1;\n"
    print_line_code += "        }\n"
    print_line_code += "    }\n"
    print_line_code += "    putch(endl);\n"
    print_line_code += "}\n"

    return print_line_code


def get_print_line_code()-> str:
    
    global print_line_code_header
    global print_line_func_type_recorder
    
    print_line_code = print_line_code_header
    
    sorted_func_type_recorder = sorted(print_line_func_type_recorder, key=lambda s: (len(s), s))
    for func_type in sorted_func_type_recorder:
        print_line_code += f"""
        
{get_print_line_func_code(func_type)}"""
    
    return print_line_code


def print_word(
    word: str,
    indent: int,
    generate_comment: bool = True,
    uid_length: int = 6,
)-> str:
    
    global string_uid_generator
        
    print_word_code = ""
    print_word_code_uid = string_uid_generator.generate(uid_length)
    
    if generate_comment:
        print_word_code += 4 * indent * " "
        print_word_code += f'// "{word}"\n'
    
    ascii_values = [ord(char) for char in word]
    ascii_values.append(0)
    print_word_code += 4 * indent * " "
    print_word_code += f"int string_{print_word_code_uid}[{len(ascii_values)}] = {{{', '.join(map(str, ascii_values))}}};\n"
    
    print_word_code += 4 * indent * " "
    print_word_code += f"print_word(string_{print_word_code_uid});"
        
    return print_word_code


def make_assertion(
    assertion: str,
    error: str,
    indent: int,
    return_zero: bool = False,
    generate_comment: bool = True,
    uid_length: int = 6,
)-> str:

    assertion_code: str = ""
    
    if generate_comment:
        # assertion_code += 4 * indent * " "
        assertion_code += f'// "{error}"\n'
        
    assertion_code_uid = string_uid_generator.generate(uid_length)
    ascii_values = [ord(char) for char in error]
    ascii_values.append(10)
    if generate_comment: assertion_code += 4 * indent * " "
    assertion_code += f"int array_{assertion_code_uid}[{len(ascii_values)}] = {{{', '.join(map(str, ascii_values))}}};\n"
        
    assertion_code += 4 * indent * " "
    assertion_code += f"assert({assertion}, array_{assertion_code_uid});\n"
    
    assertion_code += 4 * indent * " "
    if return_zero:
        assertion_code += "if (!assertion) return 0;"
    else:
        assertion_code += "if (!assertion) return;"
        
    return assertion_code


if __name__ == "__main__":
    
    pass
    
    
