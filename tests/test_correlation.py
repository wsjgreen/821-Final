"""Tests for correlation."""

import fake_data as fd
import pytest
from ministats import Correlation


def test_covariance_sample() -> None:
    """Test sample covariance calculation between two datasets."""
    c = Correlation(fd.valid_data, fd.valid_data2)
    assert c.covariance(sample=True) == pytest.approx(2.6)


def test_correlation() -> None:
    """Test Pearson correlation coefficient between two datasets."""
    c = Correlation(fd.valid_data, fd.valid_data2)
    assert c.correlation() == pytest.approx(1.0)


def test_correlation_zero_variance() -> None:
    """Test correlation function raises Error with zero variance data."""
    with pytest.raises(ZeroDivisionError):
        Correlation(fd.constant_data, fd.constant_data).correlation()
