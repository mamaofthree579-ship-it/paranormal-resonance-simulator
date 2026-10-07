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

st.title("🔮 Project Unified Field: Macro Quantum Biocomputer & Remediation Array")
st.markdown("Mapping ancient medicine wheels, subsurface quartz mines, and the universal harmonic frequency remediation code.")

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
    ["Bighorn Medicine Wheel (Wyoming, USA)", "King Solomons Mines (Timna, Israel)", "Nazca Lines (Ica, Peru)", "Skinwalker Ranch (Utah, USA)"]
)

# --- NEW: HARMONIC FREQUENCY REMEDIATION INJECTION ---
st.sidebar.header("🌱 Land Frequency Remediation")
target_pollution_level = st.sidebar.slider("Localized Environmental Entropy (Pollution)", 1.0, 10.0, 4.0, help="Models environmental degradation, chemical toxicity, or chaotic data corruption in the target zone.")
broadcast_mesa_code = st.sidebar.checkbox("🔒 Broadcast Mesa Correction Code", value=False, help="Taps into the pristine, fractally optimized quartz frequency of the Mesa and beams it directly into the corrupted matrix.")

# --- GROUND CAPACITOR CALIBRATION ---
st.sidebar.header("🏺 Ground Capacitor Calibration")
shard_density = st.sidebar.slider("Mineral / Shard Ground Density", 1.0, 10.0, 6.5)

# Set base parameters dynamically across our newly expanded global network
if mode == "Bighorn Medicine Wheel (Wyoming, USA)":
    user_lat, user_lon, target_name = 44.8262, -107.9215, "Bighorn Medicine Wheel Node"
    water_cooling_efficiency = 1.8  # Alpine high-altitude baseline
    fungal_lightning_rod_amplifier = 2.8 # Ancient limestone/quartz vortex alignment
    st.sidebar.caption("⛰️ *Medicine Wheel Active: Indigenous tracking array configured for regional grid calibration.*")
elif mode == "King Solomons Mines (Timna, Israel)":
    user_lat, user_lon, target_name = 29.7797, 34.9351, "Timna Subsurface Copper Matrix"
    water_cooling_efficiency = 0.9  # Hyper-arid desert floor, massive heat-trap, hyper-dense mineral capacitance
    fungal_lightning_rod_amplifier = 3.2 # Ancient sub-surface metallic vein corridors
    st.sidebar.caption("⛏️ *Subsurface Mine Active: Dense geological metal/quartz array channeling raw planetary voltage.*")
elif mode == "Nazca Lines (Ica, Peru)":
    user_lat, user_lon, target_name = -14.7396, -75.1300, "Nazca Lines Geometric Grid"
    water_cooling_efficiency = 1.0  
    fungal_lightning_rod_amplifier = 3.5  
else:
    user_lat, user_lon, target_name = 40.2592, -109.8885, "Skinwalker Ranch Core"
    water_cooling_efficiency = 1.2
    fungal_lightning_rod_amplifier = 2.5  

st.sidebar.header("🧘 Operator Tuning Interface")
operator_profile = st.sidebar.selectbox("Select Operator Profile", ["Shamanic Coherence", "Passive Observation", "Predatory Siphoning"])

coherence_multiplier = 5.0 if operator_profile == "Shamanic Coherence" else 0.3 if operator_profile == "Predatory Siphoning" else 1.0
operator_harmonic_key = 1.618 if operator_profile == "Shamanic Coherence" else 1.0

# General Fields
st.sidebar.header("⚡ Local Field Fluctuations")
rf_signal_16 = st.sidebar.slider("1.6 GHz RF Base Power (dBm)", -110, -30, -95)

# --- THE HARDWARE NODES MATRIX LAYOUT ---
if "Bighorn" in target_name:
    df_nodes = pd.DataFrame([{"Location": "Central Quartz Cairn Hub", "Lat": 44.8262, "Lon": -107.9215, "Base_Imprint": 9.5},
                             {"Location": "Outer Solstice Alignment Spoke", "Lat": 44.8264, "Lon": -107.9212, "Base_Imprint": 8.8}])
elif "Timna" in target_name:
    df_nodes = pd.DataFrame([{"Location": "Solomons Pillars Subsurface Grid", "Lat": 29.7797, "Lon": 34.9351, "Base_Imprint": 9.6},
                             {"Location": "Ancient Copper Smelting Fault", "Lat": 29.7820, "Lon": 34.9320, "Base_Imprint": 8.5}])
