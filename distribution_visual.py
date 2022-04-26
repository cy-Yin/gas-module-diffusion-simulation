from math import *


def distribution(x_values, y_values, z_values):
    # 创建距离列表
    r = []

    # 计算每个分子的最终位置距离原点的距离
    for i in range(len(x_values)):
        r1 = abs(x_values[i])+abs(y_values[i])+abs(z_values[i])
        r.append(r1)
    
    frequencies = []
    max_result = int(max(r))+1

    # 统计每个距离上的分子数
    for value in range(max_result):
        frequency = r.count(value)
        frequencies.append(frequency)

    return frequencies