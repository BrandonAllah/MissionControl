
import streamlit as st

# ======================================
# MISSION CONTROL
# Version 0.4 - Flight Simulation
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
    acceleration = 15          # meters/second^2

    # Velocity: v = v0 + at
    velocity = (
        initial_velocity
        + acceleration * time_seconds
    )

    # Altitude: y = y0 + v0*t + 0.5*a*t^2
    altitude = (
        initial_altitude
        + initial_velocity * time_seconds
        + 0.5 * acceleration * time_seconds ** 2
    )

    return altitude, velocity


# ======================================
# INITIALIZE SPACECRAFT DATA
# ======================================

# Session state keeps our values between
# Streamlit reruns.

if "altitude" not in st.session_state:
    st.session_state.altitude = 0
    st.session_state.velocity = 0
    st.session_state.fuel = 100
    st.session_state.mission_status = "Ready for Launch"

if "elapsed_time" not in st.session_state:
    st.session_state.elapsed_time = 0


# ======================================
# DASHBOARD HEADER
# ======================================

st.title("🚀 Mission Control")
st.write("Spacecraft Telemetry Dashboard")
st.caption("Version 0.4 | Flight Simulation")

st.divider()


# ======================================
# LAUNCH CONTROLS
# ======================================

st.subheader("Launch Controls")

col_launch, col_advance, col_reset = st.columns(3)

# Launch the spacecraft
with col_launch:
    if st.button("🚀 Launch Mission"):

        st.session_state.elapsed_time = 0
        st.session_state.altitude = 0
        st.session_state.velocity = 0
        st.session_state.fuel = 100
        st.session_state.mission_status = "In Flight"


# Advance the simulation by one second
with col_advance:
    if st.button("⏩ Advance 1 Second"):

        if st.session_state.mission_status == "In Flight":

            # Increase elapsed time
            st.session_state.elapsed_time += 1

            # Calculate new altitude and velocity
            altitude_m, velocity_ms = calculate_launch(
                st.session_state.elapsed_time
            )

            # Convert meters to kilometers
            st.session_state.altitude = round(
                altitude_m / 1000, 3
            )

            # Convert m/s to km/h
            st.session_state.velocity = round(
                velocity_ms * 3.6, 2
            )

        else:
            st.warning("Launch the spacecraft first!")


# Reset the spacecraft
with col_reset:
    if st.button("🔄 Reset Mission"):

        st.session_state.elapsed_time = 0
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
elapsed_time = st.session_state.elapsed_time
mission_status = st.session_state.mission_status

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Altitude",
        f"{altitude:.3f} km"
    )

with col2:
    st.metric(
        "Velocity",
        f"{velocity:.2f} km/h"
    )

with col3:
    st.metric(
        "Fuel Remaining",
        f"{fuel}%"
    )

with col4:
    st.metric(
        "Elapsed Time",
        f"{elapsed_time} sec"
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
