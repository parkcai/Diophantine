__all__ = [
    "get_integer_input",
    "get_boolean_input",
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
            
            
def get_boolean_input(
    prompt: str,
    default: bool
) -> bool:

    yes_set = {"yes", "y"}
    no_set = {"no", "n"}

    default_str = "Yes" if default else "No"

    while True:
        user_input = input(f"{prompt} [default = {default_str}]: ").strip().lower()

        if not user_input and default is not None:
            return default

        if user_input in yes_set:
            return True
        elif user_input in no_set:
            return False
        else:
            print("请输入 Yes 或 No（或 y / n）！")