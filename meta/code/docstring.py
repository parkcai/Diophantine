__all__ = [
    "docstring_code",
]


docstring_code = f"""/*
 * 第一代自动机 Solver V1        by parkcai
 * 
 * 【用途】
 * 全自动地求解形如a ^ x + b = c ^ y的关于正整数x, y的不定方程
 * 其中，a, b, c已知且满足a >= 2, b >= 1, c >= 2
 * 
 * 【有效求解范围】
 * 经过测试，第一代自动机可以正确而迅速地求解2 <= a <= 70, 2 <= b <= 30, 2 <= c <= 70
 * 范围内的所有方程。在此范围之外，求解有可能失败，但也有很大概率成功。
 * 譬如，方程2 ^ x + 89 = 91 ^ y是可以顺利求解的。
 * 导致求解失败的原因：
 * 1. prime_list短了（见prime_list.h）
 * 2. search_threshold/mod_threshold/max_trial_num调得太低
 * （mod_threshold/max_trial_num调得太高是不好的，因为自动机会尝试很多种求解方案，
 * 如果这两个参数调得太高，会在前几个失败的方案上浪费过多时间）
 * 作者相信，在数学意义上，此程序所给出的算法可以解出所有的a ^ x + b = c ^ y
 */
"""