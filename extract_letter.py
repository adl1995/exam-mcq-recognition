#!/usr/bin/env python

__author__ = "Adeel Ahmad"
__email__ = "adeelahmad14@hotmail.com"
__status__ = "Production"

from skimage.io import imread, imshow
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA
from scipy import ndimage as ndi
from skimage.color import rgb2gray
import skimage
from skimage import feature
import scipy as sp
from scipy.signal.signaltools import correlate2d as c2d

from buildRefTable import *
from matchTable import *
from findMaxima import *

def imgBinarize(img, sigma=3):
	img = ndi.gaussian_filter(img, sigma)
	img = rgb2gray(img)
	img = skimage.filter.canny(img, sigma=1)
	return img

def get(data):
	return (data - data.mean()) / data.std()

def extractLetter(ref):
	ref = rgb2gray(ref)
	# a, b = compare_images(img, ref)	
	img1 = get(rgb2gray(imread('letters/a-new.crop.png')))
	img2 = get(rgb2gray(imread('letters/b-new.crop.png')))
	img3 = get(rgb2gray(imread('letters/c-new.crop.png')))
	img4 = get(rgb2gray(imread('letters/d-new.jpg')))

	c1 = c2d(img1, ref, mode='same')  # baseline
	c2 = c2d(img2, ref, mode='same')
	c3 = c2d(img3, ref, mode='same')
	c4 = c2d(img4, ref, mode='same')

	result = np.array([c1.max(), c2.max(), c3.max(), c4.max()])
	letters = ['a', 'b', 'c', 'd']
	ridx = np.unravel_index(result.argmax(),result.shape) # finding max index

	if (letters[ridx[0]] == 'd' and result[ridx[0]] < 190): # select next match
		result[ridx[0]] = 0
		ridx = np.unravel_index(result.argmax(),result.shape) # finding max index

	return letters[ridx[0]], result[ridx[0]]



# refim = (imgBinarize(rgb2gray(imread('letters/d-new.jpg'))))	
# im = (imgBinarize(rgb2gray(imread('letters/all-letters.jpg'))))
# # extractLetter(ref)


# table = buildRefTable(refim)
# acc = matchTable(im, table)
# val, ridx, cidx = findMaxima(acc)

# # find the half-width and height of template
# hheight = np.floor(refim.shape[0] / 2) + 1
# hwidth = np.floor(refim.shape[1] / 2) + 1

# cstart = max(cidx - hwidth, 1)
# cend = min(cidx + hwidth, im.shape[1] - 1)
# # mcq_col = im[0:im.shape[0]-1, cstart:cend] # column containing all mcq's

# # imsave('match-col-orig.jpg', mcq_col) # saving the matched component

# # convolving our reference image on mcq column
# # acc = matchTable(mcq_col, table)
# # val, ridx, cidx = findMaxima(acc)

# # find coordinates of the box
# rstart = max(ridx - hheight, 1)
# rend = min(ridx + hheight, im.shape[0] - 1)
# # cstart = max(cidx - hwidth, 1)
# # cend = min(cidx + hwidth, im.shape[1] - 1)

# # draw the box
# im[rstart:rend, cstart] = 255
# im[rstart:rend, cend] = 255

# im[rstart, cstart:cend] = 255
# im[rend, cstart:cend] = 255

# plt.imshow(im, cmap='gray')
# plt.show()