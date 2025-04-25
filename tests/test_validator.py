"""Tests for validator."""

import fake_data as fd
import pytest
from ministats import Validator


def test_validate_numeric_list_valid() -> None:
    """Test validation passes on a valid numeric list."""
    Validator.validate_numeric_list(fd.valid_data)


def test_validate_numeric_list_empty() -> None:
    """Test validation raises ValueError for an empty list."""
    with pytest.raises(ValueError):
        Validator.validate_numeric_list(fd.empty_data)


def test_validate_numeric_list_non_numeric() -> None:
    """Test validation raises TypeError for a list with non-numeric values."""
    with pytest.raises(TypeError):
        Validator.validate_numeric_list(fd.non_numeric_data)


def test_validate_equal_length_valid() -> None:
    """Test validation passes when lists have equal lengths."""
    Validator.validate_equal_length(fd.valid_data, fd.valid_data2)


def test_validate_equal_length_invalid() -> None:
    """Test validation raises ValueError when lists have unequal lengths."""
    with pytest.raises(ValueError):
        Validator.validate_equal_length(fd.valid_data, fd.unequal_data)
