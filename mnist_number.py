import numpy as np
import mnist
import matplotlib.pyplot as plt 
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical


train_images = mnist.train_images() #training data images
train_labels = mnist.train_labels() #training data labels 
test_images = mnist.test_images() #test data images
test_labels = mnist.test_labels() #test data labels

#Normalize the values from [-0.5 - 0.5]
train_images = (train_images/255) - 0.5
test_images = (test_images/255) - 0.5

#Flatten the 28x28 pixel image to a 784 row vector
train_images = train_images.reshape((-1, 784))
test_images = test_images.reshape((-1, 784))

print(train_images.shape) #60000 rows 784 columns
print(test_images.shape) #10000 rows 784 columns


#Build the model
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=784))
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))


#Compile
model.compile(
    optimizer= 'adam',
    loss='categorical_crossentropy', 
    metrics = ['accuracy']
)

#Train images
model.fit(
    train_images, 
    to_categorical(train_labels), #10 dimensional vector
    epochs = 5, # number of iterations over the entire data set
    batch_size = 32 #number of samples per gradient update for training
)

#Evaluate the model
model.evaluate(
    test_images, 
    to_categorical(test_labels)
)


#predict on first 5 images
predictions = model.predict(test_images[:5])
#print models predictions
print(np.argmax(predictions, axis = 1))
print(test_labels[:5])

for i in range(0,5):
    first_image = test_images[i]
    first_image = np.array(first_image, dtype = 'float')
    pixels = first_image.reshape((28, 28)) 
    plt.imshow(pixels)
    plt.show()