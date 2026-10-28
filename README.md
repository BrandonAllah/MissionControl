# 🚀 Mission Control

A NASA-inspired spacecraft telemetry dashboard built with Python and Streamlit.

## About the Project

Mission Control is a personal software engineering project that explores spacecraft simulation, physics, and interactive dashboard development.

The project currently simulates vertical rocket motion using constant-acceleration kinematic equations.

## Current Features

- Interactive spacecraft telemetry dashboard
- Launch and reset controls
- Adjustable simulation time
- Physics-based altitude and velocity calculations
- Mission status monitoring
- Simulated fuel indicator

## Technologies

- Python
- Streamlit
- Git and GitHub

## Physics Equations

Velocity:

`v = v₀ + at`

Vertical position:

`y = y₀ + v₀t + ½at²`

The current simulation assumes constant net acceleration and does not yet model realistic thrust, fuel consumption, atmospheric drag, or changing rocket mass.

## Running Locally

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the dependencies:

   `python -m pip install -r requirements.txt`

4. Launch the application:

   `python -m streamlit run app.py`

## Project Status

**Version 0.3 — In Development**

Future plans include live telemetry, trajectory graphs, gravitational forces, fuel consumption, and more advanced spacecraft simulations.

*This is an independent educational project and is not affiliated with NASA.*