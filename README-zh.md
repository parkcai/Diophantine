# Diophantine_SysY

> 用 SysY 语言解不定方程 `a ^ x + b = c ^ y`

## 🧩 项目简介

**Diophantine_SysY** 是一个用 **SysY** 语言构建的实验性求解器，专门用于自动求解形如：

```
a ^ x + b = c ^ y
```

的正整数不定方程，其中 `a, b, c` 均为已知正整数，满足约束：

- a ≥ 2
- b ≥ 1
- c ≥ 2

SysY 语言 是北京大学编译原理课程采用的教学用 C 语言子集，在编程表达上存在诸多限制。因此本项目采用 **Python 元编程** 的方式来生成 `.c` 源码，随后通过 `gcc` 或学生编译器编译得到可执行程序。

## 📁 主要项目结构

```
Diophantine_SysY/
├── meta/                      # Python 元编程模块，用于生成主程序
│   └── generate.py            # 使用 `python -m meta.generate` 自动生成 diophantine.c
├── revalidate/                # 二次验证模块（CoLean）
│   └── run.py                 # 使用 `python -m revalidate.run` 验证 all 下的 .lean 文件
│   └── all                    # 建议将批量生成的方程求解过程重定向至此
│       └── 1.lean
│       └── 2.lean
├── diophantine.c              # 由 meta 生成的主程序源代码（SysY风格）
├── transcendental_diophantine1.lean  # 项目示例性文件，部分验证逻辑外包的 Lean 数学形式化文件
└── README.md
```

## 🚀 编译与使用

1. 生成 SysY 源码：

```bash
python -m meta.generate
```

2. 使用 GCC 编译生成的 `diophantine.c` 文件：（此步骤可用学生编译器代替：将 meta/generate.py 中的 for_course_compiler 变量改为 True）

```bash
gcc diophantine.c -o diophantine
```

3. 运行主程序，输入模式编号：（此步骤可用 qemu 模拟运行代替）

```bash
./diophantine
```

### 使用方式说明

运行 `./diophantine` 进入程序主入口。**程序不会提示功能模式，用户需自行输入编号以选择操作**：

- **输入 `0`：帮助信息模式**
  显示所有功能的简要说明，适合首次使用时查阅。

- **输入 `1`：交互模式（推荐）**
  手动输入 `a, b, c` 三个整数，用于求解方程 `a ^ x + b = c ^ y` 的正整数解，
  成功时将显示解或生成对应的 Lean4 代码（用于形式化验证）。

- **输入 `2`：安静模式，研究用**
  输入六个整数：`a_max a_min b_max b_min c_max c_min`，
  程序将自动遍历所有满足条件的非平凡 `(a, b, c)` 三元组并批量验证。

- **输入 `3`：文档模式**
  打印 Lean4 形式化文档 `transcendental_diophantine1.lean` 的全部内容。
  **建议将输出重定向到文件 `transcendental_diophantine1.lean` 保存，否则内容可能过长而溢出终端。**

## 💡 示例：方程求解实例

**注意：**下列所有 Lean4 示例代码均依赖于 `Claim Structure`。

```Lean
-- Claim Structure
structure VerifiedFact where
  prop : Prop
  proof : prop

axiom Claim (prop_to_claim : Prop)
  (verified_facts : List VerifiedFact)
  (revalidator : String)
  : prop_to_claim
```

1. $5 ^ x + 3 = 2 ^ y,\ x,y\in\mathbb{N}^*\Rightarrow(x,y)=(1, 3)\ or\ (x,y)=(3, 7)$

