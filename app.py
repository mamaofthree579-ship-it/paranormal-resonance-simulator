import streamlit as st
import pandas as pd
import numpy as np
import requests
import folium
from streamlit_folium import st_folium
import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Quantum Grid Intelligence",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Project Unified Field: Remote Verification & Ionization Engine")
st.markdown("Mapping historical data path trajectories, atmospheric ionization risks, and human neuroplasticity alterations remotely.")

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

# --- SIDEBAR CONTROL MATRIX ---
st.sidebar.header("⏳ Historical Data Path Trajectories")
# Scoring the time movement vectors of the Uintah Basin particles
historical_layer = st.sidebar.selectbox(
    "Select Active Historical Timeline Data Path",
    ["Pre-Columbian / Ancient Native American Layer", "1950s Deep Uranium & Atomic Excavation Era", "Modern Corporate / Military Aerospace Interception"]
)

if historical_layer == "Pre-Columbian / Ancient Native American Layer":
    time_trajectory_modifier = 2.8  # Deep, baseline high-coherence residual storage
    st.sidebar.caption("📜 *Data Path: High residual resonance linked to historical skinwalker/curse footprints.*")
elif historical_layer == "1950s Deep Uranium & Atomic Excavation Era":
    time_trajectory_modifier = 3.5  # Disruptive sub-surface atomic fracturing profiles
    st.sidebar.caption("☢️ *Data Path: Subsurface structural fragmentation. High affinity for ionized air generation.*")
else:
    time_trajectory_modifier = 2.0  # High-frequency technological interaction layers

# --- NEW: ONLINE DIGITIZED EXPERIENCE DATALOGGER ---
st.sidebar.header("🌐 Crowd-Sourced Human Experience Input")
online_incident_density = st.sidebar.slider(
    "Digitized Online Incident Density Index", 
    1.0, 10.0, 4.5,
    help="Integrates remote logs from online forums, MUFON, and public interview datasets regarding acute encounters."
)

st.sidebar.header("🧠 Human Neuroplasticity Integration")
emotional_state = st.sidebar.selectbox(
    "Observer Alignment Matrix",
    ["Unconditional Love (Phase Coherence)", "Authenticity / Alignment", "Fear / Panic (Neurological Overload)"]
)

if emotional_state == "Fear / Panic (Neurological Overload)":
    coherence_multiplier = 0.4
    st.sidebar.warning("⚡ WARNING: Incoherent neural mapping detected. High risk of neuroplasticity alteration (Bringing it home).")
elif emotional_state == "Authenticity / Alignment":
    coherence_multiplier = 2.0
else:
    coherence_multiplier = 4.5

# Field Fluctuation Baselines
st.sidebar.header("⚡ Local Field Fluctuations")
rf_signal_16 = st.sidebar.slider("1.6 GHz RF Base Power (dBm)", -110, -30, -95)
seismic_hz = st.sidebar.slider("Micro-Seismic Resonance (Hz)", 0.0, 100.0, 8.0)

# --- THE SKINWALKER CORE DATAMATRIX ---
df_nodes = pd.DataFrame({
    "Location": ["The Triangle Zone", "Homestead 2", "The Mesa Incline", "Homestead 1"],
    "Latitude": [40.2589, 40.2595, 40.2612, 40.2575],
    "Longitude": [-109.8892, -109.8920, -109.8850, -109.8955],
    "Base_Weight": [9.8, 8.5, 9.2, 6.5]
})

# --- SYSTEM CALCULATION ENGINE ---
processed_nodes = []
for idx, row in df_nodes.iterrows():
    rf_delta = max(0, (rf_signal_16 + 100) * 0.5)
    seismic_delta = seismic_hz * 0.2
    
    # Calculate automated Ionization Catalyst from local fields, data paths, and online encounter logs
    ionization_catalyst = rf_delta + seismic_delta + (live_kp * 0.5) + (online_incident_density * 1.5)
    
    # Incorporate time trajectory multipliers
    total_resonance = row["Base_Weight"] * ionization_catalyst * time_trajectory_modifier * (coherence_multiplier * 0.1)
    
    prob_manifestation = 1 / (1 + np.exp(-0.11 * (total_resonance - 30)))
    
    # Atmospheric Ionization Risk Levels (Replacing old military terms with exact bio-physics descriptors)
    if total_resonance > 65.0:
        safety_status = "CRITICAL IONIZATION: High Biological Exposure Hazard (Neurological Shift Risk)"
    elif total_resonance > 35.0:
        safety_status = "ELEVATED FIELD: Ambient Air Fluorescing (Potential Instrument Drift)"
    else:
        safety_status = "BALANCED EQUILIBRIUM: Baseline Quantum Grounding"

    processed_nodes.append({
        "Location": row["Location"], "Lat": row["Latitude"], "Longitude": row["Longitude"],
        "Output Resonance": round(total_resonance, 2),
        "Bio-Quantum Probability": f"{round(prob_manifestation * 100, 1)}%",
        "Atmospheric Safety State": safety_status
    })

df_results = pd.DataFrame(processed_nodes)

# --- USER INTERFACE LAYOUT ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Remote Anomaly Tracking Ledger")
    st.markdown(f"**Current Data Path Focus:** `{historical_layer}`")
    
    st.dataframe(df_results[["Location", "Output Resonance", "Bio-Quantum Probability", "Atmospheric Safety State"]], use_container_width=True)
    
    # SAFETY METRICS FOR FIELD IMPLEMENTATION
    st.error("""
    🔬 **Operational Safety Directive for Field Teams:** 
    When the tracking ledger shifts into 'CRITICAL IONIZATION', the grid is generating invisible high-frequency air shearing. Teams must cease kinetic rocket operations immediately to prevent permanent neuroplastic baseline distortion and acute radiation feedback.
    """)

with col2:
    st.subheader("🗺️ Geographic Ionization Perimeter Map")
    m = folium.Map(location=[40.2592, -109.8885], zoom_start=15, tiles="OpenTopomap")
    
    for idx, row in df_results.iterrows():
        marker_color = "red" if "CRITICAL" in row["Atmospheric Safety State"] else "orange" if "ELEVATED" in row["Atmospheric Safety State"] else "blue"
        
        folium.Marker(
            location=[row["Lat"], row["Longitude"]],
            popup=f"<b>{row['Location']}</b><br>State: {row['Atmospheric Safety State']}",
            icon=folium.Icon(color=marker_color, icon="flash")
        ).add_to(m)
        
        folium.Circle(
            location=[row["Lat"], row["Longitude"]],
            radius=160,
            color="purple" if marker_color == "red" else "blue",
            fill=True,
            fill_opacity=0.12,
            popup="Calculated Bio-Quantum Field Spread"
        ).add_to(m)
        
    st_folium(m, width="100%", height=420, returned_objects=[])
