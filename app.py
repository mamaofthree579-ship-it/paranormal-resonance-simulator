import streamlit as st
import pandas as pd
import numpy as np
import requests
import folium
from streamlit_folium import st_folium
import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Universal Quantum Grid",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Project Unified Field: Organic Hardware & Piezo-Electric Arrays")
st.markdown("Mapping ancient fossilized fungal lightning rods, Nazca ceramic capacitor grids, and the planetary source code.")

# --- LIVE METRIC FETCH ENGINES ---
def get_lunar_gravitational_factor():
    now = datetime.datetime.now()
    diff = now - datetime.datetime(2026, 1, 1)
    days = diff.days + (diff.seconds / 86400.0)
    cycle_position = (days % 29.53) / 29.53
    illumination = 0.5 * (1 - np.cos(2 * np.pi * cycle_position))
    gravitational_pull = 1.0 + (0.35 * np.abs(np.sin(np.pi * cycle_position)))
    return round(illumination * 100, 1), round(gravitational_pull, 2)

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
    return 3.0

lunar_illumi, lunar_grav = get_lunar_gravitational_factor()
live_kp = get_live_celestial_kp()

# --- SIDEBAR CONTROL PANEL ---
st.sidebar.header("🌍 Universal Coordinate Focal Array")
mode = st.sidebar.selectbox(
    "Select Target Spatial Matrix",
    ["Nazca Lines (Ica, Peru)", "Skinwalker Ranch (Utah, USA)", "Stonehenge (Wiltshire, UK)"]
)

# --- NEW: PIEZO-ELECTRIC CERAMIC SHARD CAPACITORS ---
st.sidebar.header("🏺 Ground Capacitor Calibration")
shard_density = st.sidebar.slider(
    "Ceramic Shard Ground Density (Capacitance)",
    1.0, 10.0, 6.5,
    help="Models the dense layers of broken quartz-clay pottery used to lock a permanent electric charge into the ground grid."
)

# Set base parameters based on selection
if mode == "Nazca Lines (Ica, Peru)":
    user_lat, user_lon, target_name = -14.7396, -75.1300, "Nazca Lines Geometric Grid"
    water_cooling_efficiency = 1.0  # Ultra-arid desert basin, massive electrical charging retention
    fungal_lightning_rod_amplifier = 3.5  # High fossilized organic geoglyph footprint paths
    st.sidebar.caption("🏺 *Nazca Matrix Active: Silica desert floor acting as an immense open-air storage capacitor bank.*")
elif mode == "Skinwalker Ranch (Utah, USA)":
    user_lat, user_lon, target_name = 40.2592, -109.8885, "Skinwalker Ranch Core"
    water_cooling_efficiency = 1.2
    fungal_lightning_rod_amplifier = 2.5  # The Mesa petrified ridge line
else:
    user_lat, user_lon, target_name = 51.1789, -1.8262, "Stonehenge Stone Circle"
    water_cooling_efficiency = 2.1
    fungal_lightning_rod_amplifier = 1.5

st.sidebar.header("🧘 Operator Tuning Interface")
operator_profile = st.sidebar.selectbox(
    "Select Operator Methodology",
    ["Shamanic Coherence (Doctor/Scientist/Healer)", "Passive Observation", "Predatory Technology Siphoning"]
)

if operator_profile == "Shamanic Coherence (Doctor/Scientist/Healer)":
    coherence_multiplier = 5.0
    extraction_load = 1.0
    operator_harmonic_key = 1.618
else:
    coherence_multiplier = 1.0
    extraction_load = 2.0
    operator_harmonic_key = 1.0

# General Fields
st.sidebar.header("⚡ Local Field Fluctuations")
rf_signal_16 = st.sidebar.slider("1.6 GHz RF Base Power (dBm)", -110, -30, -95)

# --- THE HARDWARE NODES MATRIX ---
if "Nazca" in target_name:
    df_nodes = pd.DataFrame({
        "Location": ["The Hummingbird Geoglyph (Fossilized Antenna)", "The Condor Path Layer", "The Geometric Trapezoids"],
        "Latitude": [-14.6922, -14.6975, -14.7110],
        "Longitude": [-75.1488, -75.1250, -75.1520],
        "Base_Imprint": [9.9, 9.4, 9.0]
    })
