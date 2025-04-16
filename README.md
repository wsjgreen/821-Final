# 821-Final
# ministats 📊

**ministats** is a lightweight Python library designed to implement basic 
statistical functions often used in data analysis and machine learning pipelines. 
It is intended as a simple, educational, and extendable tool to understand core 
statistics from the ground up.

---

## 🚧 Project Goal

Build a modular Python library that:
- Implements core statistical functions (e.g., mean, median, variance)
- Is testable with unit testing
- Includes clear documentation and usage examples
- Can be extended in the future with more advanced functionality

---

## 🧱 Software Architecture

**Modular Design** — The project is split into logical components:
- `central_tendency.py`: Mean, median, mode
- `dispersion.py`: Variance, standard deviation, range
- `correlation.py`: Covariance, correlation
- `utils.py`: Helper functions like data validation
- `tests/`: Unit tests for each module using `pytest`
- `examples/`: Jupyter notebooks or scripts demonstrating functionality

---

## 🧪 Dependencies

This library aims to use **only standard Python libraries** for learning purposes:
- Python ≥ 3.8
- `pytest` for testing (optional)
