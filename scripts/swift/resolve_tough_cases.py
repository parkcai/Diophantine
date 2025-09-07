import re
import sys
import subprocess
from tqdm import tqdm
from typing import Dict, Tuple
from pywheels.file_tools import append_to_file
from pywheels.file_tools import clear_file


tough_case_recorder_path = "scripts/swift/swift.out"
logger_path = "scripts/swift/log.txt"
result_path = "scripts/swift/result.txt"


existing_tunings = r"""    if (a == 31 && b == 2 && c == 47) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 31 && b == 4 && c == 47) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 31 && b == 4 && c == 53) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 31 && b == 138 && c == 173) { max_trial_num_v1 = 3; mod_threshold_v1 = 1000000000; return; }
    if (a == 43 && b == 21 && c == 59) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 43 && b == 21 && c == 101) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 43 && b == 21 && c == 107) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 43 && b == 44 && c == 107) { max_trial_num_v1 = 10; mod_threshold_v1 = 1000000000; return; }
    if (a == 43 && b == 47 && c == 107) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 47 && b == 49 && c == 59) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 47 && b == 81 && c == 73) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 47 && b == 81 && c == 83) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 47 && b == 84 && c == 19) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 47 && b == 84 && c == 59) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 47 && b == 84 && c == 83) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 47 && b == 84 && c == 89) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 47 && b == 84 && c == 107) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 47 && b == 91 && c == 31) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 47 && b == 96 && c == 59) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 47 && b == 97 && c == 59) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 47 && b == 102 && c == 59) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 47 && b == 122 && c == 31) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 59 && b == 31 && c == 47) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 59 && b == 73 && c == 47) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 59 && b == 87 && c == 47) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 59 && b == 99 && c == 47) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 59 && b == 42 && c == 67) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 59 && b == 42 && c == 83) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 59 && b == 42 && c == 89) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 59 && b == 85 && c == 83) { max_trial_num_v1 = 10; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 7 && c == 59) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 11 && c == 59) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 18 && c == 19) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 21 && c == 59) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 29 && c == 59) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 30 && c == 59) { max_trial_num_v1 = 10; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 33 && c == 47) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 33 && c == 89) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 33 && c == 173) { max_trial_num_v1 = 5; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 40 && c == 59) { max_trial_num_v1 = 10; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 51 && c == 59) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 61 && c == 59) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 78 && c == 59) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 78 && c == 173) { max_trial_num_v1 = 5; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 84 && c == 59) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 84 && c == 89) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 84 && c == 107) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 85 && c == 47) { max_trial_num_v1 = 50; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 90 && c == 173) { max_trial_num_v1 = 5; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 93 && c == 89) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 94 && c == 59) { max_trial_num_v1 = 10; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 95 && c == 59) { max_trial_num_v1 = 10; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 106 && c == 59) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 110 && c == 193) { max_trial_num_v1 = 5; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 114 && c == 197) { max_trial_num_v1 = 7; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 143 && c == 179) { max_trial_num_v1 = 2; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 196 && c == 197) { max_trial_num_v1 = 2; mod_threshold_v1 = 1000000000; return; }
    if (a == 83 && b == 197 && c == 173) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 107 && b == 22 && c == 43) { max_trial_num_v1 = 8; mod_threshold_v1 = 1000000000; return; }
    if (a == 107 && b == 34 && c == 59) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 107 && b == 82 && c == 43) { max_trial_num_v1 = 25; mod_threshold_v1 = 1000000000; return; }
    if (a == 149 && b == 90 && c == 239) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 6 && c == 173) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 9 && c == 179) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 14 && c == 181) { max_trial_num_v1 = 2; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 16 && c == 179) { max_trial_num_v1 = 9; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 31 && c == 179) { max_trial_num_v1 = 9; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 32 && c == 199) { max_trial_num_v1 = 2; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 56 && c == 223) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 62 && c == 229) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 65 && c == 179) { max_trial_num_v1 = 8; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 66 && c == 233) { max_trial_num_v1 = 5; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 72 && c == 239) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 74 && c == 241) { max_trial_num_v1 = 2; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 124 && c == 47) { max_trial_num_v1 = 3; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 124 && c == 239) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 188 && c == 173) { max_trial_num_v1 = 3; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 191 && c == 179) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 194 && c == 173) { max_trial_num_v1 = 2; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 198 && c == 199) { max_trial_num_v1 = 2; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 211 && c == 173) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 215 && c == 241) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 167 && b == 231 && c == 179) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 173 && b == 41 && c == 167) { max_trial_num_v1 = 2; mod_threshold_v1 = 1000000000; return; }
    if (a == 173 && b == 90 && c == 167) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 173 && b == 92 && c == 167) { max_trial_num_v1 = 2; mod_threshold_v1 = 1000000000; return; }
    if (a == 173 && b == 118 && c == 83) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 173 && b == 159 && c == 167) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 173 && b == 233 && c == 83) { max_trial_num_v1 = 2; mod_threshold_v1 = 1000000000; return; }
    if (a == 179 && b == 4 && c == 227) { max_trial_num_v1 = 3; mod_threshold_v1 = 1000000000; return; }
    if (a == 179 && b == 36 && c == 181) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 179 && b == 41 && c == 167) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 179 && b == 55 && c == 167) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 179 && b == 60 && c == 239) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 179 && b == 71 && c == 167) { max_trial_num_v1 = 9; mod_threshold_v1 = 1000000000; return; }
    if (a == 179 && b == 74 && c == 227) { max_trial_num_v1 = 3; mod_threshold_v1 = 1000000000; return; }
    if (a == 179 && b == 88 && c == 227) { max_trial_num_v1 = 2; mod_threshold_v1 = 1000000000; return; }
    if (a == 179 && b == 103 && c == 167) { max_trial_num_v1 = 4; mod_threshold_v1 = 1000000000; return; }
    if (a == 179 && b == 106 && c == 167) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 179 && b == 136 && c == 167) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 179 && b == 143 && c == 167) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 179 && b == 149 && c == 167) { max_trial_num_v1 = 9; mod_threshold_v1 = 1000000000; return; }
    if (a == 179 && b == 228 && c == 227) { max_trial_num_v1 = 3; mod_threshold_v1 = 1000000000; return; }
    if (a == 179 && b == 240 && c == 167) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 179 && b == 240 && c == 181) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 181 && b == 7 && c == 8) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 181 && b == 7 && c == 32) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 197 && b == 166 && c == 167) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 223 && b == 18 && c == 241) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 227 && b == 33 && c == 179) { max_trial_num_v1 = 3; mod_threshold_v1 = 1000000000; return; }
    if (a == 227 && b == 38 && c == 179) { max_trial_num_v1 = 4; mod_threshold_v1 = 1000000000; return; }
    if (a == 227 && b == 69 && c == 179) { max_trial_num_v1 = 2; mod_threshold_v1 = 1000000000; return; }
    if (a == 227 && b == 134 && c == 239) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 227 && b == 242 && c == 241) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 233 && b == 38 && c == 227) { max_trial_num_v1 = 3; mod_threshold_v1 = 1000000000; return; }
    if (a == 239 && b == 73 && c == 179) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 239 && b == 79 && c == 179) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 239 && b == 131 && c == 179) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 239 && b == 233 && c == 227) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
    if (a == 241 && b == 32 && c == 179) { max_trial_num_v1 = 1; mod_threshold_v1 = 1000000000; return; }
"""


