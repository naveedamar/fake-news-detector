# dataset 1: https://www.kaggle.com/datasets/vcclab/welfake-dataset
# has one file WELFake_Dataset.csv
import kagglehub

# Download latest version
path = kagglehub.dataset_download("vcclab/welfake-dataset")

print("Path to dataset files:", path)

# dataset 2: https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset
# has two files Fake.csv and True.csv
import kagglehub

# Download latest version
path = kagglehub.dataset_download("clmentbisaillon/fake-and-real-news-dataset")

print("Path to dataset files:", path)