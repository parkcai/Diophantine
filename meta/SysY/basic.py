__all__ = [
    "putch_code",
    "putint_code",
    "getint_code",
]


putch_code = f"""void putch(int n) {{
    printf("%c", n);
}}
"""


putint_code = f"""void putint(int n) {{
    printf("%d", n);
}}
"""


getint_code = f"""int getint() {{
    int res;
    scanf("%d", &res);
    return res;
}}
"""

