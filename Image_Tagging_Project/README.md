# Image Tagging Project

This project is an **Image Classification Model** using **TensorFlow** and **CNN (Convolutional Neural Network)**.

## Classes

- Cat
- Dog
- Car

## Dataset Structure
dataset/
│
├── cat/
│   ├── cat1.jpg
│   ├── cat2.jpg
│   ├── cat3.jpg
│   └── ...
│
├── dog/
│   ├── dog1.jpg
│   ├── dog2.jpg
│   ├── dog3.jpg
│   └── ...
│
└── car/
    ├── car1.jpg
    ├── car2.jpg
    ├── car3.jpg
    └── ...
```

The dataset contains images of:
- **Cat**
- **Dog**
- **Car**

These images are used to train and validate the image classification model.

## Technologies Used

- Python
- TensorFlow
- NumPy
- Matplotlib

## Features

- Image Classification
- CNN Model
- Data Augmentation
- Accuracy Evaluation

## How to Run

### Install Libraries

```bash
pip install tensorflow matplotlib numpy
```

### Run Training

```bash
python train.py
```

### Run Prediction

```bash
python predict.py
```

## Output

The model predicts image categories such as:

- Cat
- Dog
- Car
