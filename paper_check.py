#!/usr/bin/env python

__author__ = "Adeel Ahmad"
__email__ = "adeelahmad14@hotmail.com"
__status__ = "Production"

from skimage.io import imread, imshow
import matplotlib.pyplot as plt
from buildRefTable import *
from matchTable import *
from findMaxima import *
import numpy as np
from scipy import ndimage as ndi
from skimage import feature
import skimage
from skimage.color import rgb2gray
from scipy.misc import imsave
from skimage.filter import threshold_otsu
from extract_letter import extractLetter
from extract_number import extractNumber
from crop_image import *

def GHT(refim, im):
	table = buildRefTable(refim)
	acc = matchTable(im, table)
	val, ridx, cidx = findMaxima(acc)
	return [ridx,cidx]

def imgBinarize(img, sigma=3):
	img = ndi.gaussian_filter(img, sigma)
	img = rgb2gray(img)
	img = skimage.filter.canny(img, sigma=1)
	return img

def drawBox(refim, im, ridx, cidx, suppress=False):
	# find the half-width and height of template
	hheight = np.floor(refim.shape[0] / 2) + 1
	hwidth = np.floor(refim.shape[1] / 2) + 1
	# find coordinates of the box
	rstart = max(ridx - hheight, 1)
	rend = min(ridx + hheight, im.shape[0] - 1)
	cstart = max(cidx - hwidth, 1)
	cend = min(cidx + hwidth, im.shape[1] - 1)
	# draw the box
	im[rstart:rend, cstart] = 255
	im[rstart:rend, cend] = 255
	im[rstart, cstart:cend] = 255
	im[rend, cstart:cend] = 255
	if (suppress):
		# im[rstart+10:rend-10, cstart+10:cend-10] = 0
		im[rstart:rend, cstart:cend] = 0
	return im

full_images = ['img1-small.jpg','img2-small.jpg','img3-small.jpg','img4-small.jpg']
times_all = [4, 5, 3, 3]
question_no = 1

for img_idx, image in enumerate(full_images):
	# STEP 1: Finding a single circle in whole image
	refim = imgBinarize(imread('circle.jpg'))
	im = imgBinarize(imread(image))
	x, y = GHT(refim, im)
	orig_image = imread(image)
	question_col = im[:,y-80:y-10] # column containing all mcq's
	mcq_col = im[:,y-50:y+50] # column containing all mcq's
	original_mcq_col = orig_image[:,y-50:y+50] # column containing all mcq's

	# STEP 2: Finding all mcq's in the given image subpart
	refim = imgBinarize(imread('circle.jpg'))
	im = mcq_col

	# STEP 3: Sequentially finding all circled mcqs
	idx, times = 0, times_all[img_idx]
	table = buildRefTable(refim)
	match_coord = [[0 for x in range(1)] for y in range(times)]
	mcq_loc = []
	mcq_ans = []
	while (times != 0):
		# convolving our reference image on mcq column
		acc = matchTable(im, table)
		val, ridx, cidx = findMaxima(acc)

		# print ridx, " ", cidx
		# STEP 4: Storing location for matched mcq
		match_coord[idx].append([ridx,cidx])
		mcq_loc.append(ridx)
		# find the half-width and height of template
		hheight = np.floor(refim.shape[0] / 2) + 1
		hwidth = np.floor(refim.shape[1] / 2) + 1
		# find coordinates of the box
		rstart = max(ridx - hheight, 1)
		rend = min(ridx + hheight, im.shape[0] - 1)
		cstart = max(cidx - hwidth, 1)
		cend = min(cidx + hwidth, im.shape[1] - 1)
	
		mcq_circle = original_mcq_col[rstart+10:rend-10, cstart+10:cend-10]
		imsave('matched-mcq/image'+str(img_idx)+'-mcq'+str(idx)+'.jpg', mcq_circle) # saving the matched component
		# STEP 5: extracting letter from our mcq
		ans, val = extractLetter(mcq_circle)

		mcq_ans.append(ans)

		im = drawBox(refim, im, ridx, cidx, suppress=True)

		imsave('columns/image'+str(img_idx)+'-match-col.jpg', im) # saving the matched component
		imsave('columns_question/image'+str(img_idx)+'-match-col.jpg', question_col)
		times -= 1
		idx+=1


	# STEP 6: Sorting mcqs based on their coordinates
	sorted_ans = [x for (y,x) in sorted(zip(mcq_loc,mcq_ans))]
	for answer in sorted_ans:
		print question_no, ". selected option: ", answer
		question_no+=1

	# STEP 7: Read question numbers (ignored)
	# for i in range(len(match_coord)):
	# 	# print match_coord[i][1][0], " ", match_coord[i][1][1]
	# 	# print orig_image.shape[1]
	# 	# test = imgBinarize(orig_image[match_coord[i][1][0]-50:match_coord[i][1][0]+50,:])
	# 	height_start = match_coord[i][1][0]-500
	# 	if (height_start < 0):
	# 		height_start = match_coord[i][1][0]-300
	# 	print "height start : ", height_start
	# 	if (img_idx == 0 or img_idx == 3):
	# 		test = imgBinarize(orig_image[height_start:match_coord[i][1][0],160:160+90])
	# 	else:
	# 		test = imgBinarize(orig_image[height_start:match_coord[i][1][0],80:80+90])
	# 	number_pic = process_image(test)
	# 	number, val = extractNumber(number_pic)
	# 	print "number : ", number, " val : ", val
	# 	imsave('matched/image'+str(img_idx)+'-test'+str(i)+'.jpg', test) # saving the matched component
	# 	plt.imshow(mcq_circle, cmap='gray')
	# 	# plt.show()