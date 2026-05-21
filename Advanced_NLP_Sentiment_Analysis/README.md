# Advanced NLP Project: Sentiment Analysis using Hugging Face

## Project Overview

This project is an **AI-driven Natural Language Processing (NLP)** application that uses a **pre-trained Language Model (LM)** from **Hugging Face Transformers** to perform **sentiment analysis** on text.

The model predicts whether a sentence expresses:

- Positive Sentiment
- Negative Sentiment

---

## Objective

The objective of this project is to implement a **Language Model (LM)** in a **Jupyter Notebook** and analyze its performance and capabilities for sentiment prediction.

---

## Language Model Used

This project uses a **pre-trained Hugging Face Transformer model** for sentiment analysis.

**Model Used:**

```text
Hugging Face Transformers Pipeline
```

---

## Technologies Used

- Python
- Hugging Face Transformers
- PyTorch
- Jupyter Notebook

---

## Project Features

- Sentiment Analysis
- NLP Language Model Implementation
- Positive/Negative Text Classification
- Multiple Sentence Prediction
- Performance Analysis

---

## Project Structure

```text
Advanced_Task_NLP_Sentiment_Analysis/
│
├── dataset/
│   └── sample_texts.txt
│
├── sentiment_analysis.ipynb
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Sample Dataset

Example text samples used for testing:

```text
I love this internship
This project is difficult
Python is amazing
I hate bugs
Machine Learning is interesting
```

---

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## How to Run the Project

### Step 1: Open Jupyter Notebook

```bash
jupyter notebook
```

### Step 2: Open the Notebook File

```text
sentiment_analysis.ipynb
```

### Step 3: Run All Cells

Execute the notebook step by step to analyze sentiment.

---

## Example Output

### Input:

```text
I love this internship
```

### Output:

```text
POSITIVE
```

### Input:

```text
This project is difficult
```

### Output:

```text
NEGATIVE
```

---

## Strengths

- Fast prediction
- Easy to implement
- High accuracy using pre-trained models
- Effective for NLP tasks

---

## Limitations

- May not fully understand complex context
- Prediction quality depends on pre-trained model performance

---

## Conclusion

This project successfully demonstrates the implementation of a **Language Model (LM)** for **Natural Language Processing (NLP)** using **Hugging Face Transformers**. The model effectively classifies text sentiment as positive or negative.