def extract_abc_and_hp_from_existing_tuning(tuning: str):
    # 移除首尾空白字符
    tuning = tuning.strip()
    
    # 使用正则表达式匹配所有数值
    # 匹配模式：数字序列（可能包含负号，但你的例子中都是正数）
    pattern = r'(-?\d+)'
    numbers = re.findall(pattern, tuning)
    
    # 确保找到至少5个数字
    if len(numbers) < 5:
        raise ValueError(f"Expected at least 5 numbers, but found {len(numbers)}: {numbers}")
    
    # 转换为整数并返回前5个
    return (int(numbers[0]), int(numbers[1]), int(numbers[2]), int(numbers[4]), int(numbers[6]))

def extract_abc_from_tough_case(tough_case: str):
    # 移除首尾空白字符
    tough_case = tough_case.strip()
    
    # 找到"Case "之后的部分
    case_start = tough_case.find('Case ') + 5
    # 找到第一个冒号之前的部分
    case_end = tough_case.find(':')
    
    # 提取数字部分
    numbers_str = tough_case[case_start:case_end]
    # 按空格分割数字
    numbers = numbers_str.split()
    
    # 转换为整数并返回三元组
    return (int(numbers[0]), int(numbers[1]), int(numbers[2]))


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
    
    hps = [
        (i, 1000000000) for i in range(1, 26)
    ]
    
    hp_of_bad_case: Dict[Tuple[int, int, int], Tuple[int, int]] = {}
    
    bad_cases = set()
    
    for tuning in existing_tunings.splitlines():
        
        a, b, c, x, y = extract_abc_and_hp_from_existing_tuning(tuning)
        hp_of_bad_case[(a, b, c)] = (x, y)
        bad_cases.add((a, b, c))
        
    with open(
        file = tough_case_recorder_path,
        mode = "r",
        encoding = "UTF-8",
    ) as file_pointer:
        
        lines = file_pointer.readlines()
        
    for line in lines:
        
        a, b, c = extract_abc_from_tough_case(line)
        
        bad_cases.add((a, b, c))
        
    clear_file(logger_path)
        
    for hp in hps:
        
        append_to_file(logger_path, f"现在开始尝试超参{hp}，还有 {len((bad_cases - set(hp_of_bad_case.keys())))} 个 bad case 未解决！")
        
        for a, b, c in tqdm((bad_cases - set(hp_of_bad_case.keys()))):
            if try_diophantine_case(a, b, c, *hp): hp_of_bad_case[(a, b, c)] = hp
            
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
        
        
    
        
        
    