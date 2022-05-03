# 模拟大量分子（统计意义上）的随机漫步
# 假设步长随机，方向随机

from random import choice
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import distribution_visual


class RandomWalk():
    # 生成随机漫步数据
    def __init__(self, num_points=5000):
        # 存储随机漫步的次数
        self.num_points = num_points
        # 所有随机漫步默认从原点开始
        self.x_value = 0
        self.y_value = 0
        self.z_value = 0

    def get_step(self):
        # 确定前进方向和距离
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4]) # 假设单次在一个方向行走的步长为0-4
        step = direction * distance
        return step

    def fill_walk(self):
        # 分子随机漫步num_points次
        num = 0
        while  num < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_step = self.get_step()
            y_step = self.get_step()
            z_step = self.get_step()
            # 每次需要前进一定数值
            if x_step == 0 and y_step == 0 and z_step == 0:
                continue
            # 计算下一个点的坐标
            self.x_value += x_step
            self.y_value += y_step
            self.z_value += z_step
            
            num += 1

x_values = []
y_values = []
z_values = []

# 设置 5000 个分子，每个分子进行随机漫步50000次
for i in range(5000):

    rw = RandomWalk(50_000)
    rw.fill_walk()

    # 存储5000个分子的最终位置
    x_values.append(rw.x_value)
    y_values.append(rw.y_value)
    z_values.append(rw.z_value)


# 窗口尺寸
fig = plt.figure(figsize=(8, 6), dpi=128)
# 创建3维图形
ax = Axes3D(fig)

ax.scatter(x_values, y_values, z_values, s=1)


# 获取位置分布
frequencies = distribution_visual.distribution(x_values,y_values,z_values)

# 窗口尺寸
plt.figure(figsize=(8,6), dpi=128)

x = list(range(len(frequencies)))
plt.bar(x,frequencies,width=3)

plt.show()
