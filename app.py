import streamlit as st
import pandas as pd
import numpy as np
import requests
import folium
from streamlit_folium import st_folium
import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Unified Field Verification",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Project Unified Field: Experimental Verification Engine")
st.markdown("Validating space-time field distortions through active kinetic and RF excitation vectors.")

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

# --- NEW: ACTIVE FIELD EXPERIMENT DROP-DOWN ---
st.sidebar.header("🚀 Active Physical Experiments")
active_experiment = st.sidebar.selectbox(
    "Select Ranch Deployment Protocol",
    ["Passive Monitoring Only", "100-Drone Swarm Mapping", "Thermal Ionization Rocket Launch", "1,000-Drone Cluster Stress Test"]
)

# Initialize dynamic experiment modifiers
kinetic_shear_multiplier = 1.0
rf_saturation_factor = 0.0
ionization_vector = 0.0

if active_experiment == "100-Drone Swarm Mapping":
    rf_saturation_factor = 25.0
    st.sidebar.caption("💡 *Model Insight: Mid-level L-Band frequency noise floor saturation detected.*")
elif active_experiment == "Thermal Ionization Rocket Launch":
    ionization_vector = 45.0
    kinetic_shear_multiplier = 2.5
    st.sidebar.caption("💡 *Model Insight: Active vertical plasma corridor grounding subsurface piezo-electric strain.*")
elif active_experiment == "1,000-Drone Cluster Stress Test":
    rf_saturation_factor = 65.0
    ionization_vector = 15.0
    st.sidebar.caption("💡 *Model Insight: Critical GNSS request density. High probability of spatial coordinate refraction (spoofing).*")

# Load baseline profiles based on location selection
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

processed_nodes = []
for idx, row in df_nodes.iterrows():
    # Integrate passive sliders with active experimental excitation vectors
    rf_delta = max(0, (rf_signal_16 + 100) * 0.5) + rf_saturation_factor
    gps_delta = (gps_error_meters * 0.7) * kinetic_shear_multiplier
    
    subsurface_catalyst = (seismic_hz * 0.1) * (radar_void_density * 1.3) * tectonic_strain
    celestial_catalyst = (live_kp * 0.8) * lunar_grav
    
    # Combined Catalyst Equation compounding active ionization vectors
    total_catalyst = rf_delta + gps_delta + subsurface_catalyst + celestial_catalyst + ionization_vector
    total_resonance = row["Historical_Imprint"] * total_catalyst
    
    # Sigmoid function for field threshold processing
    prob_manifestation = 1 / (1 + np.exp(-0.11 * (total_resonance - 25)))
    
    # Determine alert triggers based on bubble boundaries
    if prob_manifestation > 0.90:
        status = "CRITICAL: Space-Time Core Disruption"
    elif total_resonance > 30.0:
        status = "WARNING: Highly Charged Grid Field"
    else:
        status = "Stabilized Background Continuity"

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
    st.markdown(f"**Active Tracker Matrix:** `{target_name}` | **Deployment Protocol:** `{active_experiment}`")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Live Solar Kp-Index", f"{live_kp} / 9.0")
    m2.metric("Lunar Illumination", f"{lunar_illumi}%")
    m3.metric("Lunar Tidal Factor", f"{lunar_grav}x")
    
    st.dataframe(df_results[["Location", "Imprint Value", "Resonance Output", "Anomalous Probability", "Field State"]], use_container_width=True)
    
    # NEW: VERIFICATION LOG DATA REPORT
    st.info(f"🔮 **Verification Insights:** When `{active_experiment}` is triggered on coordinates with an Imprint value above 9.0, the non-linear math maps an exponential surge. This mimics the real-world tool failures and UAP flashes witnessed during live deployments.")

with col2:
    st.subheader("🗺️ Unified Tracking Overlay Map (750ft Bubble Boundary Active)")
    m = folium.Map(location=[user_lat, user_lon], zoom_start=15 if mode == "Skinwalker Ranch Focal Array" else 6, tiles="OpenTopomap")
    
    for idx, row in df_results.iterrows():
        marker_color = "red" if "CRITICAL" in row["Field State"] else "orange" if "WARNING" in row["Field State"] else "blue"
        
        # Construct marker layout
        folium.Marker(
            location=[row["Lat"], row["Longitude"]],
            popup=f"<b>{row['Location']}</b><br>Resonance: {row['Resonance Output']}<br>State: {row['Field State']}",
            icon=folium.Icon(color=marker_color, icon="fullscreen")
        ).add_to(m)
        
        # NEW: BOUNDARY VISUALIZATION LAYER
        # Render a translucent 3D vertical bubble boundary radius around active anomalies
        if mode == "Skinwalker Ranch Focal Array" and row["Location"] in ["The Triangle Zone", "The Mesa Incline"]:
            folium.Circle(
                location=[row["Lat"], row["Longitude"]],
                radius=150, # 150-meter lateral radius mapping the core anomaly perimeter
                color="crimson" if marker_color == "red" else "amber",
                fill=True,
                fill_opacity=0.15,
                popup="Critical 750ft Vertical Bubble Perimeter"
            ).add_to(m)
        
    st_folium(m, width="100%", height=420, returned_objects=[])
