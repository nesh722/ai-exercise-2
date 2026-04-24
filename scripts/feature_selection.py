import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def select_features(df):
    # Drop non-numeric and target columns for selection
    X = df.drop(['Survived', 'Name', 'Ticket', 'Cabin', 'PassengerId'], axis=1)
    y = df['Survived']
    
    # Use Random Forest for Feature Importance
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    
    importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
    
    print("\nTop 10 Features:")
    print(importances.head(10))
    
    return importances.index[:10].tolist()

if __name__ == "__main__":
    df_engineered = pd.read_csv("data/train_engineered.csv")
    select_features(df_engineered)