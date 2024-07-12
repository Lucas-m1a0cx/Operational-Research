import numpy as np
from scipy.optimize import minimize

# 定义利润函数 g 和 h
def g(y, c=3):
    return c * y

def h(x_minus_y, d=2):
    return d * x_minus_y

# 定义总利润函数
def total_profit(y_values, x1, n, a, b, c, d):
    total_profit = 0
    x = x1
    for i in range(n):
        y = y_values[i]
        # 确保 y 在合理范围内
        if y < 0 or y > x:
            return np.inf  # 返回无穷大，表示不合理的选择
        total_profit += g(y, c) + h(x - y, d)
        x = a * y + b * (x - y)  # 回收后的原料量
    return -total_profit  # minimize 函数最小化总利润的负值

# 初始原料和参数
x1 = 100
n = 5
a = 0.5
b = 0.4
c = 3
d = 2

# 初始猜测的 y 值
y0 = np.full(n, x1 / 2)

# 约束条件：每个 y 值必须在 0 和 x 之间
bounds = [(0, x1)] * n

# 使用约束条件进行优化
cons = [{'type': 'ineq', 'fun': lambda y_values: x1 - sum(y_values)}] + \
       [{'type': 'ineq', 'fun': lambda y_values, i=i: y_values[i] - 0} for i in range(n)] + \
       [{'type': 'ineq', 'fun': lambda y_values, i=i: x1 - y_values[i]} for i in range(n)]

# 求解最优 y 值以最大化总利润
result = minimize(total_profit, y0, args=(x1, n, a, b, c, d), bounds=bounds)

# 打印结果
optimal_y = result.x
max_profit = -result.fun

print("Optimal y values:", optimal_y)
print("Maximum total profit:", max_profit)
