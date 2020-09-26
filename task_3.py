import numpy as np
from scipy import optimize


def solving_3_27():
    c = np.array([2000, 2800, 1200, 1500])
    c = c * (-1)
    a_ub = np.array([[150, 125, 200, 150],
                     [30, 40, 20, 20],
                     [240, 180, 120, 150],
                     [45, 45, 30, 30]])

    b_ub = np.array([2500, 360, 2160, 480])
    opt = optimize.linprog(c, A_ub=a_ub, b_ub=b_ub, bounds=None, method='interior-point')
    min_result = round(opt.fun, 2)
    result = -min_result
    cut_plan = np.array([round(i, 2) for i in opt.x])
    num = 0
    print('Номер 3 задача 27 базовый пункт')
    for i in cut_plan:
        num += 1
        if i != 0:
            print("x{} = {};\n".format(num, i))

    print('Оптимальная прибыль: ', result)


def solving_3_27_a():
    c = np.array([2000, 2800, 1200, 1500])
    c = c * (-1)
    a_ub = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1],
                     [150, 125, 200, 150],
                     [30, 40, 20, 20],
                     [240, 180, 120, 150],
                     [45, 45, 30, 30]])
    a_ub = a_ub * ([-1],
                   [-1],
                   [-1],
                   [-1],
                   [1],
                   [1],
                   [1],
                   [1])
    b_ub = np.array([5, 5, 5, 5, 2500, 360, 2160, 480])
    b_ub = b_ub * [-1, -1, -1, -1, 1, 1, 1, 1]
    opt = optimize.linprog(c, A_ub=a_ub, b_ub=b_ub, bounds=None, method='interior-point')
    min_result = round(opt.fun, 2)
    result = -min_result
    cut_plan = np.array([round(i, 2) for i in opt.x])
    num = 0
    print('Номер 3 задача 27 пункт (а)')
    for i in cut_plan:
        num += 1
        if i != 0:
            print("x{} = {};\n".format(num, i))

    print('Оптимальная прибыль: ', result)


def solving_3_27_b():
    c = np.array([2000, 2800, 1200, 1500])
    c = c * (-1)
    a_ub = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1],
                     [150, 125, 200, 150],
                     [30, 40, 20, 20],
                     [240, 180, 120, 150],
                     [45, 45, 30, 30]])
    a_ub = a_ub * ([-1],
                   [-1],
                   [-1],
                   [-1],
                   [1],
                   [1],
                   [1],
                   [1])
    b_ub = np.array([3, 3, 3, 3, 2500, 360, 2160, 480])
    b_ub = b_ub * [-1, -1, -1, -1, 1, 1, 1, 1]
    opt = optimize.linprog(c, A_ub=a_ub, b_ub=b_ub, bounds=None, method='interior-point')
    min_result = round(opt.fun, 2)
    result = -min_result
    cut_plan = np.array([round(i, 2) for i in opt.x])
    num = 0
    print('Номер 3 задача 27 пункт (b)')
    for i in cut_plan:
        num += 1
        if i != 0:
            print("x{} = {};\n".format(num, i))

    print('Оптимальная прибыль: ', result)


def solving_3_27_e():
    c = np.array([2000, 2800, 1200, 1500])
    c = c * (-1)
    a_ub = np.array([[-1, 1, -1, 1],
                     [150, 125, 200, 150],
                     [30, 40, 20, 20],
                     [240, 180, 120, 150],
                     [45, 45, 30, 30]])

    b_ub = np.array([0, 2500, 360, 2160, 480])
    opt = optimize.linprog(c, A_ub=a_ub, b_ub=b_ub, bounds=None, method='interior-point')
    min_result = round(opt.fun, 2)
    result = -min_result
    cut_plan = np.array([round(i, 2) for i in opt.x])
    num = 0
    print('Номер 3 задача 27 пункт (d)')
    for i in cut_plan:
        num += 1
        if i != 0:
            print("x{} = {};\n".format(num, i))

    print('Оптимальная прибыль: ', result)


# solving_3_27()
# solving_3_27_a()
# solving_3_27_b()
# solving_3_27_e()