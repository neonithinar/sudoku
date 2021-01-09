import cv2
import numpy as np
import Preprocessing
import matplotlib.pyplot as plt
import digit_identifier


def show_image(image):
    plt.imshow(image)
    plt.show()


def euclidian_distance(point1, point2):
    """Calcuates the euclidian distance between the point1 and point2
    used to calculate the length of the four sides of the square"""
    distance = np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    return distance


# PERSPECTIVE TRANSFORM

def Perspective_Transform(image, corners):
    def order_corner_points(corners):
        """The function takes in the input from contours and re-arranges them in the order by
        calculating centroid and euclidean distance between the points"""

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

    transformed_image = cv2.resize(transformed_image, (351, 351), interpolation=cv2.INTER_AREA)

    return transformed_image

def readImage(Path):
    return cv2.imread(Path, 0)


def extractPuzzleImg(image):
    """Extracts the puzzle from the image and returns the square image of the whole puzzle
    transformed image = ImgPrep.ExtractPuzzleImg(image_path)"""
    gray = image
    print("shape of the gray image", gray.shape)
    blur = cv2.medianBlur(gray, 3)

    try:
        block_size = 21
        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, block_size, 4)
    except:
        block_size = 20
        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, block_size, 4)

    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.015 * peri, True)
        # print(approx)

        transformed = Perspective_Transform(gray, approx)
        break

    return transformed

def image_slicer(image):
    # edge = image.shape[0] // 9
    # for i in range(0, 8):
    #     for j in range(0, 8):
    #         temp_image = image[(i * edge):((i + 1) * edge), (j * edge): ((j + 1) * edge)]
    #         # temp_image = np.mean(temp_image, axis=2)
    #         # plt.imshow(temp_image)
    #         # plt.show()
    #         # return temp_image
    #         number = digit_identifier.predictor(temp_image)
    #         print("prediction is :", number)

    rows = np.vsplit(image, 9)
    squares = []
    for row in rows:
        columns = np.hsplit(row, 9)
        for square in columns:
            squares.append(square)
    return squares


# todo create digit identifier preprocessing to 28*28 with adaptive theresholding for each square














