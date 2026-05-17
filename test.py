# Firstly, we need to import the necessary libraries for our test
import pandas as pd
df = pd.read_csv(r"D:\Users\Downloads\archive\creditcard.csv")
df.shape
# We can see that there are 284,807 rows and 31 columns in the dataset. Now, let's check for any missing values in the dataset.
df.isnull().sum()