```Lean
/-
(Class II, Front Mode, with magic prime 257)   5 ^ x + 3 = 2 ^ y
For positive integers x, y satisfying 5 ^ x + 3 = 2 ^ y,
if y >= 8, 5 ^ x = 253 (mod 256).
So x = 35 (mod 64),
which implies x = 35, 99, 163, 227 (mod 256).
Therefore, 5 ^ x = 14, 224, 243, 33 (mod 257).
So 2 ^ y = 17, 227, 246, 36 (mod 257), but this is impossible.
Therefore, y < 8.
Further examination shows that (x, y) = (1, 3), (3, 7).
-/
theorem diophantine1_5_3_2 (x : Nat) (y : Nat) (h1 : x >= 1) (h2 : y >= 1) (h3 : 5 ^ x + 3 = 2 ^ y) :
  List.Mem (x, y) [(1, 3), (3, 7)]
  := by
  have h4 : x % 1 = 0 := by omega
  have h5 : y % 1 = 0 := by omega
  by_cases h6 : y >= 8
  have h7 := Claim (2 ^ y % 256 = 0) [
    {prop := y % 1 = 0, proof := h5},
    {prop := y >= 8, proof := h6},
  ] "pow_mod_eq_zero"
  have h8 : 5 ^ x % 256 = 253 := by omega
  have h9 := Claim (x % 64 = 35) [
    {prop := x % 1 = 0, proof := h4},
    {prop := x >= 1, proof := h1},
    {prop := 5 ^ x % 256 = 253, proof := h8},
  ] "observe_mod_cycle"
  have h10 := Claim (List.Mem (5 ^ x % 257) [14, 224, 243, 33]) [
    {prop := x % 1 = 0, proof := h4},
    {prop := x >= 1, proof := h1},
    {prop := x % 64 = 35, proof := h9},
  ] "utilize_mod_cycle"
  have h11 := Claim (List.Mem (2 ^ y % 257) [17, 227, 246, 36]) [
    {prop := List.Mem (5 ^ x % 257) [14, 224, 243, 33], proof := h10},
    {prop := 5 ^ x + 3 = 2 ^ y, proof := h3},
  ] "compute_mod_add"
  have h12 := Claim False [
    {prop := y % 1 = 0, proof := h5},
    {prop := y >= 1, proof := h2},
    {prop := List.Mem (2 ^ y % 257) [17, 227, 246, 36], proof := h11},
  ] "exhaust_mod_cycle"
  apply False.elim h12
  have h7 : y <= 7 := by omega
  have h8 := Claim (List.Mem (x, y) [(1, 3), (3, 7)]) [
    {prop :=  x % 1 = 0, proof := h4},
    {prop :=  x >= 1, proof := h1},
    {prop :=  y % 1 = 0, proof := h5},
    {prop :=  y >= 1, proof := h2},
    {prop := 5 ^ x + 3 = 2 ^ y, proof := h3},
    {prop := y <= 7, proof := h7},
  ] "diophantine1_back_enumeration"
  exact h8
```

2. $3 ^ x + 10 = 13 ^ y,\ x,y\in\mathbb{N}^*\Rightarrow(x,y)=(1, 1)\ or\ (x,y)=(7, 3)$

```Lean
/-
(Class II, Back Mode, with magic prime 17497)   3 ^ x + 10 = 13 ^ y
For positive integers x, y satisfying 3 ^ x + 10 = 13 ^ y,
if x >= 8, 13 ^ y = 10 (mod 6561).
So y = 1461 (mod 2187),
which implies y = 1461, 3648, 5835, 8022 (mod 8748).
Therefore, 13 ^ y = 11616, 6486, 5881, 11011 (mod 17497).
So 3 ^ x = 11606, 6476, 5871, 11001 (mod 17497), but this is impossible.
Therefore, x < 8.
Further examination shows that (x, y) = (1, 1), (7, 3).
-/
theorem diophantine1_3_10_13 (x : Nat) (y : Nat) (h1 : x >= 1) (h2 : y >= 1) (h3 : 3 ^ x + 10 = 13 ^ y) :
  List.Mem (x, y) [(1, 1), (7, 3)]
  := by
  have h4 : x % 1 = 0 := by omega
  have h5 : y % 1 = 0 := by omega
  by_cases h6 : x >= 8
  have h7 := Claim (3 ^ x % 6561 = 0) [
    {prop := x % 1 = 0, proof := h4},
    {prop := x >= 8, proof := h6},
  ] "pow_mod_eq_zero"
  have h8 : 13 ^ y % 6561 = 10 := by omega
  have h9 := Claim (y % 2187 = 1461) [
    {prop := y % 1 = 0, proof := h5},
    {prop := y >= 1, proof := h2},
    {prop := 13 ^ y % 6561 = 10, proof := h8},
  ] "observe_mod_cycle"
  have h10 := Claim (List.Mem (13 ^ y % 17497) [11616, 6486, 5881, 11011]) [
    {prop := y % 1 = 0, proof := h5},
    {prop := y >= 1, proof := h2},
    {prop := y % 2187 = 1461, proof := h9},
  ] "utilize_mod_cycle"
  have h11 := Claim (List.Mem (3 ^ x % 17497) [11606, 6476, 5871, 11001]) [
    {prop := List.Mem (13 ^ y % 17497) [11616, 6486, 5881, 11011], proof := h10},
    {prop := 3 ^ x + 10 = 13 ^ y, proof := h3},
  ] "compute_mod_sub"
  have h12 := Claim False [
    {prop := x % 1 = 0, proof := h4},
    {prop := x >= 1, proof := h1},
    {prop := List.Mem (3 ^ x % 17497) [11606, 6476, 5871, 11001], proof := h11},
  ] "exhaust_mod_cycle"
  apply False.elim h12
  have h7 : x <= 7 := by omega
  have h8 := Claim (List.Mem (x, y) [(1, 1), (7, 3)]) [
    {prop :=  x % 1 = 0, proof := h4},
    {prop :=  x >= 1, proof := h1},
    {prop :=  y % 1 = 0, proof := h5},
    {prop :=  y >= 1, proof := h2},
    {prop := 3 ^ x + 10 = 13 ^ y, proof := h3},
    {prop := x <= 7, proof := h7},
  ] "diophantine1_front_enumeration"
  exact h8
```

