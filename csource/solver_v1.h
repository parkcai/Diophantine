/*
 * 第一代自动机 Solver V1        by parkcai
 * 
 * 【用途】
 * 全自动地求解形如a ^ x + b = c ^ y的关于正整数x, y的不定方程
 * 其中，a, b, c已知且满足a >= 2, b >= 1, c >= 2
 * 
 * 【向外提供的接口】
 * 1. set_abc_v1(int a, int b, int c) 设置a, b, c（a, b, c应满足a >= 2, b >= 1, c >= 2）
 * 2. Solve_Diophantine1() 根据设置的a, b, c进行求解，将求解信息保存在内部变量中
 * 3. set_xy_name_v1(int x_name[], int y_name[], int x_name_len, int y_name_len) 设置x和y的名字
 * 4. print_solution_v1() 根据调用时的求解信息和x, y名字在命令行输出求解过程
 * 5. Solve_Diophantine1_interface() 一个简易的界面，从命令行读入a, b, c，进行求解，然后在命令行输出求解过程
 * 6. Solve_Diophantine1_test_range(int a_max, int b_max, int c_max) 
 * 遍历范围2 <= a <= a_max, 2 <= b <= b_max, 2 <= c <= c_max进行求解，然后在命令行输出求解过程
 * 
 * 【有效求解范围】
 * 经过测试，第一代自动机可以正确而迅速地求解2 <= a <= 70, 2 <= b <= 30, 2 <= c <= 70
 * 范围内的所有方程。在此范围之外，求解有可能失败，但也有很大概率成功。
 * 譬如，方程2 ^ x + 89 = 91 ^ y是可以顺利求解的。
 * 导致求解失败的原因：
 * 1. int32只能表示有限范围内的整数
 * 2. prime_list短了（见prime_list.h）
 * 3. search_threshold/mod_threshold/max_trial_num调得太低
 * （mod_threshold/max_trial_num调得太高是不好的，因为自动机会尝试很多种求解方案，
 * 如果这两个参数调得太高，会在前几个失败的方案上浪费过多时间）
 * 作者相信，在数学意义上，此程序所给出的算法可以解出所有的a ^ x + b = c ^ y
 */

#include "SysY_utils.h"
#include "arithmetic.h"
#include "prime_list.h"

void set_abc_v1(int a, int b, int c);
void set_xy_name_v1(int x_name[], int y_name[], int x_name_len, int y_name_len);
void Solve_Diophantine1();
void print_solution_v1();
void Solve_Diophantine1_interface();
void Solve_Diophantine1_test_range(int a_max, int b_max, int c_max);
