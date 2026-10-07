import streamlit as st
import pandas as pd
import numpy as np
import requests
import folium
from streamlit_folium import st_folium
import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Quantum Entanglement Grid",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Project Unified Field: Quantum Entanglement & Resonance Engine")
st.markdown("Plottable space, time, and frequency coordinates unified through shared cosmic particle origins.")

# --- LIVE METRIC FETCH ENGINES ---
def get_lunar_gravitational_factor():
    now = datetime.datetime.now()
    diff = now - datetime.datetime(2026, 1, 1)
    days = diff.days + (diff.seconds / 86400.0)
    cycle_position = (days % 29.53) / 29.53
    illumination = 0.5 * (1 - np.cos(2 * np.pi * cycle_position))
    gravitational_pull = 1.0 + (0.35 * np.abs(np.sin(np.pi * cycle_position)))
    return round(illumination * 100, 1), round(gravitational_pull, 2)

@st.cache_data(ttl=1800)
def get_localized_weather(lat, lon):
    url = f"https://open-meteo.com{lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"
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
    return {"temp_f": 65.0, "wind_mph": 5.0}

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

# --- SIDEBAR CONTROL MATRIX ---
st.sidebar.header("⏳ Spatial Focus Mode")
mode = st.sidebar.radio("Select Target Array", ["Skinwalker Ranch Focal Array", "Bermuda Triangle Anomalous Node", "Universal Coordinate Pivot"])

# --- TRIPLE QUANTUM WAVE FUNCTION INTERFACE ---
st.sidebar.header("🧠 Human Biological Frequency Key")
psi_brain = st.sidebar.slider("Cranial Brain Frequency (Hz)", 0.5, 40.0, 12.0)
psi_heart = st.sidebar.slider("Cardiac Heart Field (Hz)", 1.0, 10.0, 4.0)
psi_gut = st.sidebar.slider("Enteric Gut Oscillation (Hz)", 0.05, 0.5, 0.1)

st.sidebar.header("❤️ Emotional Coherence Vectors")
emotional_state = st.sidebar.selectbox(
    "Active Emotional Frequency State",
    ["Baseline Awareness", "Fear / Contraction / Distortion", "Authenticity / Alignment", "Unconditional Love (Maximum Amplitude)"]
)

if emotional_state == "Fear / Contraction / Distortion":
    coherence_multiplier = 0.35
elif emotional_state == "Authenticity / Alignment":
    coherence_multiplier = 2.0
elif emotional_state == "Unconditional Love (Maximum Amplitude)":
    coherence_multiplier = 4.5
else:
    coherence_multiplier = 1.0

# --- NEW: SOLFEGGIO HARMONIC SCALE TUNING ---
st.sidebar.header("🎵 Solfeggio Harmonic Tuning Scale")
solfeggio_scale = st.sidebar.selectbox(
    "Select Ambient Tuning Scale",
    ["Baseline Frequency (432 Hz - Cosmic Balance)", "Transformation Frequency (528 Hz - Core Matrix Repair)", "Awakening Intuition (741 Hz - Consciousness Shift)"]
)

if "528" in solfeggio_scale:
    harmonic_amplifier = 1.618  # Golden Ratio resonance modifier
    st.sidebar.caption("🎵 *528 Hz Active: Enhancing geometric source code compression pathways.*")
elif "741" in solfeggio_scale:
    harmonic_amplifier = 1.414  # Root 2 structural expansion modifier
else:
    harmonic_amplifier = 1.0    # Harmonic baseline stability

# Geographic Parameter Setting
if mode == "Universal Coordinate Pivot":
    st.sidebar.markdown("### 🗺️ Custom Coordinates Shift")
    user_lat = st.sidebar.number_input("Target Latitude", value=51.1789, format="%.4f")
    user_lon = st.sidebar.number_input("Target Longitude", value=-1.8262, format="%.4f")
    target_name = st.sidebar.text_input("Location Name Label", value="Stonehenge Celestial Shift")
    user_imprint = st.sidebar.slider("Assigned Historical Imprint Weight", 1.0, 10.0, 7.5)
    tectonic_strain = st.sidebar.slider("Localized Tectonic Strain Multiplier", 1.0, 3.0, 1.1)
elif mode == "Bermuda Triangle Anomalous Node":
    user_lat, user_lon, target_name, user_imprint = 25.0000, -71.0000, "Bermuda Triangle Center", 8.8
    tectonic_strain = 1.2
else:
    user_lat, user_lon, target_name, user_imprint = 40.2592, -109.8885, "Skinwalker Ranch", 9.5
    tectonic_strain = 2.4  

local_weather = get_localized_weather(user_lat, user_lon)

st.sidebar.header("⚡ Local Field Fluctuations")
rf_signal_16 = st.sidebar.slider("1.6 GHz RF Base Power (dBm)", -110, -30, -95)
gps_error_meters = st.sidebar.slider("GPS Deflection Matrix (Meters)", 0.0, 50.0, 1.2)
seismic_hz = st.sidebar.slider("Micro-Seismic Resonance (Hz)", 0.0, 100.0, 8.0)
radar_void_density = st.sidebar.slider("Stratum Void Density (S-Band)", 1.0, 10.0, 1.5)

