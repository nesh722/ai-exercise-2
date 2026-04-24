import pandas as pd
import numpy as np

def clean_data(file_path):
    df = pd.read_csv(file_path)
    
    # 1. Missing Value Handling
    # Age: Impute with median
    df['Age'] = df['Age'].fillna(df['Age'].median())
    
    # Embarked: Impute with mode
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    
    # Cabin: Too many missing values, but we need it for "Deck" later, so fill with 'U' (Unknown)
    df['Cabin'] = df['Cabin'].fillna('U')

    # 2. Outlier Handling (Fare)
    # Capping Fare at the 99th percentile to handle extreme outliers
    q_limit = df['Fare'].quantile(0.99)
    df['Fare'] = np.where(df['Fare'] > q_limit, q_limit, df['Fare'])

    # 3. Data Consistency
    df['Sex'] = df['Sex'].str.lower()
    df = df.drop_duplicates()

    # Save cleaned data
    df.to_csv("data/train_cleaned.csv", index=False)
    print("Data cleaning complete. Saved to data/train_cleaned.csv")
    return df

if __name__ == "__main__":
    clean_data("data/train.csv")