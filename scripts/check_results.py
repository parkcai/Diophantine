import math
from tqdm import tqdm
from os.path import sep as seperator
from pywheels.file_tools import append_to_file
from pywheels.file_tools import assert_file_exist
from pywheels.task_runner import execute_command
from .utils import *


def main():
    
    a_max, a_min, b_max, b_min, c_max, c_min, a_start, b_start, exclude_trivial, timeout = \
        get_diophantine_parameters()

    progress_bar = tqdm(range((a_max - a_min + 1) * (b_max - b_min + 1)))

    for a in range(a_min, a_max + 1):
        for b in range(b_min, b_max + 1):
            
            if not(a >= (a_start + 1) or (a == a_start and b >= b_start)):
                progress_bar.update(1); continue
            
            if exclude_trivial and math.gcd(a, b) >= 2: 
                progress_bar.update(1); continue
            
            lean_file_path = f"results{seperator}{a}-{b}.lean"
            
            try:
                assert_file_exist(lean_file_path)
                
            except Exception as _:
                
                append_to_file(
                    file_path = recorder_path, 
                    content = (
                        f"file {lean_file_path} not valid, "
                        f"error: {lean_file_path} doesn't exist!"
                    )
                )
                
                progress_bar.update(1); continue
                
            try:

                result = execute_command(f"lean --run {lean_file_path}")

                assert result["stdout"] == "Native Lean4 check passed.\n"

            except Exception as _:
                
                append_to_file(
                    file_path = recorder_path, 
                    content = (
                        f"file {lean_file_path} not valid, "
                        f"error: failed native Lean4 check!"
                    )
                )
                
                progress_bar.update(1); continue
                
            progress_bar.update(1)


if __name__ == "__main__":
    
    main()
