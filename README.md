# Twitter Sentiment Analysis

This project performs sentiment analysis on Twitter data using two different techniques:
1. VADER (Valence Aware Dictionary and sEntiment Reasoner) - A lexicon and rule-based sentiment analysis tool
2. RoBERTa - A robustly optimized BERT pretraining approach

## Dataset

The project uses the Amazon Fine Food Reviews dataset, which can be found on Kaggle. However, for this analysis, we're using only a subset of 500 reviews.

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- nltk
- transformers
- tqdm

You can install the required packages using:

pip install pandas numpy matplotlib seaborn nltk transformers tqdm

## Project Structure

The project consists of the following main steps:

1. Data Loading and Basic EDA
2. NLTK Basics
3. VADER Sentiment Scoring
4. RoBERTa Pretrained Model Sentiment Analysis
5. Comparison of VADER and RoBERTa results
6. Analysis of discrepancies between model predictions and actual ratings

## How to Run

1. Clone this repository
2. Install the required packages
3. Download the Amazon Fine Food Reviews dataset from Kaggle and place it in the appropriate directory
4. Run the Jupyter notebook or Python script

## Results

The project provides visualizations comparing the sentiment scores from VADER and RoBERTa models with the actual ratings from the dataset. It also includes examples of reviews where the model predictions significantly differ from the actual ratings.

## Future Work

- Experiment with other pretrained models for sentiment analysis
- Increase the sample size for more robust results
- Implement cross-validation for model evaluation
- Try ensemble methods combining multiple models

## Contributors

ADITYA BARNWAL

## License

This project is open source and available under the [MIT License](LICENSE).
