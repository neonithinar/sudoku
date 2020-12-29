import cv2
import numpy as np
import os
import matplotlib.pyplot as plt


def euclidian_distance(point1, point2):
    """Calcuates the euclidian distance between the point1 and point2
    used to calculate the length of the four sides of the square"""
    distance = np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    return distance


# PERSPECTIVE TRANSFORM

def Perspective_Transform(image, corners):
    def order_corner_points(corners):
        """  # Separate corners into individual points
                 Index 0 - top-right
                       1 - top-left
                       2 - bottom-left
                       3 - bottom-right"""


        sort_corners = [(corner[0][0], corner[0][1]) for corner in corners]
        sort_corners = [list(ele) for ele in sort_corners]

        x, y = [], []
        for i in range(len(sort_corners[:])):
            x.append(sort_corners[i][0])
            y.append(sort_corners[i][1])

        centroid = [sum(x) / len(x), sum(y) / len(y)]
        # print("Centroid: ",centroid)

        for _, item in enumerate(sort_corners):
            if item[0] < centroid[0]:
                if item[1] < centroid[1]:
                    top_l = item
                else:
                    bottom_l = item
            elif item[0] > centroid[0]:
                if item[1] < centroid[1]:
                    top_r = item
                else:
                    bottom_r = item

        return [top_l, top_r, bottom_r, bottom_l]

    # Order points in clockwise order
    ordered_corners = order_corner_points(corners)
    # print("ordered corners: ", ordered_corners)
    top_l, top_r, bottom_r, bottom_l = ordered_corners

    """Determine the widths and heights  ( Top and bottom ) of the image and find the max of them for transform"""

    width1 = euclidian_distance(bottom_r, bottom_l)
    width2 = euclidian_distance(top_r, top_l)

    height1 = euclidian_distance(top_r, bottom_r)
    height2 = euclidian_distance(top_l, bottom_r)

    width = max(int(width1), int(width2))
    height = max(int(height1), int(height2))
    # print("width and height:", width, height)
    # print("Aspect Ratio: ", width / height)

    # Construct new points to obtain top-down view of image in
    # top_r, top_l, bottom_l, bottom_r order
    dimensions = np.array([[0, 0], [width, 0], [width, width],
                           [0, width]], dtype="float32")

    # Convert to Numpy format
    ordered_corners = np.array(ordered_corners, dtype="float32")
    # print("ordered Corners, NP array: ", ordered_corners)

    # Find perspective transform matrix
    matrix = cv2.getPerspectiveTransform(ordered_corners, dimensions)
    """
    plt.imshow(matrix)
    plt.title("Matrix")
    plt.show()
    
    """

    # Return the transformed image
    transformed_image = cv2.warpPerspective(image, matrix, (width, width))

    transformed_image = cv2.resize(transformed_image, (252, 252), interpolation= cv2.INTER_AREA)

    return transformed_image


