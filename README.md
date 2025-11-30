# Assignment9
# COVID Test Ratios Calculator (No Imports)

This project provides a simple Python script to calculate the ratio of **positive to negative tests** for each state from a CSV dataset.  
It is designed to work **without external libraries** (no `pandas`, no `csv` module), making it lightweight and portable.

---

## Features
- Reads an input CSV file with columns: `state`, `positive`, `negative`
- Aggregates totals for each state across all rows
- Calculates:
  - **Positive/Negative ratio** (`positive ÷ negative`)
  - **Positive/Total ratio** (`positive ÷ (positive + negative)`)
- Handles missing or malformed values gracefully (non-numeric → treated as 0)
- Writes results to a new CSV file with deterministic state ordering

---

## Input Format
The input CSV must contain at least these columns:

```csv
state,positive,negative
Indiana,2000,8000
Ohio,1500,5000
Illinois,3000,10000
```

---

## Output Format
- The script produces a new CSV file with the following columns:

```csv
state,positive,negative,ratio_pos_over_neg,ratio_pos_over_total
Illinois,3000,10000,0.300000,0.230769
Indiana,2000,8000,0.250000,0.200000
Ohio,1500,5000,0.300000,0.230769
```

---
## Usage
1. Set input and output paths
At the top of the script, configure:

```python
INPUT = r"c:\Users\camjh\Downloads\extracted_files\usscv19d.csv"
OUTPUT = r"c:\Users\camjh\Downloads\extracted_files\state_ratios_no_imports.csv"
```
2. Run the script
From VS Code or terminal:

```bash
python your_script.py
```
3. Check the output
The file `state_ratios_no_imports.csv` will be created in the specified folder.

## Function Overview
```python
def calculate_and_write_ratios(input_path, output_path):
    """
    Reads a CSV file with columns: state, positive, negative
    Aggregates totals per state
    Calculates ratios
    Writes results to a new CSV file
    """
```
- Input: Path to CSV file with test data
- Output: New CSV file with per-state ratios

---

## Error Handling
- If the input file is missing or empty → prints an error message
- If required columns are missing → prints an error message
- If values are non-numeric → treated as
- Division by zero → ratio fields left blank

---
