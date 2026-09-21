import pickle
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="AeroPrice AI - Revenue Optimization Engine", layout="wide")

st.title("AeroPrice AI: Dynamic Airline Pricing Engine")
st.subheader("Simulating Real-Time Revenue Management Frameworks for   All Air-ways ")
st.markdown("---")


@st.cache_resource
def load_production_assets():
    base_dir = Path(__file__).resolve().parent
    with open(base_dir / "pricing_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open(base_dir / "encoders.pkl", "rb") as f:
        encoders = pickle.load(f)
    return model, encoders


try:
    model, encoders = load_production_assets()

    airline_options = list(encoders["airline"].classes_)
    flight_class_options = list(encoders["flight_class"].classes_)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(" Flight Operational Inputs")

        airline = st.selectbox("Select Active Airline", airline_options)
        flight_class = st.selectbox("Travel Cabin Class", flight_class_options)

        days_left = st.slider("Days Until Departure Proximity (Urgency)", 1, 50, 15)
        duration_min = st.number_input("Total Flight Duration (Minutes)", min_value=30, max_value=600, value=130)

        comp_fare = st.number_input(
            "Real-Time Competitor Fare Tracked (INR)",
            min_value=1000,
            max_value=90000,
            value=6000,
        )
        route_density = st.number_input(
            "Historical Route Density Traffic Volume",
            min_value=100,
            max_value=50000,
            value=15289,
        )

        urgency_index = 1 / (days_left + 0.1)
        is_direct_flight = st.radio("Is it a Non-Stop Direct Flight?", ["Yes", "No"])
        direct_indicator = 1 if is_direct_flight == "Yes" else 0

    with col2:
        st.subheader(" Revenue Management & Pricing Strategy Engine")
        st.write("Live automated dynamic pricing matrix based on inventory updates.")
        st.markdown("---")

        try:
            input_df = pd.DataFrame([
                {
                    "airline": airline,
                    "flight_class": flight_class,
                    "days_left": days_left,
                    "duration_min": duration_min,
                    "is_direct_flight": direct_indicator,
                    "competitor_fare": comp_fare,
                    "route_density_score": route_density,
                    "urgency_index": urgency_index,
                }
            ])

            for col in ["airline", "flight_class"]:
                if input_df[col].astype(str).isin(encoders[col].classes_).all():
                    input_df[col] = encoders[col].transform(input_df[col].astype(str))
                else:
                    raise ValueError(f"Unseen value in {col}: {input_df[col].iloc[0]}")

            base_prediction = model.predict(input_df)[0]
        except ValueError as exc:
            st.error(f"Model input mismatch: {exc}")
            st.stop()

        final_fare = base_prediction
        strategy_applied = "Standard Baseline Pricing Model Matrix"
        status_color = "info"

        if days_left <= 3:
            final_fare = max(base_prediction, comp_fare) * 1.15
            strategy_applied = " HIGH URGENCY SURCHARGE ACTIVE (+15% Revenue Generation on Premium Seats)"
            status_color = "error"
        elif days_left > 35:
            final_fare = base_prediction * 0.90
            strategy_applied = " PERISHABLE INVENTORY MARKDOWN ACTIVE (-10% Discount to Maximize Seat Load Factor)"
            status_color = "warning"

        st.metric(
            label=" Recommended Algorithmic Ticket Fare (Optimized)",
            value=f" {round(final_fare, 2)}",
            delta=f"{round(final_fare - base_prediction, 2)} Strategy Drift" if days_left <= 3 or days_left > 35 else None,
        )

        if days_left <= 3:
            st.error(f"**Applied Strategy Mode:** {strategy_applied}")
        elif days_left > 35:
            st.warning(f"**Applied Strategy Mode:** {strategy_applied}")
        else:
            st.info(f"**Applied Strategy Mode:** {strategy_applied}")

        st.markdown("###  Operational Base Reference")
        st.write(f"Predicted ML Raw Base Price: **₹ {round(base_prediction, 2)}**")

except FileNotFoundError:
    st.error("Model artifacts not found. Please verify that 'pricing_model.pkl' is inside this workspace folder.")
