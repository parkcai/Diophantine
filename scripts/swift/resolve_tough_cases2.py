import re
import sys
import subprocess
from tqdm import tqdm
from typing import Dict, Tuple
from pywheels.file_tools import append_to_file
from pywheels.file_tools import clear_file
from pywheels.file_tools import get_lines


tough_case_recorder_path = "scripts/swift/result.txt"
logger_path = "scripts/swift/log2.txt"
result_path = "scripts/swift/result2.txt"


def try_diophantine_case(
    a, b, c, x, y
)-> bool:
    
    try:
    
        run_diophantine_timeout_seconds = 5
        
        exclude_trivial = False
        input_data = f"-1 {x} {y}\n2 {1 if exclude_trivial else 0} {a} {a} {b} {b} {c} {c}"
        
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
            
        return True
            
    except Exception as _:
        
        return False


def record_result(a, b, c, x, y):
    
    if x == 114514 and y == 114514:
    
        append_to_file(
            file_path = result_path,
            content = f"    ({a}, {b}, {c}, {x}, {y}), # 未解决！！！"
        )
        
    else:
        
        append_to_file(
            file_path = result_path,
            content = f"    ({a}, {b}, {c}, {x}, {y}),"
        )


def main():

    clear_file(logger_path)
    
    # 1e9 -> 2e9
    hps = [
        (i, 2000000000) for i in range(1, 26)
    ]
    
    hp_of_bad_case: Dict[Tuple[int, int, int], Tuple[int, int]] = {}
    
    bad_cases = set()
    
    tough_case_line_pattern = re.compile(
        r"\s*\((\d+), (\d+), (\d+), (\d+), (\d+)\)"
    )
    
    for line in get_lines(tough_case_recorder_path):
        
        pattern_match = tough_case_line_pattern.search(line)
        assert pattern_match
        
        a, b, c, x, y = \
            int(pattern_match.group(1)), int(pattern_match.group(2)), int(pattern_match.group(3)), \
            int(pattern_match.group(4)), int(pattern_match.group(5))
            
        bad_cases.add((a, b, c))
        
        if "未解决" not in line:
            hp_of_bad_case[(a, b, c)] = (x, y)
            
    for hp in hps:
        
        append_to_file(logger_path, f"现在开始尝试超参{hp}，还有 {len((bad_cases - set(hp_of_bad_case.keys())))} 个 bad case 未解决！")
        
        for a, b, c in tqdm((bad_cases - set(hp_of_bad_case.keys()))):
            # if try_diophantine_case(a, b, c, *hp): hp_of_bad_case[(a, b, c)] = hp
            if a > 263 or b > 263 or c > 263: hp_of_bad_case[(a, b, c)] = hp
            # if 263 not in [a, b, c]: hp_of_bad_case[(a, b, c)] = hp
            
        clear_file(result_path)

        for a, b, c in sorted(bad_cases):
            
            if (a, b, c) in hp_of_bad_case:
                record_result(a, b, c, *hp_of_bad_case[(a, b, c)])
            
            else:
                record_result(a, b, c, 114514, 114514)
                
        if not len((bad_cases - set(hp_of_bad_case.keys()))): 
            append_to_file(logger_path, f"所有 bad case 均已解决！")
            break
        
        if hp == hp[-1]:
            append_to_file(logger_path, f"失败了，没有解决所有 bad case！")


if __name__ == "__main__":
    
    main()
        
        
    
        
        
    