# Dataset Splitter

This script splits a dataset of images into training, testing, and validation sets, and randomizes the data before splitting. It is useful for preparing datasets for machine learning models.

## Requirements

The script requires the `tqdm` library for displaying progress bars. You can install it using pip:

```sh
pip install tqdm
```

## Note

**Important:** The core dataset will be deleted after the splitting process is complete. Make sure you have a backup if you need to keep the original dataset.

## Usage

You can use the script in two ways:

### 1. Using Constants File

1. **Update Paths and Ratios**:

   - Open `helpers/constants.py`.
   - Update the `DATASET_PATH` constant with the path to your core dataset.
   - Update the `DESTINATION_PATH` constant with the path to your desired destination dataset location.
   - Optionally, update the `TRAIN_RATIO` and `TEST_RATIO` constants to set default split ratios.

2. **Run the Script**:
   ```sh
   python dataset_splitter.py
   ```

### 2. Using Command Line Arguments

1. **Run the Script with Arguments**:
   - Execute the script from the command line, providing the paths and optional split ratios:
     ```sh
     python dataset_splitter.py --dataset_path path/to/core/dataset --destination_path path/to/destination/dataset --train_ratio 0.7 --test_ratio 0.2
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

### Destination Dataset Structure

After running the script, the destination dataset will have the following structure, with an intermediate directory `dataset_split` and images moved from the core dataset to the respective directories:

```
destination_dataset/
│
└── dataset_split/
    ├── train/
    │   ├── subfolder_1/
    │   │   ├── image1.JPEG
    │   │   ├── image2.JPEG
    │   │   └── ...
    │   ├── subfolder_2/
    │   ├── subfolder_3/
    │   └── subfolder_n/
    │
    ├── val/
    │   ├── subfolder_1/
    │   │   ├── image_val1.JPEG
    │   │   ├── image_val2.JPEG
    │   │   └── ...
    │   ├── subfolder_2/
    │   ├── subfolder_3/
    │   └── subfolder_n/
    │
    └── test/
        ├── subfolder_1/
        │   ├── image_test1.JPEG
        │   ├── image_test2.JPEG
        │   └── ...
        ├── subfolder_2/
        ├── subfolder_3/
        └── subfolder_n/
```

## Customization

- **Split Ratio**: The default split ratios are 0.7 for training and 0.2 for testing. The rest will be used for validation. You can customize this by passing different values to the `split_dataset` function in `dataset_splitter.py` or by updating the `TRAIN_RATIO` and `TEST_RATIO` constants in `helpers/constants.py`.

  ```python
  split_dataset(DATASET_PATH, DESTINATION_PATH, train_ratio=0.8, test_ratio=0.1)
  ```

- **Supported File Extensions**: The script currently processes files with the extensions `.jpeg`, `.jpg`, `.png`, `.bmp`, `.gif`, `.tiff`, and `.tif`. If your dataset has images with different extensions, modify the `IMAGE_EXTENSIONS` constant in `helpers/constants.py`.

  ```python
  # helpers/constants.py
  IMAGE_EXTENSIONS = ('.jpeg', '.jpg', '.png', '.bmp', '.gif', '.tiff', '.tif')
  ```
