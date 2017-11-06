import os
import numpy
import shutil

# path of the core folder
DATASET_PATH = ''

# destiny path of the test dataset
DATASET_TEST = ''

# labels inside of the core folder
labels = [folder for folder in sorted(os.listdir(DATASET_PATH))]

for label in labels:
    path_label = os.path.join(DATASET_PATH, label)
    n_img = []
    n_img += [i for i in os.listdir(path_label) if i.endswith('.JPEG')]
    n_files = len(n_img)

    # ratio of split
    split_ratio = 0.7

    split_index = int(n_files * split_ratio)

    # shuffling the dataset
    numpy.random.shuffle(n_img)

    train = n_img[0:split_index]
    test = n_img[split_index:]

    dest_test = os.path.join(DATASET_TEST, label)

    if not os.path.exists(DATASET_TEST):
        os.makedirs(DATASET_TEST)

    if not os.path.exists(dest_test):
        os.makedirs(dest_test)

    for n_test in test:
        if not os.path.exists(os.path.join(dest_test, n_test)):
            shutil.move(os.path.join(path_label, n_test), dest_test)
