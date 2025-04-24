"""ministats - A lightweight Python library for basic statistical functions.

This module combines all statistical functions into a single file for simplicity.
"""

import math
from collections import Counter
from typing import Union

import numpy as np

# Type alias for numeric lists
NumericList = list[Union[int, float]]


# Utility functions
def validate_numeric_list(data: NumericList) -> None:
    """Validate that input data is a non-empty list of numeric values.

    Args:
        data: List of numeric values to validate

    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If input list is empty
    """
    if not isinstance(data, (list, np.ndarray)):
        raise TypeError("Input must be a list or numpy array")

    if len(data) == 0:
        raise ValueError("Input list cannot be empty")

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements must be numeric")


def validate_equal_length(data1: NumericList, data2: NumericList) -> None:
    """Validate that two lists have equal length.

    Args:
        data1: First list
        data2: Second list

    Raises:
        ValueError: If lists have different lengths
    """
    if len(data1) != len(data2):
        raise ValueError("Input lists must have equal length")


# Central tendency measures
def mean(data: NumericList) -> float:
    """Calculate the arithmetic mean of a list of numbers.

    Args:
        data: List of numeric values

    Returns:
        float: Arithmetic mean of the input data

    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If input list is empty
    """
    validate_numeric_list(data)
    return sum(data) / len(data)


def median(data: NumericList) -> float:
    """Calculate the median of a list of numbers.

    Args:
        data: List of numeric values

    Returns:
        float: Median of the input data

    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If input list is empty
    """
    validate_numeric_list(data)
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]


def mode(data: NumericList) -> Union[float, list[float]]:
    """Calculate the mode(s) of a list of numbers.

    Args:
        data: List of numeric values
    Returns:
        float or List[float]: Mode(s) of the input data. If multiple modes exist,
                             returns a list of modes.

    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If input list is empty
    """
    validate_numeric_list(data)
    counts = Counter(data)
    max_count = max(counts.values())
    modes = [x for x, count in counts.items() if count == max_count]

    return modes[0] if len(modes) == 1 else modes


# Dispersion measures
def variance(data: NumericList, sample: bool = True) -> float:
    """Calculate the variance of a list of numbers.

    Args:
        data: List of numeric values
        sample: If True, calculates sample variance (n-1 denominator),
               if False, calculates population variance (n denominator)

    Returns:
        float: Variance of the input data

    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If input list is empty
    """
    validate_numeric_list(data)
    data_mean = mean(data)
    squared_diff_sum = sum((x - data_mean) ** 2 for x in data)
    n = len(data)

    return squared_diff_sum / (n - 1) if sample else squared_diff_sum / n


def std_dev(data: NumericList, sample: bool = True) -> float:
    """Calculate the standard deviation of a list of numbers.

    Args:
        data: List of numeric values
        sample: If True, calculates sample standard deviation,
               if False, calculates population standard deviation

    Returns:
        float: Standard deviation of the input data

    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If input list is empty
    """
    return math.sqrt(variance(data, sample))


def range_stat(data: NumericList) -> float:
    """Calculate the range (max - min) of a list of numbers.

    Args:
        data: List of numeric values

    Returns:
        float: Range of the input data

    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If input list is empty
    """
    validate_numeric_list(data)
    return max(data) - min(data)


# Correlation measures
def covariance(
    data1: NumericList, data2: NumericList, sample: bool = True
) -> float:
    """Calculate the covariance between two lists of numbers.

    Args:
        data1: First list of numeric values
        data2: Second list of numeric values
        sample: If True, calculates sample covariance (n-1 denominator),
               if False, calculates population covariance (n denominator)

    Returns:
        float: Covariance between the two datasets

    Raises:
        TypeError: If inputs are not lists or contain non-numeric values
        ValueError: If input lists are empty or have different lengths
    """
    validate_numeric_list(data1)
    validate_numeric_list(data2)
    validate_equal_length(data1, data2)

    mean1 = mean(data1)
    mean2 = mean(data2)
    n = len(data1)

    sum_product_diff = sum(
        (x - mean1) * (y - mean2) for x, y in zip(data1, data2)
    )
    return sum_product_diff / (n - 1) if sample else sum_product_diff / n


def correlation(data1: NumericList, data2: NumericList) -> float:
    """Calculate the Pearson correlation coefficient between two lists of numbers.

    Args:
        data1: First list of numeric values
        data2: Second list of numeric values

    Returns:
        float: Correlation coefficient between the two datasets

    Raises:
        TypeError: If inputs are not lists or contain non-numeric values
        ValueError: If input lists are empty or have different lengths
        ZeroDivisionError: If either dataset has zero standard deviation
    """
    validate_numeric_list(data1)
    validate_numeric_list(data2)
    validate_equal_length(data1, data2)

    n = len(data1)
    mean1, mean2 = mean(data1), mean(data2)

    # Calculate variances
    var1 = sum((x - mean1) ** 2 for x in data1) / (n - 1)
    var2 = sum((x - mean2) ** 2 for x in data2) / (n - 1)

    if var1 == 0 or var2 == 0:
        raise ZeroDivisionError(
            "Cannot calculate when one or both datasets have zero variance"
        )

    # Calculate correlation
    cov = covariance(data1, data2)
    return cov / (math.sqrt(var1) * math.sqrt(var2))


# Version information
__version__ = "0.1.0"
