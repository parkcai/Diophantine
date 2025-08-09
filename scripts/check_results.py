from tqdm import tqdm
from os import listdir
from os.path import join
from os.path import isfile
from pywheels.file_tools import assert_file_exist
from pywheels.task_runner import execute_command


def main():
    
    folder = f"results"

    lean_file_paths = sorted([
        join(folder, f)
        for f in listdir(folder)
        if f.endswith(".lean") and isfile(join(folder, f))
    ])

    for lean_file_path in tqdm(lean_file_paths):

        try:
            
            assert_file_exist(lean_file_path)

            result = execute_command(f"lean --run {lean_file_path}")

            assert result["stdout"] == "Native Lean4 check passed.\n"

        except Exception as error:
            
            print(f"失败！出错文件：{lean_file_path}")
            
            print(f"错误信息：{error}")
            
            return


if __name__ == "__main__":
    
    main()
