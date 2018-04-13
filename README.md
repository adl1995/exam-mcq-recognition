Multiple Choice Questions detector
===================


Description
-

Marks an MCQ type question paper. Assumption is that a student has marked a question by circling the correct option. 

Importance
-

Marking of a question paper is a tedious task. It involves 3 major steps, 

 -  Read student's answer
 -  Match the answer with the provided solution sheet
 - Mark question as right or wrong

Methodology
-
- Apply a gaussian blur to image containing all questions
- Extract edges using Canny Edge Detection algorithm
- Create a reference table for template circle image
- Apply generalized hough transform and match a template circle image and extract column containing all MCQs
- Extract individual MCQs from the extracted column and store its co-ordinates for later use
- Read letter from circled MCQ using cross correlation

Experimental Setup
-
The data was provided in the form of images. Initially, the images were large therefore they were scaled them down by a factor of 3. After this, the template images were extracted from the original image, and were used to build up a reference table. The columns were then extracted from the input image containing all MCQs, which significantly reduced the search space. From this, individual MCQs were extracted using Generalized Hough Transform. The next step was to identify the character present inside the encircled MCQ (e.g. A, B, C). For this, 2D cross-correlation was used to find similarities between two images.

Results
-
The steps followed were robust, but there were some mismatches during Hough Transform application. In this particular case, there was 1 MCQ that was incorrectly matched. Therefore the accuracy for all four input images (present in repository) is 93%. Letter recognition was very robust. 14/15 letters were correctly identified.

![result](https://github.com/adl1995/exam-mcq-recognition/blob/master/result.png)

Third party code
-	

Functions used from other libraries are mentioned below:

- `scipy.ndimage.gaussian_filter()`
- `skimage.filter.canny()`
- `scipy.signal.signaltools.correlate2d()`
	
Libraries
-
- NumPy
- SciPy
- Skimage
- Matplotlib

Limitations
-
The only limitation to the paper checking algorithm is to specify the total number of questions present on every page.

How to run
-
Type:

```
python paper-check.py
```
