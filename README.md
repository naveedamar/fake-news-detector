# Fake News Detector

An AI-powered web application that classifies news articles as Real or Fake using Machine Learning.

**Live Demo:** [fake-news-detector.streamlit.app](https://naveedamar-artificial-intelligencefake-news-detectorapp-qq8tom.streamlit.app/)


## Disclaimer
This model is trained on US political news from 2015–2018. It may misclassify articles from other regions, languages, or time periods. It detects writing patterns — it does not fact-check.

## How It Works
Paste any news article or headline into the app. The model analyzes the text and returns a classification (Real or Fake) along with a confidence score.

## Tech Stack
- Python
- Streamlit
- Scikit-learn (TF-IDF + Logistic Regression)
- Pandas
- Joblib
- Kagglehub

## Datasets
- [WELFake Dataset](https://www.kaggle.com/datasets/vcclab/welfake-dataset) — 72,134 articles
- [Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset) — 44,898 articles
- Combined: 116,993 labeled news articles

Datasets are not included in the repo due to file size. Run the following to download them automatically via Kagglehub:
```bash
python dataset.py
```

Make sure your Kaggle API credentials are configured before running. See [Kaggle API setup](https://www.kaggle.com/docs/api).

## Model Accuracy
95.4% on the test set.

## Setup

Install dependencies:
```bash
pip install streamlit scikit-learn pandas joblib python-dotenv kagglehub
```

Download the datasets:
```bash
python dataset.py
```

Train the model:
```bash
python train.py
```

Run the app:
```bash
streamlit run app.py
```
