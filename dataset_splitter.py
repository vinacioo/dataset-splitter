"""
Dataset Splitter Script

This script splits a dataset of images into training, testing, and validation sets,
and randomizes the data before splitting. It is useful for preparing
datasets for machine learning models.

Usage:
    python dataset_splitter.py [path/to/core/dataset path/to/destination]
        --train_ratio 0.7 --test_ratio 0.2

Arguments:
    dataset_path (str): Path to the core dataset
    destination_path (str): Path to the destination dataset
    train_ratio (float): Ratio of the dataset to be used for training
        (default: 0.7)
    test_ratio (float): Ratio of the dataset to be used for testing
        (default: 0.2)
"""

import argparse
import random
from os import listdir, makedirs
from os.path import isdir, join
from shutil import move, rmtree
from typing import List

from tqdm import tqdm

from helpers.constants import (DATASET_PATH, DESTINATION_PATH,
                               IMAGE_EXTENSIONS, TEST_RATIO, TRAIN_RATIO)


def create_directories(paths: List[str]) -> None:
    """
    Create directories if they do not exist.

    Args:
        paths (List[str]): A list of directory paths to create.
    """
    for path in paths:
        makedirs(path, exist_ok=True)


def split_dataset(
    dataset_path: str,
    destination_path: str,
    train_ratio: float = TRAIN_RATIO,
    test_ratio: float = TEST_RATIO,
) -> None:
    """
    Split the dataset into training, validation, and testing sets.

    Args:
        dataset_path (str): Path to the core dataset.
        destination_path (str): Path to the destination dataset.
        train_ratio (float): Ratio of the dataset to be used for training.
            Default is 0.7.
        test_ratio (float): Ratio of the dataset to be used for testing.
            Default is 0.2.
    """

    val_ratio = 1 - train_ratio - test_ratio
    if val_ratio <= 0:
        raise ValueError("Sum of train_ratio and test_ratio must be less than 1.")

    labels = [
        folder
        for folder in sorted(listdir(dataset_path))
        if isdir(join(dataset_path, folder))
    ]

    intermediate_dir = join(destination_path, "dataset_split")
    create_directories([intermediate_dir])

    for label in tqdm(labels, desc="Processing labels", colour="blue"):
        path_label = join(dataset_path, label)
        images: List[str] = [
            img for img in listdir(path_label) if img.lower().endswith(IMAGE_EXTENSIONS)
        ]
        n_files = len(images)

        random.shuffle(images)

        train_index = int(n_files * train_ratio)
        test_index = int(n_files * test_ratio) + train_index

        train_images = images[:train_index]
        test_images = images[train_index:test_index]
        val_images = images[test_index:]

        dest_train = join(intermediate_dir, "train", label)
        dest_val = join(intermediate_dir, "val", label)
        dest_test = join(intermediate_dir, "test", label)

        create_directories([dest_train, dest_val, dest_test])

        for img in tqdm(
            train_images,
            desc=f"Moving train images for label {label}",
            leave=False,
            colour="green",
        ):
            move(join(path_label, img), join(dest_train, img))
        for img in tqdm(
            val_images,
            desc=f"Moving val images for label {label}",
            leave=False,
            colour="green",
        ):
            move(join(path_label, img), join(dest_val, img))
        for img in tqdm(
            test_images,
            desc=f"Moving test images for label {label}",
            leave=False,
            colour="green",
        ):
            move(join(path_label, img), join(dest_test, img))

        print(f"\nLabel: {label}")
        print(f"Train: {len(train_images)} images stored in {dest_train}")
        print(f"Validation: {len(val_images)} images stored in {dest_val}")
        print(f"Test: {len(test_images)} images stored in {dest_test}")

    print("\nDeleting the empty core dataset directory...")
    rmtree(dataset_path)
    print(f"The empty core dataset directory '{dataset_path}' has been deleted.")
    print("Process finished.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Split a dataset of images into training, validation, and testing sets."
    )
    parser.add_argument(
        "--dataset_path",
        type=str,
        default=DATASET_PATH,
        help="Path to the core dataset",
    )
    parser.add_argument(
        "--destination_path",
        type=str,
        default=DESTINATION_PATH,
        help="Path to the destination dataset",
    )
    parser.add_argument(
        "--train_ratio",
        type=float,
        default=TRAIN_RATIO,
        help="Ratio of the dataset to be used for training (default: 0.7)",
    )
    parser.add_argument(
        "--test_ratio",
        type=float,
        default=TEST_RATIO,
        help="Ratio of the dataset to be used for testing (default: 0.2)",
    )

    args = parser.parse_args()

    split_dataset(
        args.dataset_path, args.destination_path, args.train_ratio, args.test_ratio
    )
