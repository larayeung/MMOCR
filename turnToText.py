# pip install pillow
from PIL import ImageGrab, Image
import pytesseract
import argparse
import cv2
import os
import numpy as np


def makeText(imageToTranslate):
    image = cv2.cvtColor(np.array(imageToTranslate), cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # check to see if we should apply thresholding to preprocess the
    # image
    #if args["preprocess"] == "thresh":
    if True:
        gray = cv2.threshold(gray, 0, 255,
            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # make a check to see if median blurring should be done to remove
    # noise
    #elif args["preprocess"] == "blur":
    #    gray = cv2.medianBlur(gray, 3)
    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    #cv2.imwrite(filename, gray)
    cv2.imwrite(filename, image)
    #print(filename)
    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    return text, image, gray


if __name__ == "__main__":
    imgFromClipBoard = ImageGrab.grabclipboard()
    '''
    if isinstance(imgFromClipBoard, PIL.PngImagePlugin.PngImageFile):
        pass
    else:
        print("not the right type")
    '''
    print(type(imgFromClipBoard))
    print(imgFromClipBoard)

    text, image, gray = makeText(imgFromClipBoard)

    print(text)
    # show the output images
    cv2.imshow("Image", image)
    cv2.imshow("Output", gray)
    cv2.waitKey(0)