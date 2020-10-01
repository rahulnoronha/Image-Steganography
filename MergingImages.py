# Vary these as per need
PUBLIC = r"images/image4.jpg"
SECRET = r"images/image3.jpg"
NF_BITS = 7
# PUBLIC = r"images/image7.jpg"
# SECRET = r"images/image9.jpg"
# NF_BITS = 3

from Stenography import *
import cv2
import numpy as np

def merge_images(pub_image, secret_image, nf_bits):
	"""
	Hides secret_image inside pub_image in least significant `nf_bits` bits.
	"""

	# Raise an error if secret_image doesn't fit inside pub_image
	if pub_image.shape[0] < secret_image.shape[0] or pub_image.shape[1] < secret_image.shape[1]:
		raise ValueError("Public image is smaller than SECRET image.")

	# Converting to numpy array for concise calculations
	pub_image = np.array(pub_image, np.uint8)
	secret_image = np.array(secret_image, np.uint8)
	# the parts of the result image that don't contain the secret_image should remain the same
	res_image = np.array(pub_image, np.uint8) 
	rows, cols = pub_image.shape[0], pub_image.shape[1]
	pri_rows, pri_cols = secret_image.shape[0], secret_image.shape[1]
	
	"""
	Example:
	nf_bits = 3
	Public pixel: (167, 93, 27) == (10100 111, 01011 101, 00011 011)    
	Secret pixel: (67, 200, 105) == (010 00011, 110 01000, 011 01001)    
	Output pixel: (162, 94, 27) == (10100 010, 01011 110, 00011 011)

	mask = 1111 1111 - 0000 0111 = 1111 1000
	public_pixel & mask = 10100 111 & 11111 000 = 10100 000
	010 00011 shr by (8 - 3) bits = 00000 010
	10100 000 or 00000 010 = 10100 010 = result
	"""
	mask = 2**8 - 2**nf_bits
	# applying this transformation only to the area of the image that will hide the secret_image
	res_image[0:pri_rows, 0:pri_cols, :] = \
		(mask & pub_image[0:pri_rows, 0:pri_cols, :]) | \
		secret_image >> (8 - nf_bits)
	return res_image


def unmerge_image(artificial_image, nf_bits):
	artificial_image = np.array(artificial_image, np.uint8)
	# Shifting left would show
	artificial_image <<= (8 - nf_bits)
	return artificial_image

def IHmain():
	pub_image_path = PUBLIC
	secret_image_path = SECRET
	nf_bits = NF_BITS

	pub_image = cv2.imread(pub_image_path)
	secret_image = cv2.imread(secret_image_path)
	result = merge_images(pub_image, secret_image, nf_bits)
	display_image(result, "Merged")
	hidden = unmerge_image(result, nf_bits)
	display_image(hidden, "Reveal")




if __name__ == '__main__':
	IHmain()
