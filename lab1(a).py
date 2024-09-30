import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider


a = 5
b = 3
total_time = 30
frames = 300


fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)
ax.set_xlim(-a-1, a+1)
ax.set_ylim(-b-1, b+1)
ax.set_aspect('equal')


ellipse_line, = ax.plot([], [], 'b-')
tangent_line, = ax.plot([], [], 'r-')
point, = ax.plot([], [], 'go')


ax_a = plt.axes([0.1, 0.1, 0.65, 0.03])
ax_b = plt.axes([0.1, 0.15, 0.65, 0.03])

s_a = Slider(ax_a, 'Піввісь по осі x (a)', 1, 10, valinit=a)
s_b = Slider(ax_b, 'Піввісь по осі y (b)', 1, 10, valinit=b)


def init():
    ellipse = np.linspace(0, 2 * np.pi, 100)
    x = a * np.cos(ellipse)
    y = b * np.sin(ellipse)
    ellipse_line.set_data(x, y)
    return ellipse_line, tangent_line, point


def update(frame):

    a = s_a.val
    b = s_b.val

    t = frame / frames * 2 * np.pi
    x = a * np.cos(t)
    y = b * np.sin(t)


    dx = -a * np.sin(t)
    dy = b * np.cos(t)


    tangent_x = np.array([x - dx, x + dx])
    tangent_y = np.array([y - dy, y + dy])


    point.set_data([x], [y])
    tangent_line.set_data(tangent_x, tangent_y)


    ellipse = np.linspace(0, 2 * np.pi, 100)
    ellipse_x = a * np.cos(ellipse)
    ellipse_y = b * np.sin(ellipse)
    ellipse_line.set_data(ellipse_x, ellipse_y)

    return ellipse_line, tangent_line, point


ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, repeat=False)


plt.show()
