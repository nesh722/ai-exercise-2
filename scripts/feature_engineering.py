import pandas as pd
import numpy as np

def engineer_features(df):
    # 1. Create Derived Features
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    
    # Title extraction
    df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    df['Title'] = df['Title'].replace(['Lady', 'Countess','Capt', 'Col','Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    df['Title'] = df['Title'].replace('Mlle', 'Miss').replace('Ms', 'Miss').replace('Mme', 'Mrs')
    
    # Deck extraction
    df['Deck'] = df['Cabin'].apply(lambda x: x[0])
    
    # Age groups
    df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 12, 19, 59, 100], labels=['Child', 'Teen', 'Adult', 'Senior'])
    
    # Fare per person
    df['FarePerPerson'] = df['Fare'] / df['FamilySize']

    # 2. Categorical Encoding
    df = pd.get_dummies(df, columns=['Sex', 'Embarked', 'Title', 'Deck', 'AgeGroup'], drop_first=True)

    # 3. Log Transformation (Fare)
    df['Fare'] = df['Fare'].apply(lambda x: np.log1p(x))
    
    df.to_csv("data/train_engineered.csv", index=False)
    print("Feature engineering complete. Saved to data/train_engineered.csv")
    return df

if __name__ == "__main__":
    df_cleaned = pd.read_csv("data/train_cleaned.csv")
    engineer_features(df_cleaned)