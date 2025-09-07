from pywheels.file_tools import get_lines
from pywheels.file_tools import append_to_file


result_path = "scripts/swift/result.txt"
product_path = "scripts/swift/product.txt"
append_to_product_path = lambda content: append_to_file(
    file_path = product_path,
    content = content,
)

for line in get_lines(result_path):
    if "未解决！！！" not in line:
        append_to_product_path(line)
