from pathlib import Path

from keras import Model
from keras.src.applications import VGG16
from keras.src.callbacks import History
from keras.src.layers import Dropout, Flatten, Dense
from keras.src.losses import SparseCategoricalCrossentropy
from keras.src.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot


def train_and_evaluate_model(train_dir: str,
                             evaluate_dir: str,
                             test_dir: str,
                             model_dir: str,
                             model_path: str,
                             plot_filepath: str,
                             batch_size: int,
                             epochs: int):
  model = define_model()

  # create data generator
  datagen = ImageDataGenerator(featurewise_center=True)
  # specify imagenet mean values for centering
  datagen.mean = [123.68, 116.779, 103.939]
  # prepare iterator
  train_it = datagen.flow_from_directory(
    train_dir,
    class_mode="binary",
    batch_size=batch_size,
    target_size=(224, 224)
  )
  validation_it = datagen.flow_from_directory(
    evaluate_dir,
    class_mode="binary",
    batch_size=batch_size,
    target_size=(224, 224)
  )
  # fit model
  history = model.fit_generator(
    train_it,
    steps_per_epoch=len(train_it),
    validation_data=validation_it,
    validation_steps=len(validation_it),
    epochs=epochs,
    verbose=1,
  )
  # test model
  evaluate_it = datagen.flow_from_directory(
    test_dir,
    class_mode="binary",
    batch_size=batch_size,
    target_size=(224, 224)
  )
  _, acc = model.evaluate_generator(evaluate_it, steps=len(evaluate_it), verbose=1)
  evaluate_accuracy_percentage = acc * 100.0
  print("> %.3f" % evaluate_accuracy_percentage)

  Path(model_dir).mkdir(parents=True, exist_ok=True)

  create_history_plots(history, plot_filepath)

  model.save(model_path)


def define_model() -> Model:
  model = VGG16(include_top=False, input_shape=(224, 224, 3))
  # mark loaded layers as not trainable
  for layer in model.layers:
    layer.trainable = False
  # add new classifier layers
  output = model.layers[-1].output
  drop1 = Dropout(0.2)(output)
  flat1 = Flatten()(drop1)
  class1 = Dense(64, activation="relu", kernel_initializer="he_uniform")(flat1)
  output = Dense(3, activation="sigmoid")(class1)
  # define new model
  model = Model(inputs=model.inputs, outputs=output)
  # compile model
  model.compile(optimizer='adam',
                loss=SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])
  return model


def create_history_plots(history: History, plot_filepath: str):
  # plot loss
  pyplot.subplot(211)
  pyplot.title("Cross Entropy Loss")
  pyplot.plot(history.history["loss"], color="blue", label="train")
  pyplot.plot(history.history["val_loss"], color="orange", label="test")
  # plot accuracy
  pyplot.subplot(212)
  pyplot.title("Classification Accuracy")
  pyplot.plot(history.history["accuracy"], color="blue", label="train")
  pyplot.plot(history.history["val_accuracy"], color="orange", label="test")
  # save plot to file
  pyplot.savefig(plot_filepath)
  pyplot.close()
