
import math
import subprocess
from tqdm import tqdm
from os.path import sep as seperator
from pywheels.file_tools import delete_file
from pywheels.file_tools import guarantee_file_exist
from .utils import *


def execute_diophantine(
    input_data: str, 
    output_path: str, 
    input_encoding: str = "UTF-8",
    output_encoding: str = "UTF-8",
    error_encoding: str = "UTF-8",
):
    
    with open(
        file = output_path, 
        mode = "w", 
        encoding = output_encoding,
    ) as out:
        
        process = subprocess.run(
            diophantine_exec_path,
            input = input_data.encode(input_encoding),
            stdout = out,
            stderr = subprocess.PIPE,
        )

    if process.returncode != 0:
        
        raise RuntimeError(
            f"【Diophantine 执行错误】{process.stderr.decode(error_encoding)}"
        )


def main():
    
    guarantee_file_exist("results", is_directory=True)
    
    a_max, a_min, b_max, b_min, c_max, c_min, a_start, b_start, exclude_trivial = \
        get_diophantine_parameters()
    
    clear_all_previous_results = get_boolean_input("clear_all_previous_results", True)
    
    if clear_all_previous_results:
        delete_file("results"); guarantee_file_exist("results", True)
    
    progress_bar = tqdm(range((a_max - a_min + 1) * (b_max - b_min + 1)), smoothing = 0)

    for a in range(a_min, a_max + 1):
        for b in range(b_min, b_max + 1):
            
            if not(a >= (a_start + 1) or (a == a_start and b >= b_start)):
                progress_bar.update(1); continue
            
            if exclude_trivial and math.gcd(a, b) >= 2:
                progress_bar.update(1); continue
                
            execute_diophantine(
                input_data = f"2 {1 if exclude_trivial else 0} {a} {a} {b} {b} {c_max} {c_min}", 
                output_path = f"results{seperator}{a}-{b}.lean", 
            )
                    
            progress_bar.update(1)
    
    
if __name__ == "__main__":
    
    main()
