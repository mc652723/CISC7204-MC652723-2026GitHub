# CISC7204 Assignment 02 — Module 05 Final Project, Part 02
## Creating Dashboard with Plotly and Dash: Automobile Sales

**Student:** MC652723 XIE AN

### Files
| File | Purpose |
|---|---|
| `DV0101EN-Final-Assign-Part-2-Questions.py` | Completed dashboard (all TASK 2.1–2.6 implemented) |
| `automobile-sales.csv` | Historical automobile sales dataset (1980–2023) |
| `YearlyReportgraphs.png` | Yearly Statistics report, four charts (1980) |
| `RecessionReportgraphs.png` | Recession Period Statistics report, four charts |

### Run
```bash
python DV0101EN-Final-Assign-Part-2-Questions.py
# open http://127.0.0.1:8058/
```

### What the application does
- Two dropdowns: report type (Yearly / Recession) and year.
- The year dropdown is enabled only for the Yearly report; the first callback
  sets `disabled=True` for the Recession report.
- The Yearly report shows four charts in a 2 × 2 grid:
  1. average yearly automobile sales for the whole period;
  2. total monthly sales in the selected year;
  3. average vehicles sold by vehicle type;
  4. advertising-expenditure share by vehicle type.
- The Recession report shows four charts:
  1. average sales per year during recessions;
  2. average vehicles sold by type;
  3. advertising-expenditure share by type;
  4. effect of the unemployment rate on sales by vehicle type.

### Notes
- All task markers from the skeleton have been completed.
- `null` handling: the callback returns `None` until both inputs are usable.