# --- NODES & CALCULATIONS ---
@st.cache_data
def load_base_nodes(mode_select, lat, lon, name, imprint):
    if mode_select != "Skinwalker Ranch Focal Array":
        return pd.DataFrame({
            "Location": [name], "Latitude": [lat], "Longitude": [lon], "Historical_Imprint": [imprint],
            "Description": ["Target template coordinates active."]
        })
    else:
        return pd.DataFrame({
            "Location": ["The Triangle Zone", "Homestead 2", "The Mesa Incline", "Homestead 1"],
            "Latitude": [40.2589, 40.2595, 40.2612, 40.2575],
            "Longitude": [-109.8892, -109.8920, -109.8850, -109.8955],
            "Historical_Imprint": [9.8, 8.5, 9.2, 6.5],
            "Description": ["Epicenter nodes.", "Battery drain vectors.", "Subsurface radar reflectivity.", "Baseline structural metrics."]
        })

df_nodes = load_base_nodes(mode, user_lat, user_lon, target_name, user_imprint)

# Compute the Intersecting Biological Frequency Key
bio_frequency_key = ((psi_brain * 0.4) + (psi_heart * 1.5) + (psi_gut * 10.0)) * coherence_multiplier

processed_nodes = []
for idx, row in df_nodes.iterrows():
    rf_delta = max(0, (rf_signal_16 + 100) * 0.5)
    gps_delta = gps_error_meters * 0.7
    subsurface_catalyst = (seismic_hz * 0.1) * (radar_void_density * 1.3) * tectonic_strain
    celestial_catalyst = (live_kp * 0.8) * lunar_grav
    
    total_catalyst = rf_delta + gps_delta + subsurface_catalyst + celestial_catalyst
    
    # NEW QUANTUM FIELD LINKS: Incorporating Harmonic Tuning Scales and Shared Particle Origin Weights
    total_resonance = row["Historical_Imprint"] * total_catalyst * (bio_frequency_key * 0.05) * harmonic_amplifier
    
    prob_manifestation = 1 / (1 + np.exp(-0.11 * (total_resonance - 25)))
    
    if prob_manifestation > 0.90:
        status = "QUANTUM SYNERGY: Core Bio-Resonance Active"
    elif total_resonance > 30.0:
        status = "HARMONIC SHIFT: High-Frequency Energy Alignment"
    else:
        status = "EQUILIBRIUM: Stabilized Baseline Frequency"

    processed_nodes.append({
        "Location": row["Location"], "Lat": row["Latitude"], "Longitude": row["Longitude"],
        "Imprint Value": row["Historical_Imprint"], "Resonance Output": round(total_resonance, 2),
        "Anomalous Probability": f"{round(prob_manifestation * 100, 1)}%", "Field State": status
    })

df_results = pd.DataFrame(processed_nodes)

# --- USER INTERFACE LAYOUT ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Spatial Energy Grid Analytics")
    st.markdown(f"**Active Tracker Matrix:** `{target_name}`")
    st.markdown(f"**Calculated Biological Frequency Key (\(\Psi\)):** `{round(bio_frequency_key, 2)}`")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Live Solar Kp-Index", f"{live_kp} / 9.0")
    m2.metric("Lunar Illumination", f"{lunar_illumi}%")
    m3.metric("Lunar Tidal Factor", f"{lunar_grav}x")
    
    st.dataframe(df_results[["Location", "Imprint Value", "Resonance Output", "Anomalous Probability", "Field State"]], use_container_width=True)
    st.success("🔬 **Initial Particle Entanglement Enabled:** Systems are plotting geographic space and individual frequency vectors uniformly, demonstrating shared quantum origins across all physical coordinates.")

with col2:
    st.subheader("🗺️ Unified Tracking Overlay Map")
    m = folium.Map(location=[user_lat, user_lon], zoom_start=15 if mode == "Skinwalker Ranch Focal Array" else 6, tiles="OpenTopomap")
    
    for idx, row in df_results.iterrows():
        marker_color = "red" if "QUANTUM" in row["Field State"] else "orange" if "HARMONIC" in row["Field State"] else "blue"
        
        folium.Marker(
            location=[row["Lat"], row["Longitude"]],
            popup=f"<b>{row['Location']}</b><br>Resonance: {row['Resonance Output']}<br>State: {row['Field State']}",
            icon=folium.Icon(color=marker_color, icon="fullscreen")
        ).add_to(m)
        
        if mode == "Skinwalker Ranch Focal Array" and row["Location"] in ["The Triangle Zone", "The Mesa Incline"]:
            folium.Circle(
                location=[row["Lat"], row["Longitude"]],
                radius=150,
                color="crimson" if marker_color == "red" else "amber",
                fill=True,
                fill_opacity=0.15,
                popup="Active Bio-Resonating Perimeter"
            ).add_to(m)
        
    st_folium(m, width="100%", height=420, returned_objects=[])
