import matplotlib.pyplot as plt
import numpy as np


def generate_circle(center, radius, num_points=150):
    """
    Generate the x and y coordinates of points on a circle.

    Args:
        center (tuple): The (x, y) coordinates of the center of the circle.
        radius (float): The radius of the circle.
        num_points (int, optional): The number of points to generate. Defaults to 150.

    Returns:
        tuple: The x and y coordinates of the generated points.
    """
    # Generate theta values evenly spaced between 0 and 2*pi
    theta = np.linspace(0, 2*np.pi, num_points)

    # Calculate the x and y coordinates of the points on the circle
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)

    return x, y

def circle_intersection_segment(center1, radius1, center2, radius2, num_points=100):
    """
    Calculate the intersection points of two circles along a line segment.

    Args:
        center1 (tuple): The (x, y) coordinates of the center of the first circle.
        radius1 (float): The radius of the first circle.
        center2 (tuple): The (x, y) coordinates of the center of the second circle.
        radius2 (float): The radius of the second circle.
        num_points (int, optional): The number of points to generate. Defaults to 100.

    Returns:
        tuple or None: The x and y coordinates of the intersection points on the circumference of the circles,
                       or None if the circles do not intersect.
    """
    # Calculate the distance between the centers of the circles
    distance = np.linalg.norm(np.array(center1) - np.array(center2))

    # Check if the circles intersect
    if distance < radius1 + radius2:
        # Determine the angle between the centers of the circles
        theta = np.arccos((radius1**2 + distance**2 - radius2**2) / (2 * radius1 * distance))

        # Determine the angle of the line segment relative to the x-axis
        phi = np.arctan2(center2[1] - center1[1], center2[0] - center1[0])

        # Calculate the starting and ending angles of the line segment
        start_angle = phi - theta
        end_angle = phi + theta

        # Generate points along the circle's circumference for the line segment
        angles = np.linspace(start_angle, end_angle, num_points)
        segment_points_x = center1[0] + radius1 * np.cos(angles)
        segment_points_y = center1[1] + radius1 * np.sin(angles)

        return segment_points_x, segment_points_y
    else:
        # Circles do not intersect
        return None, None


def venn2(title='Venn2', circle_labels=['A value', 'B value'], intersection_label='A n B',
          circle_descriptions=['A', 'B'], circle_colors=['red', 'blue'], intersection_color='aqua',
          intersection_strip_color='black', hide_intersection=False):
    """
    Create a Venn diagram with two circles and an intersection segment.

    Args:
        title (str): The title of the Venn diagram.
        circle_labels (list): The labels for the circles.
        intersection_label (str): The label for the intersection segment.
        circle_descriptions (list): The descriptions for the circles.
        circle_colors (list): The colors for the circles.
        intersection_color (str): The color for the intersection segment.
        intersection_strip_color (str): The color for the intersection segment hatch.
        hide_intersection (bool): Whether to hide the intersection segment.

    Returns:
        matplotlib.axes.Axes: The axes object of the Venn diagram.
    """
    # Set the center and radius of the circles
    left_center = (0.32, 0.5)
    right_center = (0.68, 0.5)
    radius = 0.25

    # Generate the coordinates of the circles
    lx, ly = generate_circle(left_center, radius)
    rx, ry = generate_circle(right_center, radius)

    # Create the figure and axes
    fg, ax = plt.subplots(figsize=(9, 9))

    # Set the title and aspect ratio of the axes
    ax.set_title(title, fontsize=14)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    # Draw the circles
    ax.fill(lx, ly, color=circle_colors[0], alpha=0.5)
    ax.fill(rx, ry, color=circle_colors[1], alpha=0.5)

    # Add the circle descriptions
    ax.text(left_center[0], left_center[1] - (radius + 0.1), circle_descriptions[0], ha='center', va='center')
    ax.text(right_center[0], right_center[1] - (radius + 0.1), circle_descriptions[1], ha='center', va='center')

    # Add the circle labels
    ax.text(left_center[0], left_center[1], circle_labels[0], ha='center', va='center')
    ax.text(right_center[0], right_center[1], circle_labels[1], ha='center', va='center')

    # Add the intersection label
    ax.text(0.5, 0.5, intersection_label, ha='center', va='center')

    if not hide_intersection:
        # Calculate the coordinates of the intersection segment
        ilx, ily = circle_intersection_segment(left_center, radius, right_center, radius)
        irx, iry = circle_intersection_segment(right_center, radius, left_center, radius)

        ix = np.concatenate((irx, ilx))
        iy = np.concatenate((iry, ily))

        # Add the intersection segment to the axes
        plt.rcParams["hatch.linewidth"] = 2
        ax.fill(ix, iy, facecolor=intersection_color, edgecolor=intersection_strip_color, hatch='/')

    return ax
