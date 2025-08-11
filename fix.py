import re
from tqdm import tqdm
from os.path import sep as seperator
from scripts.run_diophantine import execute_diophantine


def lines(
    file_path: str, 
    encoding: str = "UTF-8",
):
    with open(
        file = file_path, 
        mode = "r", 
        encoding = encoding
    ) as file_pointer:
        
        for raw in file_pointer:
            yield raw.rstrip("\r\n")
            
            
lean_files_to_fix = []

fix_pattern = re.compile(
    r"file results\\(\d+)-(\d+)\.lean not valid, error: solver may have failed\."
)

for line in lines("command_output.txt"):
    
    fix_match = fix_pattern.fullmatch(line)
    
    if not fix_match: continue
    
    a: int = int(fix_match.group(1))
    b: int = int(fix_match.group(2)) 
    
    lean_files_to_fix.append((a, b))
    
    
for a, b in tqdm(lean_files_to_fix):
    
    execute_diophantine(
        input_data = f"2 {a} {a} {b} {b} 500 2", 
        output_path = f"results{seperator}{a}-{b}.lean", 
        exe_path = "diophantine.exe"
    )
