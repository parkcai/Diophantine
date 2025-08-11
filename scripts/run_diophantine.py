import sys
import math
import subprocess
from tqdm import tqdm
from os.path import sep as seperator
from pywheels.file_tools import delete_file
from pywheels.file_tools import assert_file_exist
from pywheels.file_tools import guarantee_file_exist
from .utils import *


def execute_diophantine(
    input_data: str, 
    output_path: str, 
    exe_path: str
):
    
    with open(
        file = output_path, 
        mode = "w", 
        encoding = "UTF-8"
    ) as out:
        
        proc = subprocess.run(
            exe_path,
            input = input_data.encode("UTF-8"),
            stdout = out,
            stderr = subprocess.PIPE,
        )

    if proc.returncode != 0:
        
        raise RuntimeError(f"【Diophantine 执行错误】{proc.stderr.decode('UTF-8')}")


def main():
    
    guarantee_file_exist("results", is_directory=True)
    
    diophantine_exec_path = "diophantine.exe" if sys.platform == "win32" else "diophantine"
    
    assert_file_exist(diophantine_exec_path, f"请先生成 diophantine.c 并编译至 {diophantine_exec_path}！")

    print("请输入参数范围（直接回车使用默认值）：")
    a_max = get_integer_input("a_max", 500)
    b_max = get_integer_input("b_max", 500)
    c_max = get_integer_input("c_max", 500)
    
    progress_bar = tqdm(range((a_max - 1) * b_max), smoothing = 0)

    for a in range(2, a_max + 1):
        
        for b in range(1, b_max + 1):
            
            lean_file_path = f"results{seperator}{a}-{b}.lean"
            
            if math.gcd(a, b) >= 2:
                
                delete_file(lean_file_path)
                
            else:
                
                execute_diophantine(
                    input_data = f"2 {a} {a} {b} {b} {c_max} 2", 
                    output_path = f"results{seperator}{a}-{b}.lean", 
                    exe_path = diophantine_exec_path
                )
                    
            progress_bar.update(1)
    
    
if __name__ == "__main__":
    
    main()