3. $2 ^ x + 89 = 91 ^ y,\ x,y\in\mathbb{N}^*\Rightarrow(x,y)=(1, 1)\ or\ (x,y)=(13, 2)$

```Lean
/-
(Class II, Front Mode, with magic prime 2647)   2 ^ x + 89 = 91 ^ y
For positive integers x, y satisfying 2 ^ x + 89 = 91 ^ y,
if y >= 3, 2 ^ x = 254 (mod 343).
So x = 76 (mod 147),
which implies x = 76, 223, 370, 517, 664, 811, 958, 1105, 1252 (mod 1323).
Therefore, 2 ^ x = 1994, 852, 1811, 957, 1447, 1513, 2343, 348, 1970 (mod 2647).
So 91 ^ y = 2083, 941, 1900, 1046, 1536, 1602, 2432, 437, 2059 (mod 2647), but this is impossible.
Therefore, y < 3.
Further examination shows that (x, y) = (1, 1), (13, 2).
-/
theorem diophantine1_2_89_91 (x : Nat) (y : Nat) (h1 : x >= 1) (h2 : y >= 1) (h3 : 2 ^ x + 89 = 91 ^ y) :
  List.Mem (x, y) [(1, 1), (13, 2)]
  := by
  have h4 : x % 1 = 0 := by omega
  have h5 : y % 1 = 0 := by omega
  by_cases h6 : y >= 3
  have h7 := Claim (91 ^ y % 343 = 0) [
    {prop := y % 1 = 0, proof := h5},
    {prop := y >= 3, proof := h6},
  ] "pow_mod_eq_zero"
  have h8 : 2 ^ x % 343 = 254 := by omega
  have h9 := Claim (x % 147 = 76) [
    {prop := x % 1 = 0, proof := h4},
    {prop := x >= 1, proof := h1},
    {prop := 2 ^ x % 343 = 254, proof := h8},
  ] "observe_mod_cycle"
  have h10 := Claim (List.Mem (2 ^ x % 2647) [1994, 852, 1811, 957, 1447, 1513, 2343, 348, 1970]) [
    {prop := x % 1 = 0, proof := h4},
    {prop := x >= 1, proof := h1},
    {prop := x % 147 = 76, proof := h9},
  ] "utilize_mod_cycle"
  have h11 := Claim (List.Mem (91 ^ y % 2647) [2083, 941, 1900, 1046, 1536, 1602, 2432, 437, 2059]) [
    {prop := List.Mem (2 ^ x % 2647) [1994, 852, 1811, 957, 1447, 1513, 2343, 348, 1970], proof := h10},
    {prop := 2 ^ x + 89 = 91 ^ y, proof := h3},
  ] "compute_mod_add"
  have h12 := Claim False [
    {prop := y % 1 = 0, proof := h5},
    {prop := y >= 1, proof := h2},
    {prop := List.Mem (91 ^ y % 2647) [2083, 941, 1900, 1046, 1536, 1602, 2432, 437, 2059], proof := h11},
  ] "exhaust_mod_cycle"
  apply False.elim h12
  have h7 : y <= 2 := by omega
  have h8 := Claim (List.Mem (x, y) [(1, 1), (13, 2)]) [
    {prop :=  x % 1 = 0, proof := h4},
    {prop :=  x >= 1, proof := h1},
    {prop :=  y % 1 = 0, proof := h5},
    {prop :=  y >= 1, proof := h2},
    {prop := 2 ^ x + 89 = 91 ^ y, proof := h3},
    {prop := y <= 2, proof := h7},
  ] "diophantine1_back_enumeration"
  exact h8
```

