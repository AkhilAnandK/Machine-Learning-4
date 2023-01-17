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

[0.3546612560749054, 0.5602200627326965, 0.6331789493560791, 0.6728430986404419, 0.7162709832191467, 0.7475391030311584, 0.7973363995552063, 0.8291835784912109, 0.8711638450622559, 0.9111175537109375, 0.9293572902679443, 0.9478865265846252, 0.9620729684829712, 0.9672843217849731, 0.9716271162033081, 0.9759699106216431, 0.9808917045593262, 0.9730746746063232, 0.9843659400939941, 0.9817602634429932, 0.9797336459159851, 0.9852344989776611, 0.9852344989776611, 0.984655499458313, 0.989287793636322]
['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

Test accuracy of Second architecture is: 0.7137891054153442
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
                                                                 
 dense_1 (Dense)             (None, 5)                 645       
                                                                 
=================================================================
Total params: 1,994,821
Trainable params: 1,994,821
Non-trainable params: 0
_________________________________________________________________
>>> 