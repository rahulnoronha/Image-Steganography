from PIL import Image
import cv2
import os
images_directory = os.getcwd()

def JPEG_To_PNG(inputf,outputf):
    i_path = os.path.join(images_directory, inputf)
    o_path = os.path.join(images_directory, outputf)
    img = cv2.imread(i_path)
    cv2.imwrite(o_path, img)
    
def RGB_To_Grayscale(inputf,outputf):
    path = os.path.join(images_directory, inputf)
    o_path = os.path.join(images_directory, outputf)
    img = Image.open(path).convert('LA')
    img.save(o_path)
   
"""
def JPEG_To_PNG(inputf,outputf):
    path='F:\\GitHub\\Image_Stenography\\Images\\{}'.format(inputf)
    o_path='F:\\GitHub\\Image_Stenography\\Images\\{}'.format(outputf)
    img = Image.open(path)
    img.save(o_path)
    
def RGB_To_Grayscale(inputf,outputf):
    path='F:\GitHub\Image_Stenography\Images\{}'.format(inputf)
    o_path='F:\GitHub\Image_Stenography\Images\{}'.format(outputf)
    img = Image.open(path).convert('LA')
    img.save(o_path)
"""    


