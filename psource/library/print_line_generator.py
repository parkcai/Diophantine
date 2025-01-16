import numpy as np

lineno_path = "psource/library/line_no.npy"

def generate_print_line(str1):
    lineno = np.load(lineno_path)[0]
    ascii_values = [ord(char) for char in str1]
    ascii_values.append(10)
    print(f'//"{str1}"')
    print(f"int array{lineno}[{len(ascii_values)}] = {{{', '.join(map(str, ascii_values))}}};")
    # print(f"print(array{lineno});")
    np.save(lineno_path, np.array([lineno+1]))
    
def initialize_lineno():
    np.save(lineno_path, np.array([1]))