__all__ = [
    "get_integer_input",
]


def get_integer_input(
    prompt: str, 
    default: int
)-> int:

    while True:
        
        try:
            
            user_input = input(f"{prompt} [default = {default}]: ").strip()
            
            if not user_input and default is not None:
                return default
            return int(user_input)
        
        except ValueError:
            print("请输入一个有效的整数！")