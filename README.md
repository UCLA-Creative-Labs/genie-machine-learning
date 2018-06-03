# Genie-ML

This repo contains the dataset for the Genie model, as well as a frozen version of the model.

Currently, only a subset of the dataset is labeled. The labeled images are in processed_dataset_1 and their respective labels in annotations_1. Note that these images are greyscale and need to be converted to rgb before used for training.

To train the model, we need a mapping of labels (*.pbtxt) as well as the training set (.record) that is generated from the images and the labels.
