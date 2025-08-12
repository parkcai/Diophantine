import re
import math
from tqdm import tqdm
from os.path import sep as seperator
from pywheels.file_tools import append_to_file
from pywheels.file_tools import assert_file_exist
from .utils import *


def main():
    
    print("Please enter a value (press Enter to use the default):")
    a_max = get_integer_input("a_max", 500)
    a_min = get_integer_input("a_min", 500)
    b_max = get_integer_input("b_max", 500)
    c_max = get_integer_input("c_max", 500)
    exclude_trivial = get_boolean_input("exclude_trivial", True)

    progress_bar = tqdm(range((a_max - a_min + 1) * b_max))

    for a in range(a_min, a_max + 1):
        
        for b in range(1, b_max + 1):
            
            if exclude_trivial and math.gcd(a, b) >= 2: 
                progress_bar.update(1); continue
            
            lean_file_path = f"results{seperator}{a}-{b}.lean"
            
            assert_file_exist(lean_file_path)
            
            with open(
                file = lean_file_path, 
                mode = "r", 
                encoding = "UTF-8"
            ) as file_pointer:
                
                lean_code = file_pointer.read()
            
            valid = diophantine_rechecker.revalidate(
                lean_code = lean_code,
                mode = "string",
                show_progress = False,
            )
            
            if not valid: 
                
                append_to_file(
                    file_path = recorder_path, 
                    content = (
                        f"file {lean_file_path} not valid, "
                        f"error: {diophantine_rechecker.get_invalid_cause()}"
                    )
                )
                
            undesired_pattern = re.compile(r"failed|panic")
            
            if undesired_pattern.findall(lean_code):
                
                append_to_file(
                    file_path = recorder_path, 
                    content = (
                        f"file {lean_file_path} not valid, "
                        f"error: solver may have failed."
                    )
                )
                
            complete = True
            
            c = 2
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
            
            progress_bar.update(1)


if __name__ == "__main__":
    
    main()
