import cv2
import numpy as np
import Preprocessing
import matplotlib.pyplot as plt
import digit_identifier

class Preprocess:
    """ Aim of this class file is to accept an image as imput and do all the preprocessing
    involving around it involving cv2"""
    def __init__(self, img_path):
        """Initialisation: self, image_path"""
        self.image = cv2.imread(img_path, 0)
        self.original = np.copy(self.image)
        self.extract_grid = False
    @staticmethod
    def show_image(image):
        cv2.imshow("test image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



    def extractPuzzleImg(self):
        """Extracts the puzzle from the image and returns the square image of the whole puzzle
        transformed image = ImgPrep.ExtractPuzzleImg(image_path)"""
        gray = self.image
        blur = cv2.medianBlur(gray, 3)

        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 3)

        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.015 * peri, True)
            # print(approx)

            transformed = Preprocessing.Perspective_Transform(gray, approx)
            break

        return transformed
    @staticmethod
    def image_slicer(image):
        edge = image.shape[0] // 9
        for i in range(0, 8):
            for j in range(0, 8):
                temp_image = image[(i * edge):((i + 1) * edge), (j * edge): ((j + 1) * edge)]
                # temp_image = np.mean(temp_image, axis=2)
                # plt.imshow(temp_image)
                # plt.show()
                # return temp_image
                number = digit_identifier.predictor(temp_image)
                print("prediction is :", number)

















