# Dataset Splitter

This script splits a dataset of images into training and testing sets, and randomizes the data before splitting. It is useful for preparing datasets for machine learning models.

## Requirements

- **numpy**: The script requires the `numpy` library for shuffling the dataset. You can install it using pip:
  ```sh
  pip install numpy
  ```

## Usage

You can use the script in two ways:

### 1. Using Constants File

1. **Update Paths**:

   - Open `helpers/constants.py`.
   - Update the `DATASET_PATH` constant with the path to your core dataset.
   - Update the `DATASET_TEST` constant with the path to your desired test dataset location.

2. **Run the Script**:
   - Execute the script from the command line:
     ```sh
     python dataset_splitter.py
     ```

### 2. Using Command Line Arguments

1. **Run the Script with Arguments**:
   - Execute the script from the command line, providing the paths and optional split ratio:
     ```sh
     python dataset_splitter.py path/to/core/dataset path/to/test/dataset --split_ratio 0.7
     ```

## Folder Structure

### Core Dataset Structure

The script expects the core dataset to be organized in subfolders, each representing a different class or label. Each subfolder contains image files. For example:

```
core_dataset/
│
├── subfolder_1/
│   ├── image1.JPEG
│   ├── image2.JPEG
│   └── ...
│
├── subfolder_2/
│   ├── image1.JPEG
│   ├── image2.JPEG
│   └── ...
│
├── subfolder_3/
│   └── ...
│
└── subfolder_n/
    └── ...
```

### Test Dataset Structure

After running the script, the test dataset will have the same structure as the core dataset, with a portion of images moved from the core dataset to the test dataset:

```
test_dataset/
│
├── subfolder_1/
│   ├── image_test1.JPEG
│   ├── image_test2.JPEG
│   └── ...
│
├── subfolder_2/
│   ├── image_test1.JPEG
│   ├── image_test2.JPEG
│   └── ...
│
├── subfolder_3/
│   └── ...
│
└── subfolder_n/
    └── ...
```

## Customization

- **Split Ratio**: The default split ratio is 0.7 (70% training, 30% testing). You can customize this by passing a different value to the `split_dataset` function in `dataset_splitter.py`.

  ```python
  split_dataset(DATASET_PATH, DATASET_TEST, split_ratio=0.8)
  ```

- **Supported File Extensions**: The script currently processes files with the extensions `.jpeg`, `.jpg`, `.png`, `.bmp`, `.gif`, `.tiff`, and `.tif`. If your dataset has images with different extensions, modify the `IMAGE_EXTENSIONS` constant in `helpers/constants.py`.

  ```python
  # helpers/constants.py
  IMAGE_EXTENSIONS = ('.jpeg', '.jpg', '.png', '.bmp', '.gif', '.tiff', '.tif')
  ```
