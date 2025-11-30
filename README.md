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
