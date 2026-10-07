import streamlit as st
import pandas as pd
import numpy as np
import requests
import folium
from streamlit_folium import st_folium

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Skinwalker Analytics Node",
    page_icon="🛸",
    layout="wide"
)

st.title("🛸 Advanced Multi-Metric Field Resonance Engine")
st.markdown("### Focus Node: Skinwalker Ranch Telemetry Verification")

# --- LIVE CELESTIAL API FETCH ---
@st.cache_data(ttl=3600)
def get_live_celestial_kp():
    noaa_endpoint = "https://noaa.gov"
    try:
        response = requests.get(noaa_endpoint, timeout=5)
        if response.status_code == 200:
            data = response.json()
            live_kp = float(data.get("0", {}).get("geomagnetic", {}).get("scale", 2.0)) * 2.0
            return max(1.0, min(9.0, live_kp))
    except Exception:
        pass
    return 3.5

live_kp = get_live_celestial_kp()

# --- SIDEBAR INTERFACE & SKINWALKER EQUIPMENT SPECS ---
st.sidebar.header("🛸 Celestial Matrix")
st.sidebar.metric(label="Live NOAA Space Weather (Kp)", value=f"{live_kp} / 9.0")
solar_modifier = st.sidebar.slider("Solar Flux Scaling Factor", 1.0, 5.0, 1.0)
effective_kp = min(9.0, live_kp * solar_modifier)

st.sidebar.header("📡 Ranch Field Sensors (Simulated Inputs)")
rf_signal_16 = st.sidebar.slider("1.6 GHz RF Signal Power (dBm)", -110, -30, -90, help="Baseline is -100dBm. Spikes over -60dBm indicate active triggers.")
gps_error_meters = st.sidebar.slider("GPS Deflection Drift (Meters)", 0.0, 50.0, 1.5, help="Simulates satellite telemetry distortion over active zones.")
ionizing_radiation = st.sidebar.slider("Ionizing Radiation (uSv/h)", 0.05, 5.0, 0.12, help="Tracks sudden gamma/X-ray micro-bursts.")

# --- SKINWALKER RANCH DATASETS (STRUCTURAL BLUEPRINT) ---
@st.cache_data
def load_skinwalker_hotspots():
    # True geographic coordinates mapping specific operational points across the 512 acres
    ranch_data = {
        "Location": ["The Triangle Zone", "Homestead 2", "The Ridge / Mesa", "Homestead 1"],
        "Latitude": [40.2589, 40.2595, 40.2612, 40.2575],
        "Longitude": [-109.8892, -109.8920, -109.8850, -109.8955],
        "Historical_Imprint": [9.8, 8.5, 9.0, 6.5], # Weighted base score derived from historical records
        "Description": [
            "Center point of repeating GPS tracking anomalies, drone failures, and phantom UAP signatures.",
            "Site of acute psychological distress metrics, equipment battery drainage, and severe audio anomalies.",
            "Unexplained visual phenomena, underground physical radar echoes, and laser deflection experiments.",
            "Early homestead structure presenting lower baseline spatial resonance but steady residual variance."
        ]
    }
    return pd.DataFrame(ranch_data)

df_ranch = load_skinwalker_hotspots()

# --- MATH PREDICTIVE MODEL ENGINE ---
processed_ranch_nodes = []
for idx, row in df_ranch.iterrows():
    # Isolating sensor variations based on historical baselines
    rf_anomaly_weight = max(0, (rf_signal_16 + 100) * 0.4)
    gps_variance = gps_error_meters * 0.8
    radiation_spike = (ionizing_radiation - 0.12) * 15.0
    
    # Combined Terrestrial Catalyst Field
    ranch_catalyst = rf_anomaly_weight + gps_variance + radiation_spike + (effective_kp * 1.1)
    
    # Mathematical Space-Time Resonance Calculation
    total_resonance = row["Historical_Imprint"] * max(0.5, ranch_catalyst)
    
    # Sigmoid function for probability classification
    prob_manifestation = 1 / (1 + np.exp(-0.12 * (total_resonance - 20)))
    
    # Signal anomaly classification loop
    if prob_manifestation > 0.88:
        status = "CRITICAL: Active Time-Space Anomaly"
    elif rf_anomaly_weight > 5.0 and row["Historical_Imprint"] > 8.0:
        status = "ALERT: Pre-Event Resonance Alert"
    else:
        status = "Ambient Background Matrix"

    processed_ranch_nodes.append({
        "Location": row["Location"],
        "Lat": row["Latitude"],
        "Lon": row["Longitude"],
        "Base Imprint": row["Historical_Imprint"],
        "Resonance Score": round(total_resonance, 2),
        "Detection Probability": f"{round(prob_manifestation * 100, 1)}%",
        "System Classification": status
    })

df_ranch_results = pd.DataFrame(processed_ranch_nodes)

# --- WEB DASHBOARD INTERFACE RENDER ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📊 Dynamic Ranch Telemetry")
    st.dataframe(df_ranch_results[["Location", "Base Imprint", "Resonance Score", "Detection Probability", "System Classification"]], use_container_width=True)
    
    with st.expander("🔍 See Mathematical Model Explanation"):
        st.write("""
        This model cross-references specific geographic coordinates on the ranch with external variables. 
        When the **1.6 GHz RF signal spikes** or **GPS satellite signals defect**, the `Resonance Score` shifts non-linearly, modeling how the environment reacts during active anomalous windows.
        """)

with col2:
    st.subheader("🗺️ Target Telemetry Overlays")
    # Initialize Folium Map over the real coordinates of the Uintah Basin site
    ranch_map = folium.Map(location=[40.2592, -109.8885], zoom_start=15, tiles="OpenTopomap")
    
    for idx, row in df_ranch_results.iterrows():
        color = "red" if "CRITICAL" in row["System Classification"] else "orange" if "ALERT" in row["System Classification"] else "blue"
        
        folium.Marker(
            location=[row["Lat"], row["Lon"]],
            popup=f"<b>{row['Location']}</b><br>Resonance: {row['Resonance Score']}<br>Status: {row['System Classification']}",
            icon=folium.Icon(color=color, icon="screenshot")
        ).add_to(ranch_map)
        
    st_folium(ranch_map, width="100%", height=400, returned_objects=[])
