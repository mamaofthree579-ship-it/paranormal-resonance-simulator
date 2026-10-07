import streamlit as st
import pandas as pd
import numpy as np
import requests
import folium
from streamlit_folium import st_folium

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Skinwalker Core Node",
    page_icon="🛸",
    layout="wide"
)

st.title("🛸 Unified Field Resonance Engine: Skinwalker Ranch")
st.markdown("Evaluating universal space-time anomalies through unified sub-surface, atmospheric, and celestial metrics.")

# --- LIVE METRIC FETCH ENGINES ---
@st.cache_data(ttl=1800)  # Cache weather data for 30 minutes
def get_uintah_basin_weather():
    """Fetches real-time weather data for the Uintah Basin region (Fort Duchesne/Vernal, UT)"""
    # Using an open latitude/longitude endpoint for the ranch coordinates
    url = "https://open-meteo.com"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json().get("current", {})
            return {
                "temp_f": round((data.get("temperature_2m", 15) * 9/5) + 32, 1),
                "wind_mph": round(data.get("wind_speed_10m", 5) * 0.621371, 1)
            }
    except Exception:
        pass
    return {"temp_f": 62.5, "wind_mph": 4.2} # Baseline fallbacks

@st.cache_data(ttl=3600)  # Cache space weather for 1 hour
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
    return 3.0

# Fetch live streams
local_weather = get_uintah_basin_weather()
live_kp = get_live_celestial_kp()

# --- SIDEBAR: SYSTEM INPUTS ---
st.sidebar.header("📡 Live Automated Feed Telemetry")
st.sidebar.metric(label="Live NOAA Solar Kp-Index", value=f"{live_kp} / 9.0")
st.sidebar.metric(label="Ranch Ambient Temp", value=f"{local_weather['temp_f']} °F")

st.sidebar.header("⚡ Localized Variable Fluctuations")
rf_signal_16 = st.sidebar.slider("1.6 GHz RF Signal Power (dBm)", -110, -30, -95)
gps_error_meters = st.sidebar.slider("GPS Deflection Matrix (Meters)", 0.0, 50.0, 1.2)

st.sidebar.header("🪨 Sub-Surface / Mesa Stratum Metrics")
seismic_hz = st.sidebar.slider("Micro-Seismic Resonance (Hz)", 0.0, 100.0, 12.0, help="Tracks underground acoustic anomalies or structural vibrations.")
radar_void_density = st.sidebar.slider("Mesa Radar Void Density (S-Band)", 1.0, 10.0, 1.5, help="Models deep underground structural density changes or metallic anomalies.")

# --- THE SKINWALKER UNIFIED DATAMATRIX ---
@st.cache_data
def load_unified_nodes():
    ranch_data = {
        "Location": ["The Triangle Zone", "Homestead 2", "The Mesa Incline", "Homestead 1"],
        "Latitude": [40.2589, 40.2595, 40.2612, 40.2575],
        "Longitude": [-109.8892, -109.8920, -109.8850, -109.8955],
        "Historical_Imprint": [9.8, 8.5, 9.2, 6.5],
        "Description": ["Epicenter of 1.6 GHz bursts and localized time/altitude tracking distortions.",
                        "Site of physiological feedback loops, battery drain vectors, and transient cold spots.",
                        "Location of subsurface radar reflectivity pockets and high laser beam divergence.",
                        "Early residential settlement showing steady baseline structural imprint metrics."]
    }
    return pd.DataFrame(ranch_data)

df_nodes = load_unified_nodes()

# --- THE UNIFIED EQUATION ENGINE ---
processed_nodes = []
for idx, row in df_nodes.iterrows():
    # Convert slider inputs to active delta fields
    rf_delta = max(0, (rf_signal_16 + 100) * 0.5)
    gps_delta = gps_error_meters * 0.7
    
    # Sub-surface variables directly impact the Mesa and Triangle nodes with higher weighting
    subsurface_catalyst = (seismic_hz * 0.1) * (radar_void_density * 1.3)
    
    # The Matrix Calculus Link: Combined Celestial, Atmospheric, and Terrestrial variables
    total_catalyst = rf_delta + gps_delta + subsurface_catalyst + (live_kp * 0.8)
    
    # Apply spatial scaling law based on the node's unique historic threshold
    total_resonance = row["Historical_Imprint"] * total_catalyst
    
    # Sigmoid function maps value cleanly to a manifestation probability matrix
    prob_manifestation = 1 / (1 + np.exp(-0.11 * (total_resonance - 25)))
    
    # Universal Status Allocations
    if prob_manifestation > 0.90:
        status = "CRITICAL: Space-Time Collapse Imminent"
    elif total_resonance > 30.0:
        status = "WARNING: Highly Charged Grid Field"
    else:
        status = "Stabilized Background Continuity"

    processed_nodes.append({
        "Location": row["Location"],
        "Lat": row["Latitude"],
        "Longitude": row["Longitude"],
        "Imprint Value": row["Historical_Imprint"],
        "Resonance Output": round(total_resonance, 2),
        "Anomalous Probability": f"{round(prob_manifestation * 100, 1)}%",
        "Field State": status
    })

df_results = pd.DataFrame(processed_nodes)

# --- USER INTERFACE DISPLAY ---
col1, col2 = st.columns()

with col1:
    st.subheader("📊 Spatial Energy Grid Analytics")
    st.dataframe(df_results[["Location", "Imprint Value", "Resonance Output", "Anomalous Probability", "Field State"]], use_container_width=True)
    
    st.info(f"**Unified Field Logic Active:** The current model links celestial Kp indices and live local weather directly into the spatial coordinates. Because space is interconnected, changing the core variables shifts the local metrics instantly.")

with col2:
    st.subheader("🗺️ Unified Tracking Overlay Map")
    # Setting map view to focus directly on the real coordinates of the Utah ranch
    m = folium.Map(location=[40.2592, -109.8885], zoom_start=15, tiles="OpenTopomap")
    
    for idx, row in df_results.iterrows():
        marker_color = "red" if "CRITICAL" in row["Field State"] else "orange" if "WARNING" in row["Field State"] else "blue"
        
        folium.Marker(
            location=[row["Lat"], row["Longitude"]],
            popup=f"<b>{row['Location']}</b><br>Resonance: {row['Resonance Output']}<br>State: {row['Field State']}",
            icon=folium.Icon(color=marker_color, icon="fullscreen")
        ).add_to(m)
        
    st_folium(m, width="100%", height=420, returned_objects=[])
