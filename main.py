import Image_Preprocess
import os
# import cv2
# import matplotlib.pyplot as plt


TEST_IMAGE_PATH = "/home/nithin/miniconda3/envs/Deep_learning/pycharm_projects/sudoku/Sample_images/sample5.jpg"

prep = Image_Preprocess.readImage(TEST_IMAGE_PATH)
Image_Preprocess.show_image(prep)
transformed = Image_Preprocess.extractPuzzleImg(prep)
Image_Preprocess.show_image(transformed)

print(transformed.shape)

# temp_image = Image_Preprocess.Preprocess.image_slicer(transformed)



