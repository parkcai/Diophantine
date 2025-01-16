#include "arithmetic.h"

int greatest_common_divisor(int n, int m) {
    //"Invalid input of greatest_common_divisor!"
    int array1[42] = {73, 110, 118, 97, 108, 105, 100, 32, 105, 110, 112, 117, 116, 32, 111, 102, 32, 103, 114, 101, 97, 116, 101, 115, 116, 95, 99, 111, 109, 109, 111, 110, 95, 100, 105, 118, 105, 115, 111, 114, 33, 10};
    assert(n >= 1 && m >= 1, array1);
    if(!assertion) return 0;
    int temp;
    while (m != 0) {
        temp = m;
        m = n % m;
        n = temp;
    }
    return n;
}

int least_common_multiple(int n, int m) {
    //"Invalid input of least_common_multiple!"
    int array1[40] = {73, 110, 118, 97, 108, 105, 100, 32, 105, 110, 112, 117, 116, 32, 111, 102, 32, 108, 101, 97, 115, 116, 95, 99, 111, 109, 109, 111, 110, 95, 109, 117, 108, 116, 105, 112, 108, 101, 33, 10};
    assert(n >= 1 && m >= 1, array1);
    if(!assertion) return 0;
    int d = greatest_common_divisor(n, m);
    return n * (m / d);
}

int get_power_cycle_mod(int n, int m) {
    //"Invalid input of get_power_cycle_mod!"
    int array1[38] = {73, 110, 118, 97, 108, 105, 100, 32, 105, 110, 112, 117, 116, 32, 111, 102, 32, 103, 101, 116, 95, 112, 111, 119, 101, 114, 95, 99, 121, 99, 108, 101, 95, 109, 111, 100, 33, 10};
    assert(n >= 2 && m >= 1, array1);
    if(!assertion) return 0;
    assert(greatest_common_divisor(n,m) == 1, array1);
    if(!assertion) return 0;
    m = m % n;
    int m0 = m;
    if (m == 1) return 1;
    int result = 1;
    while (m != 1) {
        m = (m * m0) % n;
        result = result + 1;
    }
    return result;
}

int get_power_position_mod(int n, int m, int k) {
    //"Invalid input of get_power_position_mod!"
    int array1[41] = {73, 110, 118, 97, 108, 105, 100, 32, 105, 110, 112, 117, 116, 32, 111, 102, 32, 103, 101, 116, 95, 112, 111, 119, 101, 114, 95, 112, 111, 115, 105, 116, 105, 111, 110, 95, 109, 111, 100, 33, 10};
    assert(n >= 2 && m >= 1 && k >= 0, array1);
    if(!assertion) return 0;
    assert(greatest_common_divisor(n,m) == 1, array1);
    if(!assertion) return 0;
    k = k % n;
    if (k == 1) return 0;
    m = m % n;
    int m0 = m;
    int result = 1;
    while (m != 1) {
        if (k == m) return result;
        m = (m * m0) % n;
        result = result + 1;
    }
    return -1;
}

int is_prime(int n) {
    //"Invalid input of is_prime!"
    int array1[27] = {73, 110, 118, 97, 108, 105, 100, 32, 105, 110, 112, 117, 116, 32, 111, 102, 32, 105, 115, 95, 112, 114, 105, 109, 101, 33, 10};
    assert(n >= 1, array1);
    if(!assertion) return 0;
    if (n == 1) return 0;
    if (n <= 3) return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;
    int i = 5;
    while (i * i <= n) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return 0; 
        }
        i = i + 6;
    }
    return 1; 
}

int power(int base, int exp, int mod) {
    //"Invalid input of power!"
    int array1[24] = {73, 110, 118, 97, 108, 105, 100, 32, 105, 110, 112, 117, 116, 32, 111, 102, 32, 112, 111, 119, 101, 114, 33, 10};
    assert(base >= 1 && exp >= 0 && (mod >= 2 || mod == -1), array1);
    if(!assertion) return 0;
    int res = 1, i = 0;
    while (i < exp) {
        res = res * base;
        if (mod != -1) {
            res = res % mod;
        }
        i = i + 1;
    }
    return res;
}

int contain_undividable_prime_part(int d, int x) {
    //"Invalid input of contain_undividable_prime_part!"
    int array1[49] = {73, 110, 118, 97, 108, 105, 100, 32, 105, 110, 112, 117, 116, 32, 111, 102, 32, 99, 111, 110, 116, 97, 105, 110, 95, 117, 110, 100, 105, 118, 105, 100, 97, 98, 108, 101, 95, 112, 114, 105, 109, 101, 95, 112, 97, 114, 116, 33, 10};
    assert(d >= 1 && x >= 1, array1);
    if(!assertion) return 0;
    int i = 2;
    while (i <= d) {
        if (d % i == 0 && is_prime(i)) { 
            if (x % i != 0) { 
                return 1; 
            }
        }
        i = i + 1;
    }
    return 0; 
}

int get_power_times_over(int M, int a){
    //"Invalid input of get_power_times_over!"
    int array1[39] = {73, 110, 118, 97, 108, 105, 100, 32, 105, 110, 112, 117, 116, 32, 111, 102, 32, 103, 101, 116, 95, 112, 111, 119, 101, 114, 95, 116, 105, 109, 101, 115, 95, 111, 118, 101, 114, 33, 10};
    assert(a >= 2 && M >= 1, array1);
    if(!assertion) return 0;
    int n = 1, a0 = a;
    while (a <= M) {
        a = a * a0;
        n = n + 1;
    }
    return n;
}

int get_degree_wrt(int p, int N) {
    int res = 0;
    while (N % p == 0) {
        N = N / p;
        res = res + 1;
    }
    return res;
}