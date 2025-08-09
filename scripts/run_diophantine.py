import math
import subprocess
from tqdm import tqdm
from os.path import sep as seperator
from pywheels.file_tools import delete_file
from pywheels.file_tools import append_to_file
from pywheels.file_tools import assert_file_exist
from pywheels.file_tools import guarantee_file_exist


def execute_diophantine(
    input_data: str, 
    output_path: str, 
    exe_path: str
):
    
    with open(output_path, "w", encoding="utf-8") as out:
        
        proc = subprocess.run(
            exe_path,
            input = input_data.encode("utf-8"),
            stdout = out,
            stderr = subprocess.PIPE,
        )

    if proc.returncode != 0:
        
        raise RuntimeError(f"【Diophantine 执行错误】{proc.stderr.decode('utf-8')}")


def main():
    
    guarantee_file_exist("results", is_directory=True)

    diophantine_exec_path = [
        "diophantine", 
        "diophantine.exe"
    ][1]
    
    assert_file_exist(diophantine_exec_path, f"请先生成 diophantine.c 并编译至 {diophantine_exec_path}！")
    
    progress_bar = tqdm(range(249 * 250))

    for a in range(2, 251):
        
        for b in range(1, 251):
            
            lean_file_path = f"results{seperator}{a}-{b}.lean"
            
            if math.gcd(a, b) >= 2:
                
                delete_file(lean_file_path)
                
            else:

                if a >= 65 or (a == 64 and b >= 143):
                    
                    execute_diophantine(
                        input_data = f"2 {a} {a} {b} {b} 250 2", 
                        output_path = f"results{seperator}{a}-{b}.lean", 
                        exe_path = diophantine_exec_path
                    )
                    
            progress_bar.update(1)
    
    
if __name__ == "__main__":
    
    main()
