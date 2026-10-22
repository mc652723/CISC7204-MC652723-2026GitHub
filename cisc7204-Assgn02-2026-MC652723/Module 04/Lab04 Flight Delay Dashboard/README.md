# CISC7204 Assignment 02 — Module 04 Lab 04
## Flight Delay Time Statistics Dashboard

**Student:** MC652723 XIE AN

### Files
| File | Purpose |
|---|---|
| `flight_delay.py` | Main dashboard: five delay-type line charts for a selected year |
| `flight_details.py` | Practice task: title changed to “Flight Details Statistics Dashboard”, font size 35 |
| `airline_data.csv` | Airline Reporting Carrier On-Time Performance dataset |
| `screenshot_flight_delay.png` | Main dashboard for 2010 |
| `screenshot_flight_delay_2017.png` | Main dashboard after changing the year to 2017 |
| `screenshot_flight_details.png` | Practice dashboard |

### Run
```bash
python flight_delay.py   # http://127.0.0.1:8055/
python flight_details.py # http://127.0.0.1:8056/
```

### What the application does
- Builds a layout with a title, one year input and five graphs arranged in three segments.
- `compute_info()` filters by year and computes monthly averages of
  `CarrierDelay`, `WeatherDelay`, `NASDelay`, `SecurityDelay` and `LateAircraftDelay`
  for each reporting airline.
- One callback returns five `px.line` figures to the five `dcc.Graph` components.
- Charts are laid out two per row (each 50% wide) with the late-aircraft chart at 65% width.
