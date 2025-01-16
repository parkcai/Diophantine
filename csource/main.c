#include "arithmetic.h"
#include "solver_v1.h"
#include "solver_v2.h"
#include "utils.h"

/*
 * 遍历范围2 <= a <= a_max, 2 <= b <= b_max, 2 <= c <= c_max进行求解
 * 测试过有效的范围是：2 <= a <= 70, 2 <= b <= 30, 2 <= c <= 70
 * 由于int32只能表示有限范围内的整数，超出测试范围，求解是有可能失败的
 * 但也很可能成功，不妨用Solve_Diophantine1_interface一试（如2 ^ x + 89 = 91 ^ y）
 */
int main() {
    // Solve_Diophantine1_interface();
    // return;
    int a_max = 10, b_max = 10, c_max = 10;
    set_xy_name_v1(string_x, string_y, strlen_x, strlen_y);
    int a = 2;
    int first_time_protection = 1;
    while (a <= a_max) {
        int b = 1;
        while (b <= b_max) {
            int c = 2;
            while (c <= c_max) {
                set_abc_v1(a, b, c);
                Solve_Diophantine1();
                if (first_time_protection) {
                    first_time_protection = 0;
                }else{
                    print_line(newline);
                }
                print_solution_v1();
                if(!assertion) {
                    getint();
                }
                c = c + 1;
            }
            b = b + 1;
        }
        a = a + 1;
    }

    // 给变量换个名字再测试一下
    set_xy_name_v1(string_u, string_v, strlen_u, strlen_v);
    a = 2;
    first_time_protection = 1;
    while (a <= a_max) {
        int b = 1;
        while (b <= b_max) {
            int c = 2;
            while (c <= c_max) {
                set_abc_v1(a, b, c);
                Solve_Diophantine1();
                if (first_time_protection) {
                    first_time_protection = 0;
                }else{
                    print_line(newline);
                }
                print_solution_v1();
                if(!assertion) {
                    getint();
                }
                c = c + 1;
            }
            b = b + 1;
        }
        a = a + 1;
    }
}