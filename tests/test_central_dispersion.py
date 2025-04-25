"""Tests for CentralTendency and Dispersion."""

import fake_data as fd
import pytest
from ministats import CentralTendency, Dispersion


def test_mean() -> None:
    """Test mean calculation of a numeric list."""
    ct = CentralTendency(fd.valid_data)
    assert ct.mean() == pytest.approx(2.4)


def test_median() -> None:
    """Test median calculation of a numeric list."""
    ct = CentralTendency(fd.valid_data)
    assert ct.median() == 2


def test_mode_single() -> None:
    """Test mode calculation when there is a single mode."""
    ct = CentralTendency(fd.valid_data)
    assert ct.mode() == 2


def test_mode_multi() -> None:
    """Test mode calculation when multiple modes exist."""
    ct = CentralTendency(fd.multi_mode_data)
    assert sorted(ct.mode()) == [1, 2]


def test_variance_sample() -> None:
    """Test sample variance calculation."""
    d = Dispersion(fd.valid_data)
    assert d.variance(sample=True) == pytest.approx(1.3)


def test_variance_population() -> None:
    """Test population variance calculation."""
    d = Dispersion(fd.valid_data)
    assert d.variance(sample=False) == pytest.approx(1.04)


def test_std_dev_sample() -> None:
    """Test sample standard deviation calculation."""
    d = Dispersion(fd.valid_data)
    assert d.std_dev(sample=True) == pytest.approx(1.140175, rel=1e-5)


def test_range() -> None:
    """Test range calculation (max - min)."""
    d = Dispersion(fd.valid_data)
    assert d.range() == 3
