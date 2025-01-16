/*
 * 这个头文件提供了一些SysY语言的库函数
 * SysY语言的编译器应该自动地认识这些函数，所以源文件拿给SysY语言的编译器时不需要include此头文件
 */

#include <stdio.h>
/*
 * SysY库函数
 */
void putch(int n);

/*
 * SysY库函数
 */
void putint(int n);

/*
 * SysY库函数
 */
int getint();