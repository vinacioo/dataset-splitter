"""
Dataset Splitter Script

This script splits a dataset of images into training and testing sets,
and randomizes the data before splitting. It is useful for preparing
datasets for machine learning models.

Usage:
    python dataset_splitter.py [path/to/core/dataset path/to/test/dataset]
        --split_ratio 0.8

Arguments:
    dataset_path (str): Path to the core dataset
    test_path (str): Path to the test dataset
    split_ratio (float): Ratio of the dataset to be used for training
        (default: 0.7)
"""

import argparse
import os
import shutil
from typing import List

import numpy as np

from helpers.constants import DATASET_PATH, DATASET_TEST, IMAGE_EXTENSIONS


def create_directory(path: str) -> None:
    """
    Create a directory if it does not exist.

    Args:
        path (str): The path of the directory to create.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def split_dataset(dataset_path: str, test_path: str, split_ratio: float = 0.7) -> None:
    """
    Split the dataset into training and testing sets.

    Args:
        dataset_path (str): Path to the core dataset.
        test_path (str): Path to the test dataset.
        split_ratio (float): Ratio of the dataset to be used for training.
            The rest will be used for testing. Default is 0.7.
    """

    labels = [
        folder
        for folder in sorted(os.listdir(dataset_path))
        if os.path.isdir(os.path.join(dataset_path, folder))
    ]

    for label in labels:
        path_label = os.path.join(dataset_path, label)
        images: List[str] = [
            img
            for img in os.listdir(path_label)
            if img.lower().endswith(IMAGE_EXTENSIONS)
        ]
        n_files = len(images)

        # Shuffle the dataset
        np.random.shuffle(images)

        split_index = int(n_files * split_ratio)
        train_images = images[:split_index]
        test_images = images[split_index:]

        dest_test = os.path.join(test_path, label)

        create_directory(test_path)
        create_directory(dest_test)

        for img in test_images:
            shutil.move(os.path.join(path_label, img), os.path.join(dest_test, img))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Split a dataset of images into training and testing sets."
    )
    parser.add_argument(
        "--dataset_path",
        type=str,
        default=DATASET_PATH,
        help="Path to the core dataset",
    )
    parser.add_argument(
        "--test_path", type=str, default=DATASET_TEST, help="Path to the test dataset"
    )
    parser.add_argument(
        "--split_ratio",
        type=float,
        default=0.7,
        help="Ratio of the dataset to be used for training \
                        (default: 0.7)",
    )

    args = parser.parse_args()

    split_dataset(args.dataset_path, args.test_path, args.split_ratio)
