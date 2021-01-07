import Image_Preprocess
import os
import cv2
import matplotlib.pyplot as plt


TEST_IMAGE_PATH = "/home/nithin/miniconda3/envs/Deep_learning/pycharm_projects/sudoku/Sample_images/sample5.jpg"

prep = Image_Preprocess.Preprocess(TEST_IMAGE_PATH)
transformed = Image_Preprocess.Preprocess.extractPuzzleImg(prep)
# plt.imshow(transformed)
# plt.show()
# print(transformed.shape)

temp_image = Image_Preprocess.Preprocess.image_slicer(transformed)



