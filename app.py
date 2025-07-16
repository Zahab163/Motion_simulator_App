# app.py
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from motion import Body
from simulator import run_simulation
from utils import format_output, compute_kinematic_values

st.set_page_config(page_title="Motion Simulator", layout="centered")

st.title("Physics Motion Simulator")
st.markdown("Simulate the motion of a body using kinematics equations.")

# Sidebar: Simulation Inputs
st.sidebar.header("Simulation Parameters")
position = st.sidebar.number_input("Initial Position (m)", value=0.0)
velocity = st.sidebar.number_input("Initial Velocity (m/s)", value=10.0)
acceleration = st.sidebar.number_input("Acceleration (m/s²)", value=-9.8)
time_step = st.sidebar.slider("Time Step (s)", 0.01, 1.0, 0.1)
duration = st.sidebar.slider("Duration (s)", 1.0, 10.0, 2.0)

if st.sidebar.button("Run Simulation"):
    obj = Body(position, velocity, acceleration, duration)
    history = run_simulation(obj, time_step, duration)
 
    #extract data for graphing

    times = list(history.keys())
    positions = [state['position'] for state in history.values()]
    st.subheader("Position vs. Time Graph")

    fig,ax = plt.subplots()
    ax.plot(times, positions, color='blue', marker='o')
    ax.set_xlabel("Time(s)")
    ax.set_ylabel("Position(m)")
    ax.set_title("Motion Graph")

    st.pyplot(fig)

    st.subheader(" Simulation Results")
    for t, state in history.items():
        st.text(format_output(t, state))

    st.success("Simulation complete!")