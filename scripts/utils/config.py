import sys


__all__ = [
    "recorder_path",
    "diophantine_exec_path",
]


recorder_path = "command_output.txt"


diophantine_exec_path = "diophantine.exe" \
    if sys.platform == "win32" else "diophantine"