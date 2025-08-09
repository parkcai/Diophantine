import subprocess
from tqdm import tqdm
from pywheels.file_tools import clear_file
from pywheels.file_tools import append_to_file


def main():
    
    recorder_path = "command_output.txt"
    
    clear_file(recorder_path)
    
    a_max = 500; b_max = 500; c_max = 500
    
    progress_bar = tqdm(range((a_max * b_max * c_max) // 1000))
    
    for a in range(1, a_max+1, 10):
        for b in range(1, b_max+1, 10):
            for c in range(1, c_max+1, 10):
                
                try:
                    
                    if a <= 250 and b <= 250 and c <= 250: continue
                
                    subprocess.run(
                        "diophantine.exe",
                        input = f"2 {a+9} {a} {b+9} {b} {c+9} {c}".encode("utf-8"),
                        stdout = subprocess.DEVNULL,
                        stderr = subprocess.PIPE,
                        timeout = 3,
                    )
                    
                except subprocess.TimeoutExpired as _:
                    append_to_file(recorder_path, f"{a} {b} {c}")
                    
                finally:
                    progress_bar.update(1)


if __name__ == "__main__":
    
    main()