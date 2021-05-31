# from google.colab import drive
# drive.mount('/content/drive')

import os
import nibabel as nib
import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
import tensorflow as tf
# from nibabel.testing import data_path
# from skimage import feature
from scipy import ndimage
import glob
import cv2

# normalisation des images ( enlever les bruits )
def normimg(input_image):
    input_image = np.around(input_image)
    input_image = input_image / 2286.0
    return input_image
def normlab(input_image):
    input_image = input_image / 5.0
    return input_image

# rotation de l'image a fin d'avoir plus d'images ( data ogmentation )
def rot_aug(input_image):
    input_image=ndimage.rotate(input_image,-5,reshape=False)
    return input_image

def flip_aug(input_image):
    input_image=np.flipud(input_image)
    return input_image

def shift_aug(input_image):
    input_image=ndimage.shift(input_image[:,:,0],(3,-20))
    input_image=np.expand_dims(input_image, axis=-1)
    return input_image

folder = '/content/drive/MyDrive/SKIN Layers Segmentation/SKIN_dataset'

# images
imag=[]
# Label
lab =[]

all_files = [
       os.path.join(folder, f)
       for f in os.listdir(folder)
           if os.path.isfile(os.path.join(folder, f))
]

for f in all_files:

    # if img
    if 'CT' in f:
        image =  nib.load(f).get_fdata()[:,:,:,0]
        image =  normimg(image)
        image2 = flip_aug(image)
        image3 = rot_aug(image)
        image4 = rot_aug(image2)
        image5,image6,image7,image8 = shift_aug(image),shift_aug(image2),shift_aug(image3),shift_aug(image4)
        imag.extend((image,image2,image3,image4,image5,image6,image7,image8))
        images=  np.array(imag)

    # if label
    elif 'Label' in f:
        label = nib.load(f).get_fdata()
        label = normlab(label)
        label2 = flip_aug(label)
        label3 = rot_aug(label)
        label4 = rot_aug(label2)
        label5,label6,label7,label8 = shift_aug(label),shift_aug(label2),shift_aug(label3),shift_aug(label4)
        lab.extend((label,label2,label3,label4,label5,label6,label7,label8))
        labels= np.array(lab)

print('les dimensions des images: ', images.shape)
print('les dimensions des labels: ', labels.shape)

IMG_WIDTH = 384
IMG_HEIGHT = 384

# tensorflow
inputs=tf.keras.layers.Input((IMG_WIDTH,IMG_HEIGHT,1))

c1 = tf.keras.layers.Conv2D(16, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(inputs)
c1 = tf.keras.layers.Conv2D(16, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(c1)
p1= tf.keras.layers.MaxPooling2D((2,2))(c1)

c2 = tf.keras.layers.Conv2D(32, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(p1)
c2 = tf.keras.layers.Conv2D(32, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(c2)
p2= tf.keras.layers.MaxPooling2D((2,2))(c2)

c3 = tf.keras.layers.Conv2D(64, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(p2)
c3 = tf.keras.layers.Conv2D(64, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(c3)
p3= tf.keras.layers.MaxPooling2D((2,2))(c3)

c4 = tf.keras.layers.Conv2D(128, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(p3)
c4 = tf.keras.layers.Conv2D(128, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(c4)
p4= tf.keras.layers.MaxPooling2D((2,2))(c4)

c5 = tf.keras.layers.Conv2D(256, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(p4)
c5 = tf.keras.layers.Conv2D(256, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(c5)
p5= tf.keras.layers.MaxPooling2D((2,2))(c5)

#
u6=tf.keras.layers.Conv2DTranspose(128, (2,2), strides=(2, 2), padding='same')(c5)
u6=tf.keras.layers.concatenate([u6,c4])
c6=tf.keras.layers.Conv2D(128, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(u6)
c6=tf.keras.layers.Conv2D(128, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(c6)

u7=tf.keras.layers.Conv2DTranspose(64, (2,2), strides=(2, 2), padding='same')(c6)
u7=tf.keras.layers.concatenate([u7,c3])
c7=tf.keras.layers.Conv2D(64, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(u7)
c7=tf.keras.layers.Conv2D(64, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(c7)

u8=tf.keras.layers.Conv2DTranspose(32, (2,2), strides=(2, 2), padding='same')(c7)
u8=tf.keras.layers.concatenate([u8,c2])
c8=tf.keras.layers.Conv2D(32, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(u8)
c8=tf.keras.layers.Conv2D(32, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(c8)

u9=tf.keras.layers.Conv2DTranspose(16, (2,2), strides=(2, 2), padding='same')(c8)
u9=tf.keras.layers.concatenate([u9,c1])
c9=tf.keras.layers.Conv2D(16, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(u9)
c9=tf.keras.layers.Conv2D(16, (3,3), activation='relu', kernel_initializer='he_normal', padding='same')(c9)

outputs=tf.keras.layers.Conv2D(1, (1,1), activation='sigmoid')(c9)

model=tf.keras.Model(inputs=[inputs], outputs=[outputs])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


model.summary()

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
print('dimensions: ',IMAGES.shape,' ; ','Type des images: ', type(IMAGES),' ; ', 'coder sur: ', IMAGES[1].dtype)

# path to model
new_model = tf.keras.models.load_model('/src/Skin_Segmentation/Weights/model_for_medic.h5')

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