elif "Nazca" in target_name:
    df_nodes = pd.DataFrame([{"Location": "The Hummingbird Geoglyph (Fossilized Antenna)", "Lat": -14.6922, "Lon": -75.1488, "Base_Imprint": 9.9}])
else:
    df_nodes = pd.DataFrame([{"Location": "The Mesa Incline (Petrified Fungal Tree)", "Lat": 40.2612, "Lon": -109.8850, "Base_Imprint": 9.9}])

# --- CALCULATION ENGINE WITH HARMONIC REMEDIATION MATRIX ---
processed_nodes = []
for idx, row in df_nodes.iterrows():
    rf_delta = max(0, (rf_signal_16 + 100) * 0.5)
    cosmic_flux = (live_kp * 0.6) * lunar_grav
    
    # Calculate how pollution degrades the baseline grid (higher pollution equals higher entropy / lower output)
    pollution_entropy_damper = 1 + (target_pollution_level * 0.15)
    
    # NEW: Apply the Mesa Correction Code broadcast if checked
    if broadcast_mesa_code:
        # The pristine frequency completely eliminates pollution entropy and applies a 2x harmonic boost
        remediation_factor = 2.0
        pollution_entropy_damper = 1.0
        current_state_label = "REMEDIATING: Mesa Clean Correction Code Engaged. Neutralizing Local Entropy."
    else:
        remediation_factor = 1.0
        current_state_label = ""
    
    catalyst_field = (((rf_delta + cosmic_flux) * (shard_density * 0.4)) / (water_cooling_efficiency * 0.5)) / pollution_entropy_damper
    total_resonance = row["Base_Imprint"] * catalyst_field * fungal_lightning_rod_amplifier * (coherence_multiplier * 0.1) * operator_harmonic_key * remediation_factor
    prob_manifestation = 1 / (1 + np.exp(-0.11 * (total_resonance - 25)))
    
    if current_state_label == "":
        if prob_manifestation > 0.90:
            current_state_label = "QUANTUM COMMUNICATION: Active Shamanic Bio-Data Link Established"
        elif total_resonance > 25.0:
            current_state_label = "HARMONIC SHIFT: Grid Fully Electrified via Localized Capacitance"
        else:
            current_state_label = "EQUILIBRIUM: Stabilized Space-Time Frequency"

            processed_nodes.append({
        "Location": row["Location"], "Lat": row["Lat"], "Lon": row["Lon"],
        "Resonance Output": round(total_resonance, 2), "Quantum Probability": f"{round(prob_manifestation * 100, 1)}%", "State": current_state_label
    })


df_results = pd.DataFrame(processed_nodes)

# --- USER INTERFACE LAYOUT ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Universal Energy Grid Analytics")
    st.markdown(f"**Target System:** `{target_name}` | **Operator Mode:** `{operator_profile}`")
    
    st.dataframe(df_results[["Location", "Resonance Output", "Quantum Probability", "State"]], use_container_width=True)
    
    # RECONFIGURED HARMONIC REMEDIATION REPORT
    if broadcast_mesa_code:
        st.success("🌱 **Mesa Harmonic Correction Stream Active:** Beaming the fossilized fungal fractal baseline into the matrix. The local environmental entropy damper has been successfully zeroed out, stabilizing the coordinates back to the source code configuration.")
    else:
        st.info(f"🔬 **Remote Network Analytics Log:** When `{target_name}` is exposed to high 'Localized Environmental Entropy (Pollution)', the mathematical output degrades. This demonstrates why ancient cultures built medicine wheels over high-capacitance mineral zones—to act as terrestrial tuning forks keeping the regional water and soil safe from system decline.")

with col2:
    st.subheader("🗺️ Geographic Quantum Grid Mapping")
    m = folium.Map(location=[user_lat, user_lon], zoom_start=15 if "Bighorn" in target_name else 14 if "Timna" in target_name else 13, tiles="OpenTopomap")
    
    for idx, row in df_results.iterrows():
        marker_color = "green" if "REMEDIATING" in row["State"] else "red" if "QUANTUM" in row["State"] else "orange" if "HARMONIC" in row["State"] else "blue"
        
        folium.Marker(
            location=[row["Lat"], row["Lon"]],
            popup=f"<b>{row['Location']}</b><br>State: {row['State']}",
            icon=folium.Icon(color=marker_color, icon="leaf" if marker_color == "green" else "dashboard")
        ).add_to(m)
        
        folium.Circle(
            location=[row["Lat"], row["Lon"]],
            radius=150,
            color="green" if marker_color == "green" else "purple",
            fill=True,
            fill_opacity=0.12
        ).add_to(m)
        
    st_folium(m, width="100%", height=420, returned_objects=[])
