# CISC7204 Assignment 02 — Module 04 Lab 02
## Dash Basics: HTML and Core Components

**Student:** MC652723 XIE AN

### Files
| File | Purpose |
|---|---|
| `dash_basics.py` | Main lab application: title, description and a Plotly pie chart of distance-group share |
| `dash_basics_practice.py` | Practice task: title changed to “Airline On-time Performance Dashboard”, font size 50 |
| `airline_data.csv` | Airline Reporting Carrier On-Time Performance sample used by both scripts |
| `screenshot_dash_basics.png` | Running application (task 3–6) |
| `screenshot_dash_basics_practice.png` | Running application after the practice task |

### Run
```bash
python dash_basics.py
# open http://127.0.0.1:8051/
```
The script reads `airline_data.csv` from the same folder and falls back to the
course S3 URL if the file is missing.

### What the application does
- Reads the airline on-time performance data.
- Samples 500 flights with `random_state=42`.
- Draws the proportion of flights in each distance group (250-mile intervals) as a pie chart.
- Places the title (`html.H1`), description (`html.P`) and chart (`dcc.Graph`) in a single layout.
