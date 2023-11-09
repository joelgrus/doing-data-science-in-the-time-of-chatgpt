from dataframe import load_data
import tempfile
import pandas as pd


def test_load_data():
    # First, create a temporary CSV file
    # Make sure there are no extra spaces at the beginning or end of any line
    csv_content = """name,age,salary
John,20,3000
Lucy,25,4000
"""
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write(csv_content)
        filename = f.name

    # Then, load the data from the file
    df = load_data(filename)
    assert df.shape == (2, 3)
    assert df["Name"].tolist() == ["John", "Lucy"]
    assert df["Age"].tolist() == [20, 25]
    assert df["Salary"].tolist() == [3000, 4000]


def test_load_data_missing_values():
    # First, create a temporary CSV file
    # Make sure there are no extra spaces at the beginning or end of any line
    csv_content = """name,age,salary
John,20,3000
Lucy,,
"""
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write(csv_content)
        filename = f.name

    # Then, load the data from the file
    df = load_data(filename)
    assert df.shape == (2, 3)
    assert df["Name"].tolist() == ["John", "Lucy"]
    assert df["Salary"].tolist() == [3000, 0]

    # Check each element individually
    assert df["Age"].tolist()[0] == 20
    assert pd.isna(df["Age"].tolist()[1])
