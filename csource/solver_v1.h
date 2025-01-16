#include "utils.h"
#include "arithmetic.h"

/*
 * 这里存放第一代自动机求解的方程a^x + b = c^y的a, b, c
 */
int a_v1;
int b_v1;
int c_v1;
int abc_set_status_v1;

/*
 * 这里存放第一代自动机求解的方程a^x + b = c^y中x和y的名字
 */
int x_name_v1[10];
int y_name_v1[10];
int xy_name_set_status_v1;

/*
 * 这里存放形如a^x + b = c^y的关于x, y 的正整数不定方程的求解过程
 */
int solution_v1[200000];

/*
 * 这里存放指向上述求解过程的指针
 */
int solution_v1_pointer;

/*
 * 这个变量记录求解过程的长度
 */
int solution_v1_length;

/*
 * 用这个变量标记求解是否成功
 */
int solver_v1_success;

/*
 * 此函数设置第一代自动机求解的方程a^x + b = c^y的a, b, c
 * 合法的输入是：a, c为大于等于二的正整数，b为正整数
 * 【此函数调用了assert】
 */
void set_abc_v1(int a, int b, int c);

/*
 * 此函数设置第一代自动机求解的方程a^x + b = c^y中x和y的名字
 * 合法的输入是：x_name和y_name的前10个元素中有0（代表字符串结束）
 * 【此函数调用了assert】
 */
void set_xy_name_v1(int x_name[], int y_name[], int x_name_len, int y_name_len);

/*
 * 此函数是第一代自动机求解方程a^x + b = c^y的入口
 * 【此函数调用了assert】
 */
void Solve_Diophantine1();

/*
 * 此函数处理第一代自动机求解方程a^x + b = c^y时，考察b, c就可直接归谬的情形
 */
void Solve_Diophantine1_I_i();

/*
 * 此函数处理第一代自动机求解方程a^x + b = c^y时，考察a, c就可直接归谬的情形
 * 【此函数调用了assert】
 */
void Solve_Diophantine1_I_ii();

/*
 * 此函数处理第一代自动机求解方程a^x + b = c^y时，考察a, b就可直接归谬的情形
 */
void Solve_Diophantine1_I_iii();

/*
 * 此函数处理第一代自动机求解方程a^x + b = c^y时，a, b, c两两互素的情形
 * 【此函数调用了assert】
 */
void Solve_Diophantine1_II();

/*
 * 此函数在命令行输出求解过程
 * 【此函数调用了assert】
 */
void print_solution_v1();

/*
 * 此函数操纵指针将x写入solution_v1
 * 【此函数调用了assert】
 */
void write_solution_v1(int x);

int read_solution_v1();

void resume_solution_v1(int solution_v1_pointer_backup);

int search_threshold_v1;
int mod_threshold_v1;

int disproof_priorlist_prime[100];
int disproof_priorlist_power[100];
int disproof_priorlist_type[100]; // a = 1, c = 3
int disproof_priorlist_length;
int disproof_prime;
int disproof_power;
int disproof_type;

int disable_front_mode;
int disable_back_mode;

/*
 * 【此函数调用了assert】
 */
void insert_disproof_evidence(int prime, int _power, int type);

/*
 * 【此函数调用了assert】
 */
void get_disproof_evidence();

void Solve_Diophantine1_II_disproof_A();

void Solve_Diophantine1_II_disproof_C();

int verbose;

void Solve_Diophantine1_interface();

void exhaust_solution_v1(int nsolutions_pointer);

int max_trial_num_v1;

