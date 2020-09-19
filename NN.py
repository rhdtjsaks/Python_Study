import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top',
               'Trouser',
               'Pullover',
               'Dress',
               'Coat',
               'Sandal',
               'Shirt',
               'Sneaker',
               'Bag',
               'Ankle boot']

def Main():
    print(tf.__version__)

    # Test_0(0)

    global train_images, test_images

    train_images = train_images / 255.0
    test_images = test_images / 255.0

    # Test_1()
    Test_2()


def Test_0(num):
    plt.figure()
    plt.imshow(train_images[num])
    plt.colorbar()
    plt.grid(False)
    plt.show()

def Test_1():
    plt.figure(figsize=(10, 10))

    for i in range(25):
        plt.subplot(5, 5, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid()
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i]])

    plt.show()

def Test_2():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss = 'sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=5)

    test_loss, test_accuracy = model.evaluate(test_images, test_labels, verbose=2)

    print('\nTest Accuracy : ', test_accuracy)

    ### Predictions ###
    predictions = model.predict(test_images)

    # predictions[0]

    # np.argmax(predictions[0])

    # test_labels[0]

    # i = 0
    # plt.figure(figsize=(6, 3))
    # plt.subplot(1, 2, 1)
    # plot_image(i, predictions, test_labels, test_images)
    # plt.subplot(1, 2, 2)
    # plot_value_array(i, predictions, test_labels)
    # plt.show()

    # num_rows = 5
    # num_cols = 3
    # num_images = num_rows * num_cols
    # plt.figure(figsize=(2 * 2 * num_cols, 2 * num_rows))
    # for i in range(num_images):
    #     plt.subplot(num_rows, 2 * num_cols, 2 * i + 1)
    #     plot_image(i, predictions, test_labels, test_images)
    #     plt.subplot(num_rows, 2 * num_cols, 2 * i + 2)
    #     plot_value_array(i, predictions, test_labels)
    # plt.show()

    # 테스트 세트에서 이미지 하나를 선택합니다
    img = test_images[0]

    print(img.shape)

    # 이미지 하나만 사용할 때도 배치에 추가합니다
    img = (np.expand_dims(img, 0))

    print(img.shape)

    predictions_single = model.predict(img)

    print(predictions_single)

    plot_value_array(0, predictions_single, test_labels)
    _ = plt.xticks(range(10), class_names, rotation=45)

    plt.show()

    np.argmax(predictions_single[0])

def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')


if __name__ == "__main__":
    Main()