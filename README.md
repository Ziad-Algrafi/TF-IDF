## Objective

The objective of the project is to become familiar with NLP applications, particularly information retrieval. The focus is on determining the importance of words in a corpus using the TF-IDF algorithm.

## Background

The TF-IDF (Term Frequency-Inverse Document Frequency) weight is a statistical measure used in information retrieval and text mining. It evaluates the importance of a word in a document based on its frequency (TF) and inverse document frequency (IDF).

## Problem Statement

The project involves applying the TF-IDF algorithm to a corpus of 4 documents. The goal is to compute TF and IDF values, multiply them to yield vectors, normalize the vectors, and rank the documents using the cosine similarity formula.

## Solution Steps

### I. Computing TF and IDF

| Term         | IDF | TF   | D1  | D2  | D3  | D4  |
|--------------|-----|------|-----|-----|-----|-----|
| application  | 2   | 0.5  | 0   | 0   | 0   | 0   |
| vaccination  | 0.4 | 0.5  | 0.3 | 0   | 0   | 0.3 |
| covid        | 2   | 0    | 0.3 | 0   | 0   | 0   |
| pilgrims     | 2   | 0    | 0   | 0.3 | 0   | 0   |
| health       | 2   | 0    | 0   | 0.3 | 0.3 | 0   |
| certificate  | 2   | 0    | 0   | 0   | 0   | 0.3 |
| center       | 2   | 0.3  | 0   | 0.3 | 0   | 0   |

### II. TF * IDF

|         | D1  | D2  | D3  | D4  |
|---------|-----|-----|-----|-----|
| W1      | 1   | 0.2 | 0   | 0   | 0   | 0   |
| W2      | 0   | 0.12| 0.6 | 0   | 0   | 0.6 |
| W3      | 0   | 0   | 0   | 0.6 | 0.6 | 0   |
| W4      | 0   | 0.12| 0   | 0   | 0   | 0.6 |

### III. Normalization

|         | D1            | D2            | D3            | D4            |
|---------|---------------|---------------|---------------|---------------|
| W1_norm | 0.98058       | 0.19611       | 0             | 0             |
| W2_norm | 0             | 0.19611       | 0.98058       | 0             |
| W3_norm | 0             | 0             | 0             | 0.70710       |
| W4_norm | 0             | 0.19611       | 0             | 0             |

### IV. Cosine Similarity for Query "Covid Vaccination"

| Term         | IDF | TF   |
|--------------|-----|------|
| QUERY        |     |      |
| application  | 2   | 0    |
| vaccination  | 0.4 | 0.5  |
| covid        | 2   | 0.5  |
| pilgrims     | 2   | 0    |
| health       | 2   | 0    |
| certificate  | 2   | 0    |
| center       | 2   | 0    |

|         | Query         |
|---------|---------------|
| WQ      | 0             |
| W1      | 0.98058       |
| W2      | 0             |
| W3      | 0             |
| W4      | 0             |

| Lengths of Documents |               |
|----------------------|               |
| WQ_norm              | 0.99999       |
| W1_norm              | 0.99999       |
| W2_norm              | 1.400         |
| W3_norm              | 0.99999       |
| W4_norm              | 0.99999       |

| Cosine Similarity |               |
|-------------------|               |
| Cos(NQ, ND1)      | 0.03845       |
| Cos(NQ, ND2)      | 0.7142        |
| Cos(NQ, ND3)      | 0             |
| Cos(NQ, ND4)      | 0.03845       |

## Results

The documents in decreasing order of ranks are D2, D4, D1, D3.

## Code Output
![NLP](https://github.com/ZiadAlgrafi/TF-IDF/assets/117011801/34184275-e822-48cb-bb91-8cf913981a4e)

## Installation

To install the required Python packages, run:

```bash
pip install -r requirements.txt
