import pytest
from app.conversion_operations import (
    celsius_to_fahrenheit, fahrenheit_to_celsius,
    km_to_miles, miles_to_km,
    kg_to_pounds, pounds_to_kg
)

# Test para celsius_to_fahrenheit
def test_celsius_to_fahrenheit():
    # Arrange
    celsius = 0
    expected_fahrenheit = 32

    # Act
    result = celsius_to_fahrenheit(celsius)

    # Assert
    assert result == expected_fahrenheit

def test_celsius_to_fahrenheit_negative():
    # Arrange
    celsius = -40
    expected_fahrenheit = -40

    # Act
    result = celsius_to_fahrenheit(celsius)

    # Assert
    assert result == expected_fahrenheit

# Test para fahrenheit_to_celsius
def test_fahrenheit_to_celsius():
    # Arrange
    fahrenheit = 32
    expected_celsius = 0

    # Act
    result = fahrenheit_to_celsius(fahrenheit)

    # Assert
    assert result == expected_celsius

def test_fahrenheit_to_celsius_high():
    # Arrange
    fahrenheit = 212
    expected_celsius = 100

    # Act
    result = fahrenheit_to_celsius(fahrenheit)

    # Assert
    assert result == expected_celsius

# Test para km_to_miles
def test_km_to_miles():
    # Arrange
    km = 1
    expected_miles = 0.621371

    # Act
    result = km_to_miles(km)

    # Assert
    assert result == pytest.approx(expected_miles, 0.0001)

def test_km_to_miles_zero():
    # Arrange
    km = 0
    expected_miles = 0

    # Act
    result = km_to_miles(km)

    # Assert
    assert result == expected_miles

# Test para miles_to_km
def test_miles_to_km():
    # Arrange
    miles = 1
    expected_km = 1.60934

    # Act
    result = miles_to_km(miles)

    # Assert
    assert result == pytest.approx(expected_km, 0.0001)

def test_miles_to_km_zero():
    # Arrange
    miles = 0
    expected_km = 0

    # Act
    result = miles_to_km(miles)

    # Assert
    assert result == expected_km

# Test para kg_to_pounds
def test_kg_to_pounds():
    # Arrange
    kg = 1
    expected_pounds = 2.20462

    # Act
    result = kg_to_pounds(kg)

    # Assert
    assert result == pytest.approx(expected_pounds, 0.0001)

def test_kg_to_pounds_zero():
    # Arrange
    kg = 0
    expected_pounds = 0

    # Act
    result = kg_to_pounds(kg)

    # Assert
    assert result == expected_pounds

# Test para pounds_to_kg
def test_pounds_to_kg():
    # Arrange
    pounds = 1
    expected_kg = 0.453592

    # Act
    result = pounds_to_kg(pounds)

    # Assert
    assert result == pytest.approx(expected_kg, 0.0001)

def test_pounds_to_kg_zero():
    # Arrange
    pounds = 0
    expected_kg = 0

    # Act
    result = pounds_to_kg(pounds)

    # Assert
    assert result == expected_kg
