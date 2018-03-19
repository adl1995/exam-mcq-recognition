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
The data was provided in the form of images. Initially, the images were large therefore they were scaled them down by a factor of 3. After this, these template images were extracted from the original image, these images were used to build up the reference table. Then the extracted columns from the image containing all MCQs, after this individual MCQs were extracted. The next step was to identify the letter inside the circled MCQ. For this, 2D cross-correlation was used to find similarities between two images.

Results
-
The steps followed were very robust, but there were some mismatches during hough transform application. In this particular case, there was 1 MCQ that was incorrectly matched. Therefore the accuracy for all four papers (present in repository) is 93%. Letter recognition was very robust. 14/15 letters were correctly identified.

![result](https://github.com/adl1995/exam-mcq-recognition/blob/master/result.png)

Third party code
-	

Functions used from other libraries are mentioned below:

- scipy.ndimage.gaussian_filter()
-  skimage.filter.canny()
-  scipy.signal.signaltools.correlate2d()
	
Libraries
-
- NumPy
- SciPy
- Skimage
- Matplotlib

Limitations
-
The only limitation to the paper checking algorithm is to specify the total number of questions on a single page.

How to run
-
Type:
  > *python paper-check.py*

