/*
 * 这个头文件提供了一些与初等数论相关的常用函数
 * 如最大公因数、最小公倍数、ord_M N（N关于M的阶）等
 */

#include "SysY_utils.h"
/*
 * 此函数返回正整数n和m的最大公约数
 * 【此函数调用了assert】
 */
int greatest_common_divisor(int n, int m);


/*
 * 此函数返回正整数n和m的最小公倍数
 * 【此函数调用了assert】
 */
int least_common_multiple(int n, int m);

/*
 * 此函数返回数列m mod n, m^2 mod n, m^3 mod n, ... 的周期
 * 此周期亦称作“m关于n的阶”，记为ord_n m
 * 合法的输入是：n为大于等于2的正整数，m为与n互素的正整数
 * 【此函数调用了assert】
 */
int get_power_cycle_mod(int n, int m);

/*
 * 此函数返回数列m mod n, m^2 mod n, m^3 mod n, ... 中k mod n的位置
 * 合法的输入是：n为大于等于2的正整数，m为与n互素的正整数，k为自然数
 * 输出：
 * 1. 如果数列m mod n, m^2 mod n, m^3 mod n, ... 中存在k mod n，那么
 * 返回0至(ord_n m) - 1中的一个数p，使得m ^ p mod n = k mod n
 * 2. 如果数列m mod n, m^2 mod n, m^3 mod n, ... 中不存在k mod n，那么返回-1
 * 【此函数调用了assert】
 */
int get_power_position_mod(int n, int m, int k);

/*
 * 此函数判断正整数n是不是素数
 * 【此函数调用了assert】
 */
int is_prime(int n);

/*
 * 此函数实现了Python风格的pow函数
 * 合法的输入是：base为正整数，exp为自然数，mod为大于等于2的正整数或-1（后者表示不取模）
 * 【此函数调用了assert】
 */
int power(int base, int exp, int mod);

/*
 * 此函数判断d是否含有x不含有的素因子
 * 合法的输入是：d, x为正整数
 * 【此函数调用了assert】
 */
int contain_undividable_prime_part(int d, int x);

/*
 * 此函数返回满足a ^ n > M的最小正整数M
 * 合法的输入是：a为大于等于二的正整数，M为正整数
 * 【此函数调用了assert】
 */
int get_power_times_over(int M, int a);

int get_degree_wrt(int p, int N);

