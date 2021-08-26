


# -*- coding: utf-8 -*-


import cv2
import os
import numpy
import keras
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.layers import Dropout, Flatten, Dense
from keras.models import Sequential
from keras.callbacks import ModelCheckpoint
from keras.preprocessing import image                  
from PIL import ImageFile                            
import numpy as np


#############call page three
#import start_window
#start_window.page_three()

###############Distraction class #########
Classes = [ 'safe driving', ' texting - right', 'talking on the phone - right',
       'texting - left', 'talking on the phone - left', 'operating the radio',
       'drinking', 'reaching behind', 'hair and makeup', 'talking to passenger']

Counter = 0
distractionCounter = {'safe driving':0,
                 'texting - right':0,
                 'talking on the phone - right':0,
                 'texting - left':0,
                 'talking on the phone - left':0,
                 'operating the radio':0,
                 'drinking':0,
                 'reaching behind':0,
                 'hair and makeup':0,
                 'talking to passenger':0}

k = 'open'
##############################Database##############################
from datetime import date
from datetime import datetime
from datetime import timedelta
#connection to database#
import mysql.connector
db=mysql.connector.connect(host="localhost",user="mohamed",
              password="12345",db="dd")

#executing queries#
c=db.cursor()


#create table one time then remove

#c.execute("CREATE TABLE distraction3 (tdate DATE , ttime TIME , type VARCHAR(50) ,counter int , var_counter int )")

#check if table is created terminal
#mysql -u mohamed -p
#password : 12345
#USE dd;
#SHOW TABLES;

##################### Model intialization ##########################


model = Sequential()

model.add(Conv2D(filters=64, kernel_size=2, padding='same', activation='relu', input_shape=(224,224,1), kernel_initializer='glorot_normal'))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(filters=128, kernel_size=2, padding='same', activation='relu', kernel_initializer='glorot_normal'))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(filters=256, kernel_size=2, padding='same', activation='relu', kernel_initializer='glorot_normal'))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(filters=512, kernel_size=2, padding='same', activation='relu', kernel_initializer='glorot_normal'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(500, activation='relu', kernel_initializer='glorot_normal'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax', kernel_initializer='glorot_normal'))


print(model.summary())

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

model.load_weights('distracted-14-1.00 .hdf5')

def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path,color_mode = 'grayscale', target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (1, 224, 224, 1)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 1) and return 4D tensor
    return np.expand_dims(x, axis=0)

##############################Open Camera######################################



cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    #cv2.imshow("test", frame)


    if k  == 'close':
        # ESC pressed
        ### Turn Off The Cammera and Delet All Images ###
        for i in range(img_counter):
            os.remove("opencv_frame_{}.png".format(i))
            img_counter = 0
        print("Escape hit, closing...")
        ###############################
        cam.release()
        cv2.destroyAllWindows()
        import pause_window
        pause_window.page_four()
        break
    else:
        # SPACE pressed
        
        
        ############ Save The Image######################
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        ######### increase the counter of image ##########
        img_counter += 1
        #############Call the model########################
        tensor = path_to_tensor(img_name).astype('float32') / 255 - 0.5
        ypred = model.predict(tensor)
        ypred_class = int(np.argmax(ypred , axis =1))
        print("the pridaction is ",Classes[ypred_class])

        ############# Save in data base####################
        distractioType = Classes[ypred_class]
        if distractioType != 'safe driving' :
            Counter +=1

        distractionCounter[distractioType] += 1

        # INSERT INTO TABLE
        # today = date.today()
        # now = datetime.now()
        # t1= now.strftime("%H:%M:%S")
        # distraction_Type = distractioType
        # count=Counter
        #counterOfDistraction = distractionCounter[distractioType]
        # sql="INSERT INTO distraction3 (tdate , ttime , type , counter , var_counter) VALUES (%s , %s, %s , %s , %s)"
        # data=(today , t1, distraction_Type , count , counterOfDistraction )
        # c.execute(sql,data)
        # db.commit()


cam.release()
cv2.destroyAllWindows()
