#!/usr/bin/python
# -*- coding: utf-8 -*-
# import all the required libraries

#Author: Arun Kumar and Rahul Noronha
#Date:
#23/09/2020
#->Encoding function worked for png only, RGB_To_Grayscale and JPEG_To_PNG throwing IOError
#24/09/2020
#->Encoding function worked for png and jpg only RGB_To_Grayscale worked succesfully,
#->JPEG_To_PNG works only for JPG and fails for JPEG

import cv2
import numpy as np
import types
from Convert_Image import *  # User defined module to Convert JP(E)G to PNG and RGB to Grayscale

# Has two functions RGB_To_Grayscale and JPEG_To_PNG which take parameters input file name and output file name

DELIMETER = '#####'


def to_binary(message):
    '''
    Function to convert the message to be encoded to Binary
    '''

    if type(message) == str:
        return ''.join([format(ord(i), '08b') for i in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [format(i, '08b') for i in message]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, '08b')
    else:
        raise TypeError('Input type not supported')


def hide_data(image, secret_message):
    '''
    Function to Hide the binary data into the Image
    Hidden one bit in LSB of red, green and blue pixel
    LSB technique causes minor change in the pixel values
    TODO: Consider encrypting the hidden message before encoding and decrypting the decoded message later to provide additional security
    '''

    # calculate the maximum bytes that can be encoded
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    print('Maximum bytes to encode:', n_bytes)

    # Check if the number of bytes to encode is less than the maximum bytes in the image
    if len(secret_message) > n_bytes:
        raise ValueError('Error: Insufficient bytes. Need bigger image or less data')

    secret_message += DELIMETER  # you can use any string as the delimeter

    secret_message = to_binary(secret_message)
    data_index = 0
    data_len = len(secret_message)

    for values in image:
        for pixel in values:

            # convert RGB values to binary format
            (r, g, b) = to_binary(pixel)

            # modify the least significant bit only if there is still data to store
            if data_index < data_len:
                # hide the data into least significant bit of red pixel
                pixel[0] = int(r[:-1] + secret_message[data_index], base=2)
                data_index += 1

            if data_index < data_len:
                # hide the data into least significant bit of green pixel
                pixel[1] = int(g[:-1] + secret_message[data_index], base=2)
                data_index += 1

            if data_index < data_len:
                # hide the data into least significant bit of  blue pixel
                pixel[2] = int(b[:-1] + secret_message[data_index], base=2)
                data_index += 1

            # if data is encoded, just break out of the loop
            if data_index >= data_len:
                break

    return image


def unhide_data(image):
    '''
    This function is used to decode the message from the png image file by checking for our preset delimiter DELIMETER which can be changed to anything we want.
    '''

    binary_data = ''
    for values in image:
        for pixel in values:
            (r, g, b) = to_binary(pixel)  # convert the red, green and blue values into binary format
            # extracting data from the least significant bit of red, green and blue pixels
            binary_data += r[-1] + g[-1] + b[-1]

    # split by 8-bits
    all_bytes = [binary_data[i:i + 8] for i in range(0,
                                                     len(binary_data), 8)]

    # convert from bits to characters
    decoded_data = ''
    for byte in all_bytes:
        decoded_data += chr(int(byte, base=2))
        if decoded_data[-5:] == DELIMETER:  # check if we have reached the delimeter which is "#####"
            break

    # print(decoded_data)

    return decoded_data[:-5]  # remove the delimeter to show the original hidden message


def display_image(image, title):
    print('The shape of the image is', image.shape)  # check the shape of image to calculate size in bytes
    resized_image = cv2.resize(image, (500, 500))  # resize the image as per your requirement
    cv2.imshow(title, resized_image)  # display the image
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def encode_text():
    '''
    This function is used to read the message to be encoded and the image file to hide the message in and then decode the message into the image using hide_data.
    TODO: Fails for jpeg images, so fix this.
    '''

    input_image_path = input('Enter image path: ')
    input_image_path = os.path.abspath(input_image_path)
    image = cv2.imread(input_image_path)  # Read the input image using OpenCV-Python.
    if image is None:
        raise FileNotFoundError()

    display_image(image, 'Resized Input Image')

    data = input('Enter data to be encoded : ')
    if len(data) == 0:
        raise ValueError('Data is empty')

    output_image_path = input('Enter path for output image (PNG recommended) : ')
    output_image_path = os.path.abspath(output_image_path)

    encoded_image = hide_data(image, data)
    cv2.imwrite(output_image_path, encoded_image)

    print("Output image has been generated at", output_image_path)


def decode_text():
    # Decode the data in the image
    # read the image that contains the hidden image

    input_image_path = input('Enter image path: ')
    input_image_path = os.path.abspath(input_image_path)
    image = cv2.imread(input_image_path)  # Read the input image using OpenCV-Python.

    display_image(image, 'Resized Image with Hidden text')

    text = unhide_data(image)
    print('Decoded message is ' + text)
    return text


def menu():
    choice = int(input("Encode (1) or Decode (2): "))
    if choice == 1:
        encode_text()
    elif choice == 2:
        print('Decoded message is ' + decode_text())
    else:
        raise Exception('Invalid input.')


def THmain():
    while True:
        menu()
        yn = input("Do you want to continue? (y/n): ").lower()
        if yn != 'y': break


if __name__ == '__main__':
    THmain()
