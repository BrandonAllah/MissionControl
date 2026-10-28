
import streamlit as st

# ======================================
# MISSION CONTROL
# Version 0.3 - Physics-Based Launch
# ======================================

# Configure the application
st.set_page_config(
    page_title="Mission Control",
    page_icon="🚀",
    layout="wide"
)

# ======================================
# PHYSICS SIMULATION
# ======================================

def calculate_launch(time_seconds):
    """
    Calculate rocket altitude and velocity
    using constant acceleration equations.
    """

    initial_velocity = 0       # meters/second
    initial_altitude = 0       # meters
    acceleration = 15         # meters/second^2

    # Velocity equation: v = v0 + at
    velocity = (
        initial_velocity
        + acceleration * time_seconds
    )

    # Position equation: y = y0 + v0*t + 0.5*a*t^2
    altitude = (
        initial_altitude
        + initial_velocity * time_seconds
        + 0.5 * acceleration * time_seconds ** 2
    )

    return altitude, velocity


# ======================================
# INITIALIZE SPACECRAFT DATA
# ======================================

if "altitude" not in st.session_state:
    st.session_state.altitude = 0
    st.session_state.velocity = 0
    st.session_state.fuel = 100
    st.session_state.mission_status = "Ready for Launch"


# ======================================
# DASHBOARD HEADER
# ======================================

st.title("🚀 Mission Control")
st.write("Spacecraft Telemetry Dashboard")
st.caption("Version 0.3 | Physics-Based Launch Simulation")

st.divider()


# ======================================
# LAUNCH CONTROLS
# ======================================

st.subheader("Launch Controls")

# Choose how long the rocket accelerates
time_seconds = st.slider(
    "Simulation Time (seconds)",
    min_value=0,
    max_value=60,
    value=10,
    step=1
)

col_launch, col_reset = st.columns(2)

with col_launch:
    if st.button("🚀 Launch Mission"):

        # Calculate altitude and velocity
        altitude_m, velocity_ms = calculate_launch(
            time_seconds
        )

        # Convert meters to kilometers
        st.session_state.altitude = round(
            altitude_m / 1000, 2
        )

        # Convert m/s to km/h
        st.session_state.velocity = round(
            velocity_ms * 3.6, 2
        )

        # Placeholder fuel consumption
        st.session_state.fuel = 95

        st.session_state.mission_status = "In Flight"

with col_reset:
    if st.button("🔄 Reset Mission"):

        st.session_state.altitude = 0
        st.session_state.velocity = 0
        st.session_state.fuel = 100
        st.session_state.mission_status = "Ready for Launch"

st.divider()


# ======================================
# SPACECRAFT TELEMETRY
# ======================================

st.subheader("Spacecraft Telemetry")

altitude = st.session_state.altitude
velocity = st.session_state.velocity
fuel = st.session_state.fuel
mission_status = st.session_state.mission_status

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Altitude",
        f"{altitude} km"
    )

with col2:
    st.metric(
        "Velocity",
        f"{velocity} km/h"
    )

with col3:
    st.metric(
        "Fuel Remaining",
        f"{fuel}%"
    )

st.divider()


# ======================================
# MISSION STATUS
# ======================================

st.subheader("Mission Status")

if mission_status == "Ready for Launch":
    st.info("🟢 Ready for Launch")

elif mission_status == "In Flight":
    st.success("🚀 Spacecraft In Flight")

else:
    st.warning(mission_status)


# ======================================
# SIMULATION INFORMATION
# ======================================

st.divider()

st.subheader("Simulation Information")

st.write("**Net Acceleration:** 15 m/s²")
st.write("**Initial Velocity:** 0 m/s")
st.write("**Initial Altitude:** 0 meters")

st.caption(
    "This simulation uses constant net acceleration. "
    "It does not yet model changing gravity, "
    "rocket mass, atmospheric drag, or realistic fuel usage."
)
