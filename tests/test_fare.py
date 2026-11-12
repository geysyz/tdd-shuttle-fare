import pytest
from fare import fare_cents


def test_short_trip_adult_pays_base_fare():
    # Arrange
    distance_km = 3
    # Act
    result = fare_cents(distance_km, "adult")
    # Assert
    assert result == 200

# Exactly 5 km for an adult costs 200 (a boundary: the edge of a rule is where bugs hide)
def test_exactly_5km_adult_pays_base_fare():
    # Arrange
    distance_km = 5
    # Act
    result = fare_cents(distance_km, "adult")
    # Assert
    assert result == 200

# 8 km for an adult costs 350
def test_more_than_5_km():
    # Arrange
    distance_km = 8
    # Act
    result = fare_cents(distance_km, "adult")
    # Assert
    assert result == 350

# 8 km for a student costs 175
def test_student_fare():
    # Arrange
    distance_km = 8
    # Act
    result = fare_cents(distance_km, "student")
    # Assert
    assert result == 175

# 20 km for a child costs 0
def test_child_discount():
    # Arrange
    distance_km = 20
    # Act
    result = fare_cents(distance_km, "child")
    # Assert
    assert result == 0

# A distance of −1 raises an error (pytest.raises(ValueError))
def test_negative_distance():
    # Arrange
    distance_km = -1
    # Act
    result = fare_cents(distance_km, "adult")
    # Assert
    assert result == pytest.raises(ValueError)

# An unknown rider type such as "pilot" raises an error
def test_invalid_rider():
    # Arrange
    distance_km = 20
    # Act
    result = fare_cents(distance_km, "pilot")
    # Assert
    assert result == 0