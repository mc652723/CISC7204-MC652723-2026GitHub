# CISC7204 Assignment 02 — Module 04 Lab 03
## Add Interactivity: User Input and Callbacks

**Student:** MC652723 XIE AN

### Files
| File | Purpose |
|---|---|
| `dash_interactivity.py` | Main lab application: year input drives a monthly average arrival-delay line chart |
| `dash_interactivity_barplot.py` | Practice task: year input drives a bar chart of flights by destination state and reporting airline |
| `airline_data.csv` | Airline Reporting Carrier On-Time Performance dataset |
| `screenshot_interactivity_2010.png` | Main app with the default year 2010 |
| `screenshot_interactivity_2015.png` | Main app after changing the year to 2015 (callback verified) |
| `screenshot_barplot_2010.png` | Practice bar-chart application |

### Run
```bash
python dash_interactivity.py       # http://127.0.0.1:8053/
python dash_interactivity_barplot.py  # http://127.0.0.1:8054/
```

### What the application does
- Uses `dcc.Input(id='input-year')` as the only user input.
- The `@app.callback` filters the data for the selected year, groups by `Month`,
  and returns a new `go.Figure` to `dcc.Graph(id='line-plot')`.
- The practice version returns a stacked `px.bar` of flights by `DestState`
  split by `Reporting_Airline` to `bar-plot`.
