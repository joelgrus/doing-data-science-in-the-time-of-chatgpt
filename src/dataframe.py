import pandas as pd


def load_data(filename: str) -> pd.DataFrame:
    """
    Load data from the specified CSV file.
    Make sure all the column names start with capital letters.
    In the "Salary" column fill missing values with 0.
    """
    df = pd.read_csv(filename)
    df.columns = [col.capitalize() for col in df.columns]
    df["Salary"].fillna(0, inplace=True)
    return df
