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

configuration = tf.compat.v1.ConfigProto(device_count={"GPU": 0})
session = tf.compat.v1.Session(config=configuration)
# CUDA_VISIBLE_DEVICES=""


def normimg(input_image):
    input_image = np.around(input_image)
    input_image = input_image / 2286.0
    return input_image

# rotation de l'image a fin d'avoir plus d'images ( data ogmentation )
def rot_aug(input_image):
    input_image = ndimage.rotate(input_image, -5, reshape=False)
    return input_image

def flip_aug(input_image):
    input_image = np.flipud(input_image)
    return input_image

def shift_aug(input_image):
    input_image = ndimage.shift(input_image[:, :, 0], (3, -20))
    input_image = np.expand_dims(input_image, axis=-1)
    return input_image

def load_data(data_path):
  data = sorted(glob.glob(data_path))
  total=len(data)
  imag = []
  masks = []
  for count, file in enumerate(data,1):

    image = nib.load(file).get_fdata()[:,:,:,0]
    imag.append(image)  

    print("{} / {}".format(count,total))
  return np.array(imag)



# path to image input
DATA_PATH ='/src/Skin_Segmentation/Inputs/Nifti_images/CT_*.nii.gz'

IMAGES = load_data(DATA_PATH)
print('dimensions: ',IMAGES.shape,' ; ','Type des images: ', type(IMAGES))
# print('dimensions: ',IMAGES.shape,' ; ','Type des images: ', type(IMAGES),' ; ', 'coder sur: ', IMAGES[1].dtype)

# path to model
# new_model = tf.keras.models.load_model('/src/Skin_Segmentation/Weights/model_for_medic.h5')
new_model = tf.keras.models.load_model('/home/islem/Documents/full_projects/PFEenv/src/Skin_Segmentation/Weights/model_for_medic.h5')

# Save Predictions
def predict_data(data_path):
  data = sorted(glob.glob(data_path))
  total=len(data)

  for count, file in enumerate(data,1):
    imags = []
    image = nib.load(file)
    im = normimg(image.get_fdata()[:,:,:,0])
    imags.append(im)
    test=  np.array(imags)
    resultat = new_model.predict(test)
    for i in resultat :
      i = i[:,:] * 5
      i = np.around(i)
      a=i
      i = i[:,:] * 51
      nft_img = nib.Nifti1Image(a, image.affine)
      nib.save(nft_img, os.path.join('/src/Skin_Segmentation/Outputs/Nifti_Outputs/Output_img%01.0d.nii.gz'%count ))
      cv2.imwrite('/src/Skin_Segmentation/Outputs/JPEG_Outputs/Output_img%01.0d.jpeg'%count, i)
      print("{} / {}".format(count,total))
      return np.array(imags)

DATA_PATH ='/src/Skin_Segmentation/Inputs/Nifti_images/CT_*.nii.gz'

predict_data(DATA_PATH)



# data preprocessing ( preparation des images (data) )
# create tha architacture of the reseau de neronnes
# validation ( evaluer les images )
# prediction ( passer a l'algorithme des images jamais vu ) et sa donne un mask
# input : i7waj les images ken sans label( usuful for the trainting of the network )