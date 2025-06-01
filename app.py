import streamlit as st
import pandas as pd

# Load pricing database
@st.cache_data
def load_pricing_data():
    return pd.read_excel("Pricing Database.xlsx", sheet_name="Pricing database")

# Load calculator formula sheet for future expansion
@st.cache_data
def load_calculator_template():
    return pd.read_excel("Pricing Calculator Formula - test.xlsx", sheet_name="Solar + Batt Pricing", header=None)

# App title
st.title("🔋 Polygon Energy - Solar + Battery System Pricing Calculator")

# Load data
pricing_df = load_pricing_data()

# Get dropdown options
panel_options = pricing_df[pricing_df['Type'] == 'Panel']['Model'].tolist()
inverter_options = pricing_df[pricing_df['Type'] == 'Inverter']['Model'].tolist()
battery_options = pricing_df[pricing_df['Type'] == 'Battery']['Model'].tolist()

# User Inputs
st.header("🧩 Select Your System Components")
selected_panel = st.selectbox("🔆 Solar Panel", panel_options)
selected_inverter = st.selectbox("⚡ Inverter", inverter_options)
selected_battery = st.selectbox("🔋 Battery", battery_options)
num_panels = st.number_input("🧮 Number of Panels", min_value=1, max_value=100, value=10)
num_batteries = st.number_input("🔢 Number of Batteries", min_value=0, max_value=20, value=1)

# Lookup prices
panel_price = pricing_df.loc[pricing_df['Model'] == selected_panel, 'Unit Price'].values[0]
inverter_price = pricing_df.loc[pricing_df['Model'] == selected_inverter, 'Unit Price'].values[0]
battery_price = pricing_df.loc[pricing_df['Model'] == selected_battery, 'Unit Price'].values[0]

# Basic system price calculation
total_panel_cost = panel_price * num_panels
total_battery_cost = battery_price * num_batteries
total_cost = total_panel_cost + inverter_price + total_battery_cost

# Output
st.header("💰 Estimated System Price (in $AUD)")
st.markdown(f"""
- **Solar Panels Cost:** $ {total_panel_cost:,.2f}  
- **Inverter Cost:** $ {inverter_price:,.2f}  
- **Battery Cost:** $ {total_battery_cost:,.2f}  
---
### ✅ **Total Estimated Price: $ {total_cost:,.2f}**
""")

st.caption("Note: All prices shown are in AUD ($). This calculator uses basic logic and can be expanded to include detailed formulas.")
