import Image_Preprocess
import os
# import cv2
# import matplotlib.pyplot as plt


TEST_IMAGE_PATH = "/home/nithin/miniconda3/envs/Deep_learning/pycharm_projects/sudoku/Sample_images/sample3.png"

prep = Image_Preprocess.readImage(TEST_IMAGE_PATH)
Image_Preprocess.show_image(prep)
transformed = Image_Preprocess.extractPuzzleImg(prep)
Image_Preprocess.show_image(transformed)

# split the image to smallest squares

sliced_image = Image_Preprocess.image_slicer(transformed)
print(len(sliced_image))





