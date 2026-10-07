import streamlit as st
import pandas as pd
import numpy as np
import requests
import folium
from streamlit_folium import st_folium

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Field Resonance Simulator",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Multi-Metric Space-Time Resonance Simulator")
st.markdown("Modeling the intersection of historical structural attachments, terrestrial shifts, and celestial energy.")

# --- LIVE CELESTIAL API FETCH ENGINE ---
@st.cache_data(ttl=3600)  # Cache data for 1 hour to prevent spamming NOAA
def get_live_celestial_kp():
    noaa_endpoint = "https://noaa.gov"
    try:
        response = requests.get(noaa_endpoint, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # Map the current active geomagnetic storm scale to a proxy Kp value
            live_kp = float(data.get("0", {}).get("geomagnetic", {}).get("scale", 2.0)) * 2.0
            return max(1.0, min(9.0, live_kp))
    except Exception:
        pass
    return 3.5  # Realistic baseline fallback if API is down

# Fetch live space weather
live_kp = get_live_celestial_kp()

# --- SIDEBAR INTERFACE ---
st.sidebar.header("🛸 Celestial Control Matrix")
st.sidebar.metric(label="Live NOAA Planetary K-Index (Kp)", value=f"{live_kp} / 9.0")

# Allow the user to override or simulate higher solar flare activity
solar_modifier = st.sidebar.slider("Simulate Solar Influx Multiplier", 1.0, 5.0, 1.0, step=0.1)
effective_kp = min(9.0, live_kp * solar_modifier)

st.sidebar.header("🏠 Terrestrial Environment Baseline")
simulated_emf = st.sidebar.slider("Ambient Baseline EMF (mG)", 0.5, 10.0, 2.0)
simulated_temp = st.sidebar.slider("Ambient Temperature Drop (°F)", 0.0, 15.0, 2.0)

# --- PUBLIC DATASET INTEGRATION ---
# Mocking the layout of the Kaggle Haunted Places dataset for rapid cloud deployment
@st.cache_data
def load_historical_data():
    mock_historical_data = {
        "Location": ["Moundsville Penitentiary", "Gettysburg Battlefield", "Amityville House", "Eastern State Penitentiary", "The Stanley Hotel"],
        "State": ["WV", "PA", "NY", "PA", "CO"],
        "Description": [
            "The old state penitentiary where a past warden was tragically obsessed with control. Violent events left a heavy imprint.",
            "Soldiers from the historical battlefield are reported seen repeating past march loops. High emotional residual energy.",
            "A family home where a sudden tragic event occurred. Subsequent owners report severe structural dread.",
            "Historic prison designed for solitary confinement. Inmates experienced severe isolation and emotional distress.",
            "A grand historic hotel that deeply captivated its original builder, creating a lasting structural impression."
        ],
        "Latitude": [39.9173, 39.8309, 40.6666, 39.9683, 40.3831],
        "Longitude": [-80.7431, -77.2311, -73.4149, -75.1727, -105.5189]
    }
    return pd.DataFrame(mock_historical_data)

df_places = load_historical_data()

# --- MATHEMATICAL NLP ENGINE ---
def score_historical_imprint(text):
    desc_lower = str(text).lower()
    base_charge = 2.0
    weights = {"obsessed": 2.5, "tragic": 2.0, "battlefield": 3.5, "violent": 3.0, "dread": 2.0, "isolation": 2.5}
    for word, weight in weights.items():
        if word in desc_lower:
            base_charge += weight
    return min(10.0, base_charge)

# Process equations
df_places["Attachment_Field"] = df_places["Description"].apply(score_historical_imprint)

# Calculate dynamic resonance metrics across rows
processed_results = []
for idx, row in df_places.iterrows():
    catalyst = (simulated_emf * 1.2) + (simulated_temp * 1.5) + (effective_kp * 0.8)
    total_resonance = row["Attachment_Field"] * catalyst
    manifestation_prob = 1 / (1 + np.exp(-0.15 * (total_resonance - 15)))
    
    processed_results.append({
        "Location": row["Location"],
        "Lat": row["Latitude"],
        "Lon": row["Longitude"],
        "Attachment": row["Attachment_Field"],
        "Resonance": round(total_resonance, 2),
        "Probability": f"{round(manifestation_prob * 100, 1)}%"
    })

df_results = pd.DataFrame(processed_results)

# --- MAIN DISPLAY LAYOUT ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📊 Current Telemetry Grid")
    st.dataframe(df_results[["Location", "Attachment", "Resonance", "Probability"]], use_container_width=True)

with col2:
    st.subheader("🗺️ Live Anomalous Radar Map")
    
    # Initialize Folium Map
    m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)
    
    for idx, row in df_results.iterrows():
        marker_color = "red" if row["Resonance"] > 25.0 else "orange" if row["Resonance"] > 15.0 else "green"
        
        popup_text = f"""
        <b>{row['Location']}</b><br>
        Attachment: {row['Attachment']}/10<br>
        Field Resonance: {row['Resonance']}<br>
        Manifestation Prob: {row['Probability']}
        """
        
        folium.Marker(
            location=[row["Lat"], row["Lon"]],
            popup=folium.Popup(popup_text, max_width=250),
            icon=folium.Icon(color=marker_color, icon="eye-open")
        ).add_to(m)
    
    # Render map back into Streamlit interface
    st_folium(m, width="100%", height=400, returned_objects=[])
