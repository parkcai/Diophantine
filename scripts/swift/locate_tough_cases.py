import re
import sys
import subprocess
from tqdm import tqdm
from pywheels.asker import get_integer_input
from pywheels.file_tools import append_to_file


def try_diophantine_case(a, b, c, silent = False):
    
    try:
    
        run_diophantine_timeout_seconds = 5
        
        exclude_trivial = False
        input_data = f"2 {1 if exclude_trivial else 0} {a} {a} {b} {b} {c} {c}"
        
        output_path = "scripts/swift/tmp.lean"
        input_encoding = "UTF-8"
        output_encoding = "UTF-8"
        diophantine_exec_path = "diophantine.exe" \
            if sys.platform == "win32" else "diophantine"
        
        with open(
            file = output_path, 
            mode = "w", 
            encoding = output_encoding,
        ) as out:
        
            subprocess.run(
                diophantine_exec_path,
                input = input_data.encode(input_encoding),
                stdout = out,
                stderr = subprocess.PIPE,
                timeout = run_diophantine_timeout_seconds,
            )
            
    except Exception as error:
        
        if not silent:
        
            append_to_file("scripts/swift/swift.out", f"Case {a} {b} {c}: {error}")


def main():
    
    abc_tuples = []
    
    with open(
        file = "command_output.txt", 
        mode = "r",
        encoding = "UTF-8",
    ) as file_pointer:
        
        for line in file_pointer:
            
            a, b = map(int, re.findall(r"\d+", line.strip())[:2])
            
            for c in range(2, 501): abc_tuples.append((a, b, c))
            
    a_start = get_integer_input("请输入断点续跑的 a 值", abc_tuples[0][0])
    b_start = get_integer_input("请输入断点续跑的 b 值", abc_tuples[0][1])
                
    for a, b, c in tqdm(abc_tuples): 
        
        if a < a_start or (a == a_start and b < b_start): continue
        
        try_diophantine_case(a, b, c)


if __name__ == "__main__":
    
    main()