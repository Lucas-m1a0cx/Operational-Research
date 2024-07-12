import numpy as np
from scipy.optimize import minimize

# 定义目标函数
def objective_function():
    def obj(x):
        # 目标函数： -(3*x[0] - (x[0]-1)**2 + 3*x[1] - (x[1]-2)**2)
        return -(3*x[0] - (x[0]-1)**2 + 3*x[1] - (x[1]-2)**2)
    return obj

# 定义第一个约束条件函数
def constraint1(x):
    # 约束条件1: 4 * x[0] + x[1] - 20 ≥ 0
    return 4 * x[0] + x[1] - 20

# 定义第二个约束条件函数
def constraint2(x):
    # 约束条件2: 4 * x[1] + x[0] - 20 ≥ 0
    return 4 * x[1] + x[0] - 20

# 定义约束条件集合
def constraints():
    cons = [{'type': 'ineq', 'fun': constraint1},  # 约束条件1
            {'type': 'ineq', 'fun': constraint2}]  # 约束条件2
    return cons

if __name__ == "__main__":
    ## 初始迭代点
    x0 = np.array([1, 1])  # 初始猜测的解

    ## 获取约束条件
    cons = constraints()

    ## 定义变量的边界
    bnds = ((0, None), (0, None))  # 每个变量的边界 (0, 无上限)

    ## 使用 minimize 函数求解优化问题
    res = minimize(objective_function(), x0, bounds=bnds, constraints=cons)

    ## 打印优化结果
    print(res)
