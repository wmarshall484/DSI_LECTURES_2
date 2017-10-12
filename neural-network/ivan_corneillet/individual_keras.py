from utilities import load_data

train, validation, test = load_data('data/mnist.pkl.gz', True)

X_train = train[0]
y_train = train[1]

X_validation = validation[0]
y_validation = validation[1]

from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD

model = Sequential()

model.add(Dense(30, input_dim=X_train.shape[1]))
model.add(Activation('sigmoid'))

model.add(Dense(10))
model.add(Activation('softmax'))

sgd = SGD(lr=.001)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=validation)

print model.evaluate(X_train, y_train)
print model.evaluate(X_validation, y_validation)