4. $x,y\in\mathbb{N}^*\Rightarrow 101^x+3\neq103^y$

```Lean
/-
(Class II, Back Mode, with magic prime 701)   101 ^ x + 3 = 103 ^ y
For positive integers x, y satisfying 101 ^ x + 3 = 103 ^ y,
if x >= 1, 103 ^ y = 3 (mod 101).
So y = 69 (mod 100),
which implies y = 19 (mod 25).
Therefore, 103 ^ y = 583 (mod 701).
So 101 ^ x = 580 (mod 701), but this is impossible.
Therefore, x < 1.
So 101 ^ x + 3 = 103 ^ y is impossible.
-/
theorem diophantine1_101_3_103 (x : Nat) (y : Nat) (h1 : x >= 1) (h2 : y >= 1) (h3 : 101 ^ x + 3 = 103 ^ y) :
  False
  := by
  have h4 : x % 1 = 0 := by omega
  have h5 : y % 1 = 0 := by omega
  by_cases h6 : x >= 1
  have h7 := Claim (101 ^ x % 101 = 0) [
    {prop := x % 1 = 0, proof := h4},
    {prop := x >= 1, proof := h6},
  ] "pow_mod_eq_zero"
  have h8 : 103 ^ y % 101 = 3 := by omega
  have h9 := Claim (y % 100 = 69) [
    {prop := y % 1 = 0, proof := h5},
    {prop := y >= 1, proof := h2},
    {prop := 103 ^ y % 101 = 3, proof := h8},
  ] "observe_mod_cycle"
  have h10 := Claim (List.Mem (103 ^ y % 701) [583]) [
    {prop := y % 1 = 0, proof := h5},
    {prop := y >= 1, proof := h2},
    {prop := y % 100 = 69, proof := h9},
  ] "utilize_mod_cycle"
  have h11 := Claim (List.Mem (101 ^ x % 701) [580]) [
    {prop := List.Mem (103 ^ y % 701) [583], proof := h10},
    {prop := 101 ^ x + 3 = 103 ^ y, proof := h3},
  ] "compute_mod_sub"
  have h12 := Claim False [
    {prop := x % 1 = 0, proof := h4},
    {prop := x >= 1, proof := h1},
    {prop := List.Mem (101 ^ x % 701) [580], proof := h11},
  ] "exhaust_mod_cycle"
  apply False.elim h12
  have h7 : x <= 0 := by omega
  have h8 := Claim False [
    {prop :=  x % 1 = 0, proof := h4},
    {prop :=  x >= 1, proof := h1},
    {prop :=  y % 1 = 0, proof := h5},
    {prop :=  y >= 1, proof := h2},
    {prop := 101 ^ x + 3 = 103 ^ y, proof := h3},
    {prop := x <= 0, proof := h7},
  ] "diophantine1_front_enumeration"
  exact h8
```

## 🧪 示例：研究模式 + 二次验证

本项目所生成的 `.lean` 文件并非完全通过 Lean 系统验证，而是依赖于 CoLean 框架进行**二次验证**，因此推荐以下流程：

```bash
# Step 1: 运行程序，生成 Lean4 代码到文件
./diophantine > revalidate/all.lean
# 建议输入如下参数：
2 100 2 100 1 100 2
```

```bash
# Step 2: 调用 CoLean 进行 revalidation（二次验证）
python -m revalidate.run
```

这样可以对生成的 `.lean` 文件进行静态结构检查，辅助分析是否满足 Claim 结构，并调动额外的判定逻辑。
