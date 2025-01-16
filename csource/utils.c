#include "utils.h"
const int endl = 10;
const int space = 32;
const int left_parenthesis = 40;
const int right_parenthesis = 41;
const int period = 46;
const int comma = 44;
const int percentage = 37;
const int equals = 61;
const int hat = 94;
int assertion = 1;
int null[1] = {0};
int newline[1] = {10};

int string_x[2] = {120, 0};
int strlen_x = 2;
int string_y[2] = {121, 0};
int strlen_y = 2;
int string_z[2] = {122, 0};
int strlen_z = 2;
int string_u[2] = {117, 0};
int strlen_u = 2;
int string_v[2] = {118, 0};
int strlen_v = 2;

void assert(int expr, int err_info[]) {
    assertion = expr;
    if (!assertion) {
        print_line(err_info);
    }
}

void print_line(int line[]){
    if (!line[0]) return;
    int i = 0;
    while (line[i] != endl) { 
        putch(line[i]);   
        i = i + 1;   
    }
    putch(endl);
}

void print_word(int word[]) {
    int i = 0;
    while (word[i]) { 
        putch(word[i]);   
        i = i + 1;   
    }
}

void print_line_with_ddd(int line[], int arg1, int arg2, int arg3) {
    if (!line[0]) return;
    int i = 0;
    int count = 1;
    while (line[i] != endl) {
        if (line[i] != percentage) {
            putch(line[i]);   
            i = i + 1; 
        }else{
            if (count == 1) {
                putint(arg1);
                i = i + 2; 
                count = count + 1;
            }else if (count == 2) {
                putint(arg2);
                i = i + 2; 
                count = count + 1;
            }else{
                putint(arg3);
                i = i + 2; 
            }
        }
    }
    putch(endl);
}

void print_line_with_dsd(int line[], int arg1, int arg2[], int arg3) {
    if (!line[0]) return;
    int i = 0;
    int count = 1;
    while (line[i] != endl) {
        if (line[i] != percentage) {
            putch(line[i]);   
            i = i + 1; 
        }else{
            if (count == 1) {
                putint(arg1);
                i = i + 2; 
                count = count + 1;
            }else if (count == 2) {
                print_word(arg2);
                i = i + 2; 
                count = count + 1;
            }else{
                putint(arg3);
                i = i + 2; 
            }
        }
    }
    putch(endl);
}

void print_line_with_dsdds(int line[], int arg1, int arg2[], int arg3, int arg4, int arg5[]) {
    if (!line[0]) return;
    int i = 0;
    int count = 1;
    while (line[i] != endl) {
        if (line[i] != percentage) {
            putch(line[i]);   
            i = i + 1; 
        }else{
            if (count == 1) {
                putint(arg1);
                i = i + 2; 
                count = count + 1;
            }else if (count == 2) {
                print_word(arg2);
                i = i + 2; 
                count = count + 1;
            }else if (count == 3) {
                putint(arg3);
                i = i + 2; 
                count = count + 1;
            }else if (count == 4) {
                putint(arg4);
                i = i + 2; 
                count = count + 1;
            }else{
                print_word(arg5);
                i = i + 2;
            }
        }
    }
    putch(endl);
}

void print_line_with_sdsd(int line[], int arg1[], int arg2, int arg3[], int arg4) {
    if (!line[0]) return;
    int i = 0;
    int count = 1;
    while (line[i] != endl) {
        if (line[i] != percentage) {
            putch(line[i]);   
            i = i + 1; 
        }else{
            if (count == 1) {
                print_word(arg1);
                i = i + 2; 
                count = count + 1;
            }else if (count == 2) {
                putint(arg2);
                i = i + 2; 
                count = count + 1;
            }else if (count == 3) {
                print_word(arg3);
                i = i + 2; 
                count = count + 1;
            }else{
                putint(arg4);
                i = i + 2; 
                count = count + 1;
            }
        }
    }
    putch(endl);
}

void print_line_with_dd(int line[], int arg1, int arg2) {
    if (!line[0]) return;
    int i = 0;
    int count = 1;
    while (line[i] != endl) {
        if (line[i] != percentage) {
            putch(line[i]);   
            i = i + 1; 
        }else{
            if (count == 1) {
                putint(arg1);
                i = i + 2; 
                count = count + 1;
            }else{
                putint(arg2);
                i = i + 2; 
                count = count + 1;
            }
        }
    }
    putch(endl);
}

