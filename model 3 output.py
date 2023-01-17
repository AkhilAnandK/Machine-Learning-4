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

[0.33960625529289246, 0.5442964434623718, 0.6887666583061218, 0.8126809597015381, 0.8920092582702637, 0.9296467900276184, 0.9551244974136353, 0.9701794981956482, 0.9748117923736572, 0.9748117923736572, 0.9748117923736572, 0.9808917045593262, 0.9800231456756592, 0.984655499458313, 0.981181263923645, 0.9832078814506531, 0.981181263923645, 0.9762594103813171, 0.987261176109314, 0.9843659400939941, 0.9791545867919922, 0.9924724698066711, 0.9840764403343201, 0.987261176109314, 0.98552405834198]
['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

Test accuracy of third architecture is: 0.5469292998313904
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 rescaling (Rescaling)       (None, 150, 150, 3)       0         
                                                                 
 conv2d (Conv2D)             (None, 148, 148, 32)      896       
                                                                 
 conv2d_1 (Conv2D)           (None, 146, 146, 12)      3468      
                                                                 
 conv2d_2 (Conv2D)           (None, 144, 144, 24)      2616      
                                                                 
 flatten (Flatten)           (None, 497664)            0         
                                                                 
 dense (Dense)               (None, 128)               63701120  
                                                                 
 dropout (Dropout)           (None, 128)               0         
                                                                 
 dense_1 (Dense)             (None, 5)                 645       
                                                                 
=================================================================
Total params: 63,708,745
Trainable params: 63,708,745
Non-trainable params: 0
_________________________________________________________________
>>> 