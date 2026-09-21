# AeroPrice AI

AeroPrice AI is a real-time airline fare optimization dashboard that combines machine learning with dynamic pricing strategy to recommend smarter ticket prices based on operational and market conditions.

## Project Overview

This project simulates a practical revenue-management workflow for airlines. It helps evaluate how fare recommendations should respond to:

- flight duration
- days left until departure
- airline selection
- cabin class
- competitor pricing
- route density
- direct versus connecting flight

The system uses a trained XGBoost regression model and applies pricing rules to generate a final fare recommendation in a live dashboard.

## Why This Project Matters

Airline pricing is a high-impact decision area where even small changes in fare strategy can influence:

- revenue per flight
- seat occupancy
- customer conversion
- pricing competitiveness

This project demonstrates how data-driven pricing logic can support smarter commercial decisions in a travel and aviation context.

## Business Use Case

The app is designed for a scenario where an airline or travel revenue team wants to:

- optimize ticket pricing in real time
- respond to urgency and demand pressure
- stay competitive against nearby fares
- balance revenue goals with load factor optimization

## Features

- Live fare prediction using a trained ML model
- Categorical handling for airline and cabin class using saved encoders
- Revenue strategy logic for urgency-based pricing
- Dynamic recommendation engine adapted to booking time sensitivity
- Interactive UI built with Streamlit
- Easy deployment from a local project folder

## Tech Stack

- Python
- Pandas
- NumPy
- scikit-learn
- XGBoost
- Streamlit
- Pickle model serialization

## Project Structure

- [app.py](app.py) — interactive Streamlit dashboard
- [load.ipynb](load.ipynb) — notebook for preprocessing, feature engineering, and model training
- [pricing_model.pkl](pricing_model.pkl) — trained XGBoost model
- [encoders.pkl](encoders.pkl) — saved label encoders for categorical variables
- [business.csv](business.csv) — business-class flight data
- [economy.csv](economy.csv) — economy-class flight data

## Model Logic

The workflow is built around three key layers:

1. Data preparation and feature engineering
   - flight duration
   - urgency index
   - direct flight flag
   - route density
   - competitor fare comparison

2. Machine learning prediction
   - model predicts a baseline fare based on historical patterns

3. Revenue strategy adjustment
   - if the flight is close to departure, a premium surcharge is applied
   - if the booking window is far away, a markdown discount is used
   - otherwise a standard fare is recommended

## Pricing Strategy

The system applies practical pricing behavior based on the number of days remaining:

- If days left <= 3:
  - apply urgency surcharge (+15%)
- Else if days left > 35:
  - apply markdown discount (-10%)
- Else:
  - keep standard pricing baseline

This mirrors real aviation pricing decisions where urgency and low-demand windows affect pricing policy.

## Running the Project

From the project folder, run:

```powershell
cd "D:\archive (14)\SENFEKNE"
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Then open the local URL displayed in the terminal, typically:

```text
http://localhost:8501
```

## Expected Outcome

When the app runs successfully, the user can input flight details and immediately receive:

- predicted market-based fare
- pricing strategy status
- optimized recommended ticket price
- business-friendly revenue recommendation

## Notes

- The app loads the trained model and encoder artifacts already stored in the project folder.
- The model and encoders must remain in sync to avoid label mismatch issues.
- If required files are missing, the app displays a clear error message instead of crashing.

## Project Impact

This project demonstrates:

- applied machine learning in a business scenario
- practical revenue optimization thinking
- dashboard-driven decision support
- clean integration of analytics and product experience

## Future Enhancements

Possible next steps include:

- adding real-time airline inventory tracking
- integrating demand forecasting models
- enhancing the dashboard with charts and business KPIs
- deploying the app to a cloud platform
- adding explainability for each fare recommendation

## License

This project is intended for educational and portfolio use.