void print_line_with_ss(int line[], int arg1[], int arg2[]) {
    if (!line[0]) return;
    int i = 0;
    int count = 1;
    while (line[i] != endl) {
        if (line[i] != percentage) {
            putch(line[i]);   
            i = i + 1; 
        }else{
            if (count == 1) {
                print_word(arg1);
                i = i + 2; 
                count = count + 1;
            }else{
                print_word(arg2);
                i = i + 2; 
                count = count + 1;
            }
        }
    }
    putch(endl);
}

void print_line_with_sddsdd(int line[], int arg1[], int arg2, int arg3, int arg4[], int arg5, int arg6) {
    if (!line[0]) return;
    int i = 0;
    int count = 1;
    while (line[i] != endl) {
        if (line[i] != percentage) {
            putch(line[i]);   
            i = i + 1; 
        } else {
            if (count == 1) {
                print_word(arg1);
                i = i + 2; 
                count = count + 1;
            } else if (count == 2) {
                putint(arg2);
                i = i + 2; 
                count = count + 1;
            } else if (count == 3) {
                putint(arg3);
                i = i + 2; 
                count = count + 1;
            } else if (count == 4) {
                print_word(arg4);
                i = i + 2; 
                count = count + 1;
            } else if (count == 5) {
                putint(arg5);
                i = i + 2; 
                count = count + 1;
            } else {
                putint(arg6);
                i = i + 2;
                count = count + 1;
            }
        }
    }
    putch(endl);
}

void print_line_with_sdd(int line[], int arg1[], int arg2, int arg3) {
    if (!line[0]) return;
    int i = 0;
    int count = 1;
    while (line[i] != endl) {
        if (line[i] != percentage) {
            putch(line[i]);   
            i = i + 1; 
        } else {
            if (count == 1) {
                print_word(arg1);
                i = i + 2; 
                count = count + 1;
            } else if (count == 2) {
                putint(arg2);
                i = i + 2; 
                count = count + 1;
            } else {
                putint(arg3);
                i = i + 2; 
                count = count + 1;
            }
        }
    }
    putch(endl);
}

void print_line_with_d(int line[], int arg1) {
    if (!line[0]) return;
    int i = 0;
    int count = 1;
    while (line[i] != endl) {
        if (line[i] != percentage) {
            putch(line[i]);   
            i = i + 1; 
        } else {
            if (count == 1) {
                putint(arg1);
                i = i + 2; 
                count = count + 1;
            }
        }
    }
    putch(endl);
}

void print_line_with_sd(int line[], int arg1[], int arg2) {
    if (!line[0]) return;
    int i = 0;
    int count = 1;
    while (line[i] != endl) {
        if (line[i] != percentage) {
            putch(line[i]);   
            i = i + 1; 
        } else {
            if (count == 1) {
                print_word(arg1);
                i = i + 2; 
                count = count + 1;
            }else {
                putint(arg2);
                i = i + 2;
            }
        }
    }
    putch(endl);
}

void print_line_with_ssdsdds(int line[], int arg1[], int arg2[], int arg3, int arg4[], int arg5, int arg6, int arg7[]) {
    if (!line[0]) return;
    int i = 0;
    int count = 1;
    while (line[i] != endl) {
        if (line[i] != percentage) {
            putch(line[i]);   
            i = i + 1; 
        } else {
            if (count == 1) {
                print_word(arg1);
                i = i + 2; 
                count = count + 1;
            } else if (count == 2) {
                print_word(arg2);
                i = i + 2; 
                count = count + 1;
            } else if (count == 3) {
                putint(arg3);
                i = i + 2; 
                count = count + 1;
            } else if (count == 4) {
                print_word(arg4);
                i = i + 2; 
                count = count + 1;
            } else if (count == 5) {
                putint(arg5);
                i = i + 2; 
                count = count + 1;
            }else if (count == 6) {
                putint(arg6);
                i = i + 2; 
                count = count + 1;
            } else {
                print_word(arg7);
                i = i + 2;
                count = count + 1;
            }
        }
    }
    putch(endl);
}