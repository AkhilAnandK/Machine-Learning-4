from tensorflow.keras import preprocessing
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Rescaling, Conv2D, Dense, Flatten, MaxPooling2D, Dropout, GlobalAveragePooling2D
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

training_set = preprocessing.image_dataset_from_directory("flowers",
                                                              validation_split=0.2,
                                                              subset="training",
                                                              label_mode="categorical",
                                                              seed=0,
                                                              image_size=(150,150))
test_set = preprocessing.image_dataset_from_directory("flowers",
                                                              validation_split=0.2,
                                                              subset="validation",
                                                              label_mode="categorical",
                                                              seed=0,
                                                              image_size=(150,150))

#First architecture
print("\nFirst Architecture\n")
def first_architecture() :
    """ Trains and evaluates CNN image classifier on the flowers dataset.
        Returns the trained model. """
        
    # build the model
    m = Sequential()
    m.add(Rescaling(1/255))
    m.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(150,150,3)))
    m.add(MaxPooling2D(pool_size=(2, 2)))
    m.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    m.add(MaxPooling2D(pool_size=(2, 2)))
    m.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    m.add(MaxPooling2D(pool_size=(2, 2)))
    m.add(Conv2D(256, kernel_size=(3, 3), activation='relu'))
    m.add(MaxPooling2D(pool_size=(2, 2)))
    m.add(Flatten())
    m.add(Dense(128, activation='relu'))
    m.add(Dropout(0.5))
    m.add(Dense(5, activation='softmax'))

    # setting and training
    m.compile(loss="categorical_crossentropy", metrics=['accuracy'])
    history  = m.fit(training_set, batch_size=32, epochs=25,verbose=0)
    print(history.history["accuracy"])
    print(training_set.class_names)

    # testing
    score = m.evaluate(test_set, verbose=0)
    print('\nTest accuracy of first architecture is:', score[1])
    m.summary()
    m.save("First_Architecture.h5")
    return m

#Second Architecture
print("\nSecond Architecture\n")
def second_architecture() :
    """ Trains and evaluates CNN image classifier on the flowers dataset.
        Returns the trained model. """
    
    # build the model
    m = Sequential()
    m.add(Rescaling(1/255))
    m.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(150,150,3)))
    m.add(MaxPooling2D(pool_size=(2, 2)))
    m.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    m.add(MaxPooling2D(pool_size=(2, 2)))
    m.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    m.add(MaxPooling2D(pool_size=(2, 2)))
    m.add(Conv2D(256, kernel_size=(3, 3), activation='relu'))
    m.add(MaxPooling2D(pool_size=(2, 2)))
    m.add(Flatten())
    m.add(Dense(128, activation='relu'))
    m.add(Dense(5, activation='softmax'))

    # setting and training
    m.compile(loss="categorical_crossentropy", metrics=['accuracy'])
    history  = m.fit(training_set, batch_size=32, epochs=25,verbose=0)
    print(history.history["accuracy"])
    print(training_set.class_names)

    # testing
    score = m.evaluate(test_set, verbose=0)
    print('\nTest accuracy of Second architecture is:', score[1])
    m.summary()
    m.save("Second_Architecture.h5")
    return m

#Third architecture
print("\nThird Architecture\n")
def third_architecture() :
    """ Trains and evaluates CNN image classifier on the flowers dataset.
        Returns the trained model. """
    
    # build the model
    m = Sequential()
    m.add(Rescaling(1/255))
    m.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(150,150,3)))
    m.add(Conv2D(12, kernel_size=(3, 3), activation='relu'))
    m.add(Conv2D(24, kernel_size=(3, 3), activation='relu'))
    m.add(Flatten())
    m.add(Dense(128, activation='relu'))
    m.add(Dropout(0.5))
    m.add(Dense(5, activation='softmax'))

    # setting and training
    m.compile(loss="categorical_crossentropy", metrics=['accuracy'])
    history  = m.fit(training_set, batch_size=32, epochs=25,verbose=0)
    print(history.history["accuracy"])
    print(training_set.class_names)

    # testing
    score = m.evaluate(test_set, verbose=0)
    print('\nTest accuracy of third architecture is:', score[1])
    m.summary()
    m.save("Third_Architecture.h5")
    return m

#Fourth architecture
print("\nFourth Architecture\n")
def fourth_architecture() :
    """ Trains and evaluates CNN image classifier on the flowers dataset.
        Returns the trained model. """
    
    # build the model
    m = Sequential()
    m.add(Rescaling(1/255))
    m.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(150,150,3)))
    m.add(MaxPooling2D(pool_size=(2, 2)))
    m.add(Conv2D(16, kernel_size=(3, 3), activation='relu'))
    m.add(MaxPooling2D(pool_size=(2, 2)))
    m.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
    m.add(MaxPooling2D(pool_size=(2, 2)))
    m.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    m.add(MaxPooling2D(pool_size=(2, 2)))
    m.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    m.add(MaxPooling2D(pool_size=(2, 2)))
    m.add(MaxPooling2D(pool_size=(2, 2)))
    m.add(Flatten())
    m.add(Dense(128, activation='relu'))
    m.add(Dropout(0.5))
    m.add(Dropout(0.5))
    m.add(Dense(5, activation='softmax'))

    # setting and training
    m.compile(loss="categorical_crossentropy", metrics=['accuracy'])
    history  = m.fit(training_set, batch_size=32, epochs=25,verbose=0)
    print(history.history["accuracy"])
    print(training_set.class_names)

    # testing
    score = m.evaluate(test_set, verbose=0)
    print('\nTest accuracy of fourth architecture is:', score[1])
    m.summary()
    m.save("Fourth_Architecture.h5")
    return m


def test_image(m, image_file) :
    """ Classifies the given image using the given model. """
    # load the image
    img = preprocessing.image.load_img(image_file,target_size=(150,150))
    img_arr = preprocessing.image.img_to_array(img)

    # show the image
    plt.imshow(img_arr.astype("uint8"))
    plt.show()

    # classify the image
    img_cl = img_arr.reshape(1,150,150,3)
    score = m.predict(img_cl)
    print(score)

first_architecture()
second_architecture()
third_architecture()
fourth_architecture()

#Testing with the google images
old_model = load_model("Fourth_Architecture.h5")
image_1="Daisy_1.jpg"
image_2="Daisy_2.jpg"
image_3="dandelion_1.jpg"
image_4="dandelion_2.jpg"
image_5="Rose_1.jpg"
image_6="Rose_2.jpg"
image_7="sunflower_1.jpg"
image_8="sunflower_2.jpg"
image_9="tulip_1.jpg"
image_10="tulip_2.jpg"

test_image(old_model,image_1)
test_image(old_model,image_2)
test_image(old_model,image_3)
test_image(old_model,image_4)
test_image(old_model,image_5)
test_image(old_model,image_6)
test_image(old_model,image_7)
test_image(old_model,image_8)
test_image(old_model,image_9)
test_image(old_model,image_10)



    
    


                                                              
    
    
