#program to split an scanned document in jpg/png and crop letters,lines,words
import cv2
from PIL import Image
import os

fname=input("Enter image filename in the format fname.jpg : ")
img = cv2.imread('C:\\users\\ashis\\projects\\pychallenge\\input\\'+fname)

#preprocessing of image starts here
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # Convert the image to gray scale
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)     # Performing OTSU threshold


#-----------------------------------for cropping letters---------------------------------------------------

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))  # Specify structure shape and kernel size. 
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)      # Appplying dilation on the threshold image
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)    # Finding contours
im2 = img.copy()     # Creating a copy of image


# Looping through the identified contours
i=0;
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)   #coordinates of a contour
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)   # Drawing a rectangle around letters on copied image

    name='letter'+str(i)+'.png'                   # define path to save the cropped letter
    path = os.path.join('C:\\users\\ashis\\projects\\pychallenge\\letters\\',name)
    im1=Image.open('C:\\users\\ashis\\projects\\pychallenge\\input\\'+fname)
    letter=im1.crop((x,y,x+w,y+h))                #crop and save letter as png using PIL
    letter.save(path,'PNG')
    i=i+1

#--------------------------------------------------------------------------------------------------------------------------------------------------


#-----------------------------------for cropping words---------------------------------------------------

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # Specify structure shape and kernel size. 
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)      # Appplying dilation on the threshold image
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)    # Finding contours
im2 = img.copy()     # Creating a copy of image


# Looping through the identified contours
i=0;
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)   #coordinates of a contour
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)   # Drawing a rectangle around word on copied image

    name='word'+str(i)+'.png'                   # define path to save the cropped word
    path = os.path.join('C:\\users\\ashis\\projects\\pychallenge\\words\\',name)
    im1=Image.open('C:\\users\\ashis\\projects\\pychallenge\\input\\'+fname)
    letter=im1.crop((x,y,x+w,y+h))                #crop and save word as png
    letter.save(path,'PNG')
    i=i+1

#--------------------------------------------------------------------------------------------------------------------------------------------------


#-----------------------------------for cropping lines---------------------------------------------------

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 1))  # Specify structure shape and kernel size. 
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)      # Appplying dilation on the threshold image
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)    # Finding contours
im2 = img.copy()     # Creating a copy of image


# Looping through the identified contours
i=0;
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)   #coordinates of a contour
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)   # Drawing a rectangle around line on copied image

    name='line'+str(i)+'.png'                   # define path to save the cropped line
    path = os.path.join('C:\\users\\ashis\\projects\\pychallenge\\lines\\',name)
    im1=Image.open('C:\\users\\ashis\\projects\\pychallenge\\input\\'+fname)
    letter=im1.crop((x,y,x+w,y+h))                #crop and save line as png
    letter.save(path,'PNG')
    i=i+1

#--------------------------------------------------------------------------------------------------------------------------------------------------