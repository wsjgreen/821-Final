"""ministats - A lightweight Python library for basic statistical functions.

This module combines all statistical functions into a single file for
 simplicity.
"""

import math
from collections import Counter
from typing import Union

import numpy as np

# Type alias for numeric lists
NumericList = list[Union[int, float]]


class Validator:
    """Validation utility methods for statistical calculations."""

    @staticmethod
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

    @staticmethod
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


class CentralTendency:
    """Central tendency measures."""

    def __init__(self, data: NumericList):
        """Initialize a CentralTendency object with data."""
        Validator.validate_numeric_list(data)
        self.data = data

    def mean(self) -> float:
        """Calculate the arithmetic mean of a list of numbers.

        Args:
            data: List of numeric values.

        Returns:
            float: Arithmetic mean of the input data

        Raises:
            TypeError: If input is not a list or contains non-numeric values
            ValueError: If input list is empty
        """
        return sum(self.data) / len(self.data)

    def median(self) -> float:
        """Calculate the median of a list of numbers.

        Args:
            data: List of numeric values

        Returns:
            float: Median of the input data

        Raises:
            TypeError: If input is not a list or contains non-numeric values
            ValueError: If input list is empty
        """
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    def mode(self) -> Union[float, list[float]]:
        """Calculate the mode of a list of numbers.

        Args:
            data: List of numeric values

        Returns:
            float or List[float]: Mode(s) of the input data.
            If multiple modes exist,returns a list of modes.

        Raises:
            TypeError: If input is not a list or contains non-numeric values
            ValueError: If input list is empty
        """
        counts = Counter(self.data)
        max_count = max(counts.values())
        modes = [x for x, count in counts.items() if count == max_count]
        return modes[0] if len(modes) == 1 else modes


class Dispersion:
    """Dispersion measures."""

    def __init__(self, data: NumericList):
        """Initialize a Dispersion object with data."""
        Validator.validate_numeric_list(data)
        self.data = data

    def variance(self, sample: bool = True) -> float:
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
        data_mean = CentralTendency(self.data).mean()
        squared_diff = [(x - data_mean) ** 2 for x in self.data]
        n = len(self.data)
        return sum(squared_diff) / (n - 1 if sample else n)

    def std_dev(self, sample: bool = True) -> float:
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
        return math.sqrt(self.variance(sample))

    def range(self) -> float:
        """Calculate the range (max - min) of a list of numbers.

        Args:
            data: List of numeric values

        Returns:
            float: Range of the input data

        Raises:
            TypeError: If input is not a list or contains non-numeric values
            ValueError: If input list is empty
        """
        return max(self.data) - min(self.data)


class Correlation:
    """Correlation measures."""

    def __init__(self, data1: NumericList, data2: NumericList):
        """Initialize a Correlation object with data1 and data2."""
        Validator.validate_numeric_list(data1)
        Validator.validate_numeric_list(data2)
        Validator.validate_equal_length(data1, data2)
        self.data1 = data1
        self.data2 = data2

    def covariance(self, sample: bool = True) -> float:
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
        mean1 = CentralTendency(self.data1).mean()
        mean2 = CentralTendency(self.data2).mean()
        n = len(self.data1)
        diffs = [
            (x - mean1) * (y - mean2) for x, y in zip(self.data1, self.data2)
        ]
        return sum(diffs) / (n - 1 if sample else n)

    def correlation(self) -> float:
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
        """  # noqa: E501
        var1 = Dispersion(self.data1).variance()
        var2 = Dispersion(self.data2).variance()

        if var1 == 0 or var2 == 0:
            raise ZeroDivisionError(
                "Cannot calculate when one or both datasets have zero variance"
            )

        # Calculate correlation
        cov = self.covariance()
        return cov / (math.sqrt(var1) * math.sqrt(var2))


# Version information
__version__ = "0.2.0"
