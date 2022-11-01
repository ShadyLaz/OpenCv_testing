import sys
import cv2 as cv
import numpy as np


class Image:
    def saveImage(self):
        cv.samples.addSamplesDataSearchPath("C:\\Users\\clazkani\\Anaconda3\\pkgs\\openjpeg-2.4.0-h4fc8c34_0")
        global image
        image = cv.imread(cv.samples.findFile("messi-ronaldo.jpg"))
        #image = cv.imread(cv.samples.findFile("alg.jpg"))
        b = image[:,:,0]
        Image.twoFace(self)
        Image.accessPixel(self)
        Image.cropImage(self)


    def twoFace(self):
        """For Alg photo"""
        #face = image[196:324, 362:637]
        #image[196:324, 46:321] = face

        """For Messi Ronaldo Photo"""
        face = image[19:244, 213:392]
        image[39:264, 780:959] = face



    def cropImage(self):
        roi = cv.selectROI(image)
        print(roi)
        roi_cropped=image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
        cv.imshow("ROI", roi_cropped)
        cv.imwrite("crop.jpeg",roi_cropped)
        cv.waitKey(0)

    def displayImage(self):
        if image is None:
            sys.exit("Could not read the image.")
        cv.imshow("Display window", image)
        k = cv.waitKey(0)
        if k == ord("s"):
            cv.imwrite("starry_night.png", image)

    def accessPixel(self):

        image.itemset((10, 10, 2), 100)
        print(image.item(10, 10, 2))
        print(image.size)
        print(image.dtype)
        print(image.shape)