Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\kundu\AppData\Local\Programs\Python\Python38\Assignment4_ML_Akhilanand_Kundurthi.py
Found 4317 files belonging to 5 classes.
Using 3454 files for training.
Found 4317 files belonging to 5 classes.
Using 863 files for validation.
First Architecture

[0.3546612560749054, 0.517081618309021, 0.5909090638160706, 0.6456282734870911, 0.6832658052444458, 0.7162709832191467, 0.7495657205581665, 0.7689635157585144, 0.7828604578971863, 0.8045744299888611, 0.8326578140258789, 0.8514765501022339, 0.8592935800552368, 0.8856398463249207, 0.8821656107902527, 0.9004053473472595, 0.9064852595329285, 0.9203821420669556, 0.9212507009506226, 0.9264620542526245, 0.9221192598342896, 0.9279096722602844, 0.9293572902679443, 0.9313839077949524, 0.9296467900276184]
['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
Test accuracy of first architecture is: 0.7288528680801392
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 rescaling (Rescaling)       (None, 150, 150, 3)       0         
                                                                 
 conv2d (Conv2D)             (None, 148, 148, 32)      896       
                                                                 
 max_pooling2d (MaxPooling2D  (None, 74, 74, 32)       0         
 )                                                               
                                                                 
 conv2d_1 (Conv2D)           (None, 72, 72, 64)        18496     
                                                                 
 max_pooling2d_1 (MaxPooling  (None, 36, 36, 64)       0         
 2D)                                                             
                                                                 
 conv2d_2 (Conv2D)           (None, 34, 34, 128)       73856     
                                                                 
 max_pooling2d_2 (MaxPooling  (None, 17, 17, 128)      0         
 2D)                                                             
                                                                 
 conv2d_3 (Conv2D)           (None, 15, 15, 256)       295168    
                                                                 
 max_pooling2d_3 (MaxPooling  (None, 7, 7, 256)        0         
 2D)                                                             
                                                                 
 flatten (Flatten)           (None, 12544)             0         
                                                                 
 dense (Dense)               (None, 128)               1605760   
                                                                 
 dropout (Dropout)           (None, 128)               0         
                                                                 
 dense_1 (Dense)             (None, 5)                 645       
                                                                 
=================================================================
Total params: 1,994,821
Trainable params: 1,994,821
Non-trainable params: 0
_________________________________________________________________
>>> 