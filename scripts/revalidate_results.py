import re
import math
from tqdm import tqdm
from os.path import sep as seperator
from pywheels.file_tools import append_to_file
from pywheels.file_tools import assert_file_exist
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError
from .utils import *


def main():
    
    a_max, a_min, b_max, b_min, c_max, c_min, a_start, b_start, exclude_trivial = \
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
            
            with open(
                file = lean_file_path, 
                mode = "r", 
                encoding = "UTF-8"
            ) as file_pointer:
                
                lean_code = file_pointer.read()
            
            with ThreadPoolExecutor(
                max_workers=1
            ) as executor:
                
                future = executor.submit(
                    diophantine_rechecker.revalidate,
                    lean_code = lean_code,
                    mode = "string",
                    show_progress = False,
                )
                
                try:
                    valid = future.result(
                        timeout = revalidate_timeout_seconds,
                    )
                    
                except TimeoutError:
                    
                    append_to_file(
                        file_path = recorder_path, 
                        content = (
                            f"file {lean_file_path} not valid, "
                            f"error: timeout!"
                        )
                    )
                    
                    progress_bar.update(1); continue
            
            if not valid: 
                
                append_to_file(
                    file_path = recorder_path, 
                    content = (
                        f"file {lean_file_path} not valid, "
                        f"error: {diophantine_rechecker.get_invalid_cause()}"
                    )
                )
                
                progress_bar.update(1); continue
                
            undesired_pattern = re.compile(r"failed|panic")
            
            if undesired_pattern.findall(lean_code):
                
                append_to_file(
                    file_path = recorder_path, 
                    content = (
                        f"file {lean_file_path} not valid, "
                        f"error: solver may have failed."
                    )
                )
                
                progress_bar.update(1); continue
                
            complete = True
            
            c = c_min
            while (c <= c_max):
                
                if exclude_trivial and (math.gcd(a, c) >= 2 or math.gcd(b, c) >= 2): 
                    c += 1; continue
                
                if f"theorem diophantine1_{a}_{b}_{c}" not in lean_code:
                    complete = False; break
                    
                c += 1
                    
            if not complete:
                
                append_to_file(
                    file_path = recorder_path, 
                    content = (
                        f"file {lean_file_path} not valid, "
                        f"error: theorem diophantine1_{a}_{b}_{c} missing."
                    )
                )
                
                progress_bar.update(1); continue
            
            progress_bar.update(1)


if __name__ == "__main__":
    
    main()
