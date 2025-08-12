import sys


__all__ = [
    "recorder_path",
    "diophantine_exec_path",
    "run_diophantine_timeout_seconds",
    "revalidate_timeout_seconds",
]


recorder_path = "command_output.txt"


diophantine_exec_path = "diophantine.exe" \
    if sys.platform == "win32" else "diophantine"
    
    
run_diophantine_timeout_seconds = 20
    
    
revalidate_timeout_seconds = 20