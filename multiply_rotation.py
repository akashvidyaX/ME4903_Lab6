import numpy as np 
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)

def rotation_matrix_z(theta):
    """Generate a rotation matrix for a rotation about the Z-axis by theta."""
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

def rotation_matrix_y(theta):
    """Generate a rotation matrix for a rotation about the Y-axis by theta."""
    return np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

# angles in radians (you'll need to fill these in with the correct values)
theta_1 = 90*np.pi/180  # placeholder
theta_2 = -45*np.pi/180  # placeholder
theta_3 = 0*np.pi/180  # placeholder
theta_4 = 45*np.pi/180  # placeholder

rot_z_theta_1 = rotation_matrix_z(theta_1)
rot_y_theta_2 = rotation_matrix_y(theta_2)
rot_y_theta_3 = rotation_matrix_y(theta_3)
rot_y_theta_4 = rotation_matrix_y(theta_4)
eye = np.eye(3)

# tool frame w.r.t the base frame
rot_0_5 = rot_z_theta_1 @ rot_y_theta_2 @ rot_y_theta_3 @ rot_y_theta_4

print(rot_0_5)

# Given the updated rotation matrix, the columns represent the rotated x, y, and z axes.
x_axis = rot_0_5[:, 0]
y_axis = rot_0_5[:, 1]
z_axis = rot_0_5[:, 2]

print(x_axis)
print(y_axis)
print(z_axis)

# Create vectors for the coordinate frame
origin = np.zeros(3)

# Visualize the coordinate frame
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(*origin, *x_axis, color='r', label='X-axis')
ax.quiver(*origin, *y_axis, color='g', label='Y-axis')
ax.quiver(*origin, *z_axis, color='b', label='Z-axis')

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()
