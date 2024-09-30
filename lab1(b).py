import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)


circle_radius = 5
circle_center = [2, 3]
theta_vals = np.linspace(0, 2 * np.pi, 100)


a = 3
b = 2
foci_distance = np.sqrt(a ** 2 - b ** 2)



def rotated_ellipse(theta, focus, rotation_angle):

    center_x = focus[0] - foci_distance * np.cos(rotation_angle)
    center_y = focus[1] - foci_distance * np.sin(rotation_angle)


    t = np.linspace(0, 2 * np.pi, 100)
    x = a * np.cos(t)
    y = b * np.sin(t)


    x_rot = x * np.cos(rotation_angle) - y * np.sin(rotation_angle)
    y_rot = x * np.sin(rotation_angle) + y * np.cos(rotation_angle)


    x_final = x_rot + center_x
    y_final = y_rot + center_y

    return x_final, y_final



circle, = ax.plot(circle_center[0] + circle_radius * np.cos(theta_vals),
                  circle_center[1] + circle_radius * np.sin(theta_vals), 'r-')


ellipse_line, = ax.plot([], [], 'b-')
tangent_line, = ax.plot([], [], 'g')
point_on_ellipse, = ax.plot([], [], 'bo')
focus_dot, = ax.plot([], [], 'ro')


tangent_length = 20



def animate(i):

    angle = i * 0.02
    ellipse_focus = [circle_center[0] + circle_radius * np.cos(angle),
                     circle_center[1] + circle_radius * np.sin(angle)]


    rotation_angle = angle


    ellipse_x, ellipse_y = rotated_ellipse(0, ellipse_focus, rotation_angle)


    point_x, point_y = ellipse_x[25], ellipse_y[25]


    slope = (ellipse_y[26] - ellipse_y[24]) / (ellipse_x[26] - ellipse_x[24])


    tangent_vector = np.array([1, slope])
    tangent_vector /= np.linalg.norm(tangent_vector)


    tangent_start = np.array([point_x, point_y]) - (tangent_length / 2) * tangent_vector
    tangent_end = np.array([point_x, point_y]) + (tangent_length / 2) * tangent_vector


    ellipse_line.set_data(ellipse_x, ellipse_y)


    point_on_ellipse.set_data([point_x], [point_y])


    tangent_line.set_data([tangent_start[0], tangent_end[0]],
                          [tangent_start[1], tangent_end[1]])


    focus_dot.set_data([ellipse_focus[0]], [ellipse_focus[1]])

    return ellipse_line, point_on_ellipse, tangent_line, focus_dot



ani = FuncAnimation(fig, animate, frames=500, interval=30, blit=True)

plt.show()
