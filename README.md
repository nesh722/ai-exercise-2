\# Titanic Survival Analysis - Assignment 2



\## 1. Approach

I used a modular approach by creating separate Python scripts for each stage of the data pipeline: cleaning, feature engineering, and feature selection. This ensures the code is organized and reusable.



\## 2. Data Cleaning Decisions

\- \*\*Missing Values\*\*: I filled missing 'Age' values with the median. For 'Embarked', I used the most common value (mode). For 'Cabin', I filled missing values with 'U' for Unknown.

\- \*\*Outliers\*\*: I capped the 'Fare' at the 99th percentile to prevent extreme outliers from affecting the model.

\- \*\*Consistency\*\*: I converted 'Sex' to lowercase and removed any duplicate rows.



\## 3. Features Engineered

\- \*\*FamilySize\*\*: Combined siblings and parents into one total count.

\- \*\*Title\*\*: Extracted titles (Mr, Mrs, etc.) from the name column.

\- \*\*Deck\*\*: Extracted the deck letter from the Cabin number.

\- \*\*FarePerPerson\*\*: Created to see the individual cost of a ticket.

\- \*\*Categorical Encoding\*\*: Used One-Hot Encoding for 'Sex', 'Embarked', and 'Title'.



\## 4. Key Findings

Based on the Feature Selection script, the top factors predicting survival were:

1\. \*\*Age\*\*

2\. \*\*FarePerPerson\*\*

3\. \*\*Fare\*\*

4\. \*\*Title (specifically 'Mr')\*\*

5\. \*\*Sex\*\*

