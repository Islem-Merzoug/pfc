import os
import nibabel as nib
import numpy as np 
# import pandas as pd
# import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from nibabel.testing import data_path
# from skimage import feature
from scipy import ndimage
import glob
import cv2

# path to image input
# DATA_PATH ='../Inputs/Nifti_images/CT_*.nii.gz'
image_path ='/src/Inputs/JPEG_Inputs/JPEG_CT_27.JPG'

# Image directory
directory ='/src/Outputs/JPEG_Outputs'

# to read the image
image = cv2.imread(image_path)

# process
# image = ndimage.rotate(image, -5, reshape=False)


# to specified directory 
os.chdir(directory)

print("Before saving image:")  
print(os.listdir(directory))  

# Filename
filename = 'savedImage.jpg'

# Saving the image
cv2.imwrite(filename, image)

print("After saving image:")  
print(os.listdir(directory))
  
print('Successfully saved')