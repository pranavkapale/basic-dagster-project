import pytest
import pandas as pd
from car_data.assets import load_car_data, transform_car_data

# Test to ensure the dataset loads correctly
def test_load_car_data():
    data = load_car_data()
    assert not data.empty, "Dataset should not be empty"
    assert list(data.columns) == [
        "symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors",
        "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width",
        "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size",
        "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm",
        "city-mpg", "highway-mpg", "price"
    ], "Column names do not match the expected schema"

# Test to validate data transformations
def test_transform_car_data():
    raw_data = pd.DataFrame({
        "symboling": [3, 1],
        "normalized-losses": ["?", 164.0],
        "make": ["alfa-romero", "audi"],
        "fuel-type": ["gas", "gas"],
        "aspiration": ["std", "std"],
        "num-of-doors": ["two", "four"],
        "body-style": ["convertible", "sedan"],
        "drive-wheels": ["rwd", "fwd"],
        "engine-location": ["front", "front"],
        "wheel-base": [88.6, 99.8],
        "length": [168.8, 176.6],
        "width": [64.1, 66.2],
        "height": [48.8, 54.3],
        "curb-weight": [2548, 2337],
        "engine-type": ["dohc", "ohc"],
        "num-of-cylinders": ["four", "four"],
        "engine-size": [130, 109],
        "fuel-system": ["mpfi", "mpfi"],
        "bore": [3.47, 3.19],
        "stroke": [2.68, 3.4],
        "compression-ratio": [9.0, 10.0],
        "horsepower": [111, 102],
        "peak-rpm": [5000, 5500],
        "city-mpg": [21, 24],
        "highway-mpg": [27, 30],
        "price": [13495.0, 13950.0]
    })

    transformed_data = transform_car_data(raw_data)

    # Check if transformations are applied correctly
    assert "price_category" in transformed_data.columns, "Transformed data should include 'price_category' column"
    assert transformed_data["price_category"].iloc[0] == "High", "Price category for first row should be 'High'"
    assert transformed_data["price_category"].iloc[1] == "Medium", "Price category for second row should be 'Medium'"

# Test for missing values
def test_missing_values():
    data = load_car_data()
    assert data.isnull().sum().sum() > 0, "Dataset should have missing values to handle"

# Test for data types
def test_data_types():
    data = load_car_data()
    assert data["price"].dtype == float, "Price column should be of type float"
    assert data["horsepower"].dtype == int, "Horsepower column should be of type int"

