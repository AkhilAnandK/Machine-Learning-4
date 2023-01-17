Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\kundu\AppData\Local\Programs\Python\Python38\Assignment4_ML_Akhilanand_Kundurthi.py
Found 4317 files belonging to 5 classes.
Using 3454 files for training.
Found 4317 files belonging to 5 classes.
Using 863 files for validation.

First Architecture


Second Architecture


Third Architecture


Fourth Architecture

[0.3430804908275604, 0.42269831895828247, 0.48407644033432007, 0.5251882076263428, 0.5691951513290405, 0.6045165061950684, 0.6392588019371033, 0.6537348031997681, 0.662420392036438, 0.674001157283783, 0.6852924227714539, 0.7107701301574707, 0.7148233652114868, 0.7188766598701477, 0.7400115728378296, 0.7472495436668396, 0.7553561329841614, 0.7750434279441833, 0.7730168104171753, 0.7903879284858704, 0.7979154586791992, 0.8109438419342041, 0.82657790184021, 0.8300521373748779, 0.8462651968002319]
['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

Test accuracy of fourth architecture is: 0.7311703562736511
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 rescaling (Rescaling)       (None, 150, 150, 3)       0         
                                                                 
 conv2d (Conv2D)             (None, 148, 148, 32)      896       
                                                                 
 max_pooling2d (MaxPooling2D  (None, 74, 74, 32)       0         
 )                                                               
                                                                 
 conv2d_1 (Conv2D)           (None, 72, 72, 16)        4624      
                                                                 
 max_pooling2d_1 (MaxPooling  (None, 36, 36, 16)       0         
 2D)                                                             
                                                                 
 conv2d_2 (Conv2D)           (None, 34, 34, 32)        4640      
                                                                 
 max_pooling2d_2 (MaxPooling  (None, 17, 17, 32)       0         
 2D)                                                             
                                                                 
 conv2d_3 (Conv2D)           (None, 15, 15, 64)        18496     
                                                                 
 max_pooling2d_3 (MaxPooling  (None, 7, 7, 64)         0         
 2D)                                                             
                                                                 
 conv2d_4 (Conv2D)           (None, 5, 5, 128)         73856     
                                                                 
 max_pooling2d_4 (MaxPooling  (None, 2, 2, 128)        0         
 2D)                                                             
                                                                 
 max_pooling2d_5 (MaxPooling  (None, 1, 1, 128)        0         
 2D)                                                             
                                                                 
 flatten (Flatten)           (None, 128)               0         
                                                                 
 dense (Dense)               (None, 128)               16512     
                                                                 
 dropout (Dropout)           (None, 128)               0         
                                                                 
 dropout_1 (Dropout)         (None, 128)               0         
                                                                 
 dense_1 (Dense)             (None, 5)                 645       
                                                                 
=================================================================
Total params: 119,669
Trainable params: 119,669
Non-trainable params: 0
_________________________________________________________________
>>> 