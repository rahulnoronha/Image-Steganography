from PIL import Image
import os

def JPEG_To_PNG(inputf,outputf):
    input_image_path = os.path.abspath(inputf)
    output_image_path = os.path.abspath(outputf)
    img = Image.open(input_image_path)
    img.save(output_image_path)

def RGB_To_Grayscale(inputf,outputf):
    input_image_path = os.path.abspath(inputf)
    output_image_path = os.path.abspath(outputf)
    img = Image.open(input_image_path).convert('LA')
    img.save(output_image_path)
   