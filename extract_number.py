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

def extractNumber(ref):
	ref = rgb2gray(ref)
	# a, b = compare_images(img, ref)	
	img1 = get(imgBinarize(rgb2gray(imread('numbers/1.crop.png'))))
	img2 = get(imgBinarize(rgb2gray(imread('numbers/2.crop.png'))))
	img3 = get(imgBinarize(rgb2gray(imread('numbers/3.crop.png'))))
	img4 = get(imgBinarize(rgb2gray(imread('numbers/4.crop.png'))))
	img5 = get(imgBinarize(rgb2gray(imread('numbers/5.crop.png'))))
	img6 = get(imgBinarize(rgb2gray(imread('numbers/6.crop.png'))))
	img7 = get(imgBinarize(rgb2gray(imread('numbers/7.crop.png'))))
	img8 = get(imgBinarize(rgb2gray(imread('numbers/8.crop.png'))))
	img9 = get(imgBinarize(rgb2gray(imread('numbers/9.crop.png'))))
	img10 = get(imgBinarize(rgb2gray(imread('numbers/10.crop.png'))))
	img11 = get(imgBinarize(rgb2gray(imread('numbers/11.crop.png'))))
	img12 = get(imgBinarize(rgb2gray(imread('numbers/12.crop.png'))))
	img13 = get(imgBinarize(rgb2gray(imread('numbers/13.crop.png'))))
	img14 = get(imgBinarize(rgb2gray(imread('numbers/14.crop.png'))))
	img15 = get(imgBinarize(rgb2gray(imread('numbers/15.crop.png'))))

	c1 = c2d(img1, ref, mode='same')  # baseline
	c2 = c2d(img2, ref, mode='same')
	c3 = c2d(img3, ref, mode='same')
	c4 = c2d(img4, ref, mode='same')
	c5 = c2d(img5, ref, mode='same')
	c6 = c2d(img6, ref, mode='same')
	c7 = c2d(img7, ref, mode='same')
	c8 = c2d(img8, ref, mode='same')
	c9 = c2d(img9, ref, mode='same')
	c10 = c2d(img10, ref, mode='same')
	c11 = c2d(img11, ref, mode='same')
	c12 = c2d(img12, ref, mode='same')
	c13 = c2d(img13, ref, mode='same')
	c14 = c2d(img14, ref, mode='same')
	c15 = c2d(img15, ref, mode='same')

	result = np.array([c1.max(), c2.max(), c3.max(), c4.max(), c5.max(), c6.max(), c7.max(), c8.max(), c9.max(), c10.max(), c11.max(), c12.max(), c13.max(), c14.max(), c15.max()])
	letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
	ridx = np.unravel_index(result.argmax(),result.shape) # finding max index

	# if (letters[ridx[0]] == 'd' and result[ridx[0]] < 190): # select next match
	result[ridx[0]] = 0
	ridx = np.unravel_index(result.argmax(),result.shape) # finding max index

	return letters[ridx[0]], result[ridx[0]]


																											
# refim = (rgb2gray(imread('matched/image1-test1.crop.png')))
# # plt.imshow(refim, cmap='gray')	
# # refim = (imgBinarize(rgb2gray(imread('numbers/9.jpg'))))	
# num, val = extractNumber(refim)
# print num, val
					