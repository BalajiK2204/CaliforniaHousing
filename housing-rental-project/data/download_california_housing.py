import pandas as pd
from sklearn.datasets import fetch_california_housing

def download_and_save():
    data = fetch_california_housing(as_frame=True)
    df = pd.concat([data.data, data.target.rename("MedHouseVal")], axis=1)
    df.to_csv("california_housing.csv", index=False)
    print("Dataset downloaded and saved as california_housing.csv")

if __name__ == "__main__":
    download_and_save()