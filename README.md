# ministats

A lightweight Python library for basic statistical functions used in data analysis. This library provides an object-oriented approach to statistical calculations with built-in data validation and visualization capabilities.

## Features

- **Central Tendency Measures**
  - Mean
  - Median
  - Mode

- **Dispersion Statistics**
  - Variance (sample and population)
  - Standard deviation
  - Range

- **Correlation Analysis**
  - Covariance
  - Pearson correlation coefficient

- **Data Visualization**
  - Histograms
  - Scatter plots

- **Built-in Data Validation**
  - Input type checking
  - Empty list validation
  - List length validation for correlation analysis

## Installation

```bash
pip install -r requirements.txt
```

## Usage Examples

### Basic Statistical Calculations

```python
from src.ministats import CentralTendency, Dispersion

# Sample data
data = [1, 2, 2, 3, 4, 5, 5]

# Central tendency calculations
ct = CentralTendency(data)
print(f"Mean: {ct.mean()}")
print(f"Median: {ct.median()}")
print(f"Mode: {ct.mode()}")

# Dispersion calculations
disp = Dispersion(data)
print(f"Variance (sample): {disp.variance()}")
print(f"Standard Deviation: {disp.std_dev()}")
print(f"Range: {disp.range()}")
```

### Correlation Analysis

```python
from src.ministats import Correlation

# Two datasets
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

# Create correlation object
corr = Correlation(x, y)
print(f"Covariance: {corr.covariance()}")
print(f"Correlation: {corr.correlation()}")
```

### Data Visualization

```python
from src.ministats import Visualizer

# Create visualizations
Visualizer.plot_histogram(data, bins=10)
Visualizer.plot_scatter(x, y)
```

## Dependencies

- numpy
- matplotlib

## Project Structure

```
ministats/
├── src/
│   └── ministats.py    # Main implementation file
├── requirements.txt    # Project dependencies
└── README.md          # Documentation
```

## Classes Overview

### Validator
- Static methods for input validation
- Checks for numeric lists and equal length lists

### CentralTendency
- Calculates mean, median, and mode
- Handles single mode and multiple modes cases

### Dispersion
- Provides variance, standard deviation, and range calculations
- Supports both sample and population variance

### Correlation
- Implements covariance and Pearson correlation
- Includes validation for paired data analysis

### Visualizer
- Creates histograms and scatter plots
- Uses matplotlib for visualization

## Version

Current version: 0.2.0

## Contributing

Feel free to submit issues and enhancement requests!
