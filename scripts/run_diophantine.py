import math
import subprocess
from tqdm import tqdm
from typing import Optional
from os import cpu_count
from os.path import sep as seperator
from pywheels.file_tools import delete_file
from pywheels.file_tools import append_to_file
from pywheels.file_tools import guarantee_file_exist
from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor
from .utils import *


def execute_diophantine(
    input_data: str, 
    output_path: str, 
    timeout: bool,
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
            timeout = run_diophantine_timeout_seconds if timeout else None,
        )

    if process.returncode != 0:
        
        raise RuntimeError(
            f"【Diophantine 执行错误】{process.stderr.decode(error_encoding)}"
        )


def main():
    
    guarantee_file_exist("results", is_directory=True)
    
    a_max, a_min, b_max, b_min, c_max, c_min, a_start, b_start, exclude_trivial, timeout = \
        get_diophantine_parameters()
        
    # multi_thread = get_boolean_input("multi_thread", True)
    multi_thread = False
    
    clear_all_previous_results = get_boolean_input("clear_all_previous_results", False)
    
    if clear_all_previous_results: delete_file("results"); guarantee_file_exist("results", True)

    tasks = []
    
    for a in range(a_min, a_max + 1):
        for b in range(b_min, b_max + 1):
            
            if not (a >= (a_start + 1) or (a == a_start and b >= b_start)):
                continue
            
            if exclude_trivial and math.gcd(a, b) >= 2:
                continue
            
            tasks.append((a, b))
            
    progress_bar = tqdm(
        total = len(tasks), 
        smoothing = 0,
    )
    
    def process_task(a, b):
        
        lean_file_path = f"results{seperator}{a}-{b}.lean"
        
        try:
            
            execute_diophantine(
                input_data = f"2 {1 if exclude_trivial else 0} {a} {a} {b} {b} {c_max} {c_min}",
                output_path = lean_file_path,
                timeout = timeout,
            )
            
        except subprocess.TimeoutExpired:
            
            append_to_file(
                file_path=recorder_path, 
                content=(
                    f"file {lean_file_path} not successfully generated, "
                    f"error: timeout!"
                )
            )
            
        finally: progress_bar.update(1)

    with ThreadPoolExecutor(
        max_workers = cpu_count() if multi_thread else 1,
    ) as executor:
        
        future_to_task = {
            executor.submit(process_task, a, b): (a, b)
            for a, b in tasks
        }
        
        for future in as_completed(future_to_task):
            a, b = future_to_task[future]
            
            try:
                future.result()
                
            except Exception as e:
                append_to_file(
                    file_path=recorder_path,
                    content=f"Unexpected error processing task a={a}, b={b}: {str(e)}"
                )
    
    progress_bar.close()

    
if __name__ == "__main__":
    
    main()
