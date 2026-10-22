# CISC7204 Assignment 02 — Module 05 Practice Project, Part 02
## Creating Dashboards: Australia Wildfire

**Student:** MC652723 XIE AN

### Files
| File | Purpose |
|---|---|
| `Dash_wildfire.py` | Interactive wildfire dashboard |
| `Historical_Wildfires.csv` | Historical wildfire data for Australia |
| `screenshot_wildfire_NSW_2005.png` | Default view: New South Wales, 2005 |
| `screenshot_wildfire_queensland_2005.png` | Queensland, 2005 (radio-item callback verified) |

### Run
```bash
python Dash_wildfire.py
# open http://127.0.0.1:8057/
```

### What the application does
- Radio items select one of the seven Australian regions (NSW, NT, QL, SA, TA, VI, WA).
- A dropdown selects a year from the dataset (2005–2020; default 2005).
- One callback filters the data and returns two charts:
  - a pie chart of monthly average estimated fire area;
  - a bar chart of monthly average pixel count for presumed vegetation fires.
- Months are placed in calendar order, so the bar chart reads January → December.
