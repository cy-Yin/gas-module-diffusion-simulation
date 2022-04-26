# 模拟一个分子的随机漫步
# 假设步长随机，方向随机

from random import choice
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class RandomWalk():
    # 生成随机漫步数据
    def __init__(self, num_points=5000):
        # 存储随机漫步的次数
        self.num_points = num_points
        # 存储随机漫步经过的每个点
        # 所有随机漫步默认从原点开始
        self.x_values = [0]
        self.y_values = [0]
        self.z_values = [0]

    def get_step(self):
        # 确定前进方向和距离
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4]) # 假设单次在一个方向行走的步长为0-4
        step = direction * distance
        return step

    def fill_walk(self):
        # 计算随机漫步包含的所有点
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_step = self.get_step()
            y_step = self.get_step()
            z_step = self.get_step()
            # 每次需要前进一定数值
            if x_step == 0 and y_step == 0 and z_step == 0:
                continue
            # 计算下一个点的坐标
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            next_z = self.z_values[-1] + z_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
            self.z_values.append(next_z)


rw = RandomWalk(50_000)
rw.fill_walk()

point_numbers = range(rw.num_points)

# 窗口尺寸
fig = plt.figure(figsize=(8, 6), dpi=128)
# 创建3维图形
ax = Axes3D(fig)

ax.scatter(rw.x_values, rw.y_values, rw.z_values, c=point_numbers, cmap=plt.cm.Blues, s=0.5)
# 突出显示起点和终点
ax.scatter(0, 0, 0, c='red', s=50)
ax.scatter(rw.x_values[-1], rw.y_values[-1], rw.z_values[-1], c='red', s=50)

plt.show()