else:
    df_nodes = pd.DataFrame({
        "Location": ["The Mesa Incline (Petrified Fungal Tree)", "The Triangle Zone", "Homestead 2"],
        "Latitude": [40.2612, 40.2589, 40.2595],
        "Longitude": [-109.8850, -109.8892, -109.8920],
        "Base_Imprint": [9.9, 9.8, 8.5]
    })

# --- CALCULATION ENGINE ---
processed_nodes = []
for idx, row in df_nodes.iterrows():
    rf_delta = max(0, (rf_signal_16 + 100) * 0.5)
    cosmic_flux = (live_kp * 0.6) * lunar_grav
    
    # Base catalyst incorporates our new ceramic capacitor charge variable
    catalyst_field = ((rf_delta + cosmic_flux) * (shard_density * 0.4)) / (water_cooling_efficiency * 0.5)
    
    # Combine ancient biological lightning rod geometry with Shamanic interface modifiers
    total_resonance = row["Base_Imprint"] * catalyst_field * fungal_lightning_rod_amplifier * (coherence_multiplier * 0.1) * operator_harmonic_key
    prob_manifestation = 1 / (1 + np.exp(-0.11 * (total_resonance - 25)))
    
    if prob_manifestation > 0.90:
        field_state = "QUANTUM COMMUNICATION: Active Shamanic Bio-Data Link Established"
    elif total_resonance > 25.0:
        field_state = "HARMONIC SHIFT: Grid Fully Electrified via Localized Capacitance"
    else:
        field_state = "EQUILIBRIUM: Stabilized Water-Cooled Processing"

    processed_nodes.append({
        "Location": row["Location"], "Lat": row["Latitude"], "Lon": row["Longitude"],
        "Resonance Output": round(total_resonance, 2), "Quantum Probability": f"{round(prob_manifestation * 100, 1)}%", "State": field_state
    })

df_results = pd.DataFrame(processed_nodes)

# --- USER INTERFACE LAYOUT ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Universal Energy Grid Analytics")
    st.markdown(f"**Target System:** `{target_name}` | **Operator Alignment:** `{operator_profile}`")
    
    st.dataframe(df_results[["Location", "Resonance Output", "Quantum Probability", "State"]], use_container_width=True)
    
    # RECONFIGURED ANCIENT ENGINEERING ANALYSIS
    st.info(f"""
    🔬 **Ancient Engineering Analysis Log:** 
    Your simulation of the `{target_name}` proves the ceramic capacitor thesis. Bumping up the **Ceramic Shard Ground Density** acts as a linear multiplier for the active grid. Because the hyper-arid Peruvian desert has a low water-cooling factor (`1.0`), it retains electrical charge flawlessly. The towering ancient fungal trees functioned as natural high-voltage lightning rods, driving immense currents directly into the ground matrix to power up the geoglyph antenna network.
    """)

with col2:
    st.subheader("🗺️ Geographic Quantum Grid Mapping")
    m = folium.Map(location=[user_lat, user_lon], zoom_start=13 if "Nazca" in target_name else 15, tiles="OpenTopomap")
    
    for idx, row in df_results.iterrows():
        marker_color = "red" if "QUANTUM" in row["State"] else "orange" if "HARMONIC" in row["State"] else "blue"
        
        folium.Marker(
            location=[row["Lat"], row["Lon"]],
            popup=f"<b>{row['Location']}</b><br>State: {row['State']}",
            icon=folium.Icon(color=marker_color, icon="grain" if "Fungal" in row["Location"] or "Antenna" in row["Location"] else "dashboard")
        ).add_to(m)
        
        folium.Circle(
            location=[row["Lat"], row["Lon"]],
            radius=400 if "Nazca" in target_name else 150,
            color="orange" if marker_color == "orange" else "green" if marker_color == "red" else "blue",
            fill=True,
            fill_opacity=0.12
        ).add_to(m)
        
    st_folium(m, width="100%", height=420, returned_objects=[])
