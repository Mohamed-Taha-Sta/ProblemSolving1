# 2879
import pandas as pd
import pytest

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

def test_selectFirstRows_with_valid_dataframe():
    # Given
    data = {'Name': ['Tom', 'Nick', 'John', 'Eric'],
            'Age': [20, 21, 19, 18]}
    df = pd.DataFrame(data)

    # When
    result = selectFirstRows(df)

    # Then
    assert len(result) == 3
    assert result.equals(df.head(3))

def test_selectFirstRows_with_empty_dataframe():
    # Given
    df = pd.DataFrame()

    # When
    result = selectFirstRows(df)

    # Then
    assert len(result) == 0

def test_selectFirstRows_with_less_than_three_rows():
    # Given
    data = {'Name': ['Tom', 'Nick'],
            'Age': [20, 21]}
    df = pd.DataFrame(data)

    # When
    result = selectFirstRows(df)

    # Then
    assert len(result) == 2
    assert result.equals(df)