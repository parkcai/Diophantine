/*
 * 这个头文件提供了一些使编写SysY程序更简单的工具性函数和变量
 */

#include "SysY.h"
const int endl;
const int space;
const int left_parenthesis;
const int right_parenthesis;
const int period;
const int comma;
const int equals;
const int percentage;
const int hat;
int null[1];
int newline[1];
int assertion;
int string_x[2];
int strlen_x;
int string_y[2];
int strlen_y;
int string_z[2];
int strlen_z;
int string_u[2];
int strlen_u;
int string_v[2];
int strlen_v;

/*
 * 此函数用于断言表达式expr为真，如若不然，则输出err_info并exit
 * 由于SysY语法实际上不支持exit，所以此函数的作用是令assertion = expr，并在expr为假时输出err_info
 * 为实现exit的效果，应在所有assert(..., ...);后都加上一句if (!assertion) return 0; 或 if (!assertion) return;
 * 此外，在调用所有调用了assert的函数后，理论上也都应加上一句if (!assertion) return 0; 或 if (!assertion) return;
 * 不过，如果对于不会assert失败比较自信，或者觉得assert失败后继续运行一会儿也无所谓，那么也可以不加
 */
void assert(int expr, int err_info[]);

/*
 * 此函数用于向控制台输出句子line
 * line是一个一维整数数组，每个整数被理解为ASCII码下对应的字符
 * 必须以10（换行符）结尾，这是为了保证及时输出（SysY没法flush printf的缓冲区）
 * 如果line[0] == 0，则理解为空字符串，什么也不输出
 */
void print_line(int line[]);

void print_word(int word[]);

void print_line_with_ddd(int line[], int arg1, int arg2, int arg3);

void print_line_with_dsd(int line[], int arg1, int arg2[], int arg3);

void print_line_with_dsdds(int line[], int arg1, int arg2[], int arg3, int arg4, int arg5[]);

void print_line_with_sdsd(int line[], int arg1[], int arg2, int arg3[], int arg4);

void print_line_with_dd(int line[], int arg1, int arg2);

void print_line_with_ss(int line[], int arg1[], int arg2[]);

void print_line_with_sddsdd(int line[], int arg1[], int arg2, int arg3, int arg4[], int arg5, int arg6);

void print_line_with_sdd(int line[], int arg1[], int arg2, int arg3);

void print_line_with_d(int line[], int arg1);

void print_line_with_sd(int line[], int arg1[], int arg2);

void print_line_with_ssdsdds(int line[], int arg1[], int arg2[], int arg3, int arg4[], int arg5, int arg6, int arg7[]);

