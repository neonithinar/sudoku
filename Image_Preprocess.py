import os
import cv2
import numpy as np
import Preprocessing



class ImgPrep:
    """ Aim of this class file is to accept an image as imput and do all the preprocessing
    involving around it involving cv2"""
    def __init__(self, img_path):
        """Initialisation: self, image_path"""
        self.image = cv2.imread(img_path, 0)
        self.original = np.copy(self.image)


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
            print(approx)

            transformed = Preprocessing.Perspective_Transform(gray, approx)
            break

        return transformed














