# Motion_simulator_App
It's a Python Project that simulates Motion of an object using Physic formulas.
##Motion Simulator
Simulate the motion of objects using 1D and 2D kinematics formulas, powered by Python, NumPy, and Streamlit. This interactive tool lets users input physical parameters and visualize motion over time.


## Folder Structure
motion_simulator/
├── main.py              # CLI simulation runner
├── app.py               # Streamlit interface
├── motion.py            # Body class & physics logic
├── simulator.py         # Runs time-step simulations
├── utils.py             # Helpers & formatting tools
├── data/
│   └── history.json     # Logs of past simulations
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation


python main.py
# 🚀 Motion Simulator App

The Motion Simulator App is an interactive tool built with **Python** and **Streamlit** that visualizes physics-based motion in real time. Users can input motion parameters, simulate movement, and view dynamic graphs representing velocity, displacement, and acceleration.


## 📸 Demo
  
Example:  
![App Screenshot](graph_placeholder.png)

---

## 🧠 Features

- 🎛 Real-time input of motion parameters (initial velocity, acceleration, time)
- 📈 Dynamic graph generation with Matplotlib/Plotly for:
  - Velocity vs. Time
  - Displacement vs. Time
  - Acceleration vs. Time
- 📁 History tracking using JSON
- 🧮 Custom physics formulas through modular Python files
- 🛠 Modular structure for easy scalability

---

## 📂 Project Structure


## User Inputs
- Mass of object (kg)
- Initial velocity (m/s)
- Acceleration (m/s²)
- Duration of motion (s)
- Time step for simulation (s)

## Outputs
- Final velocity and displacement
- Step-by-step motion data
- Optional: line charts and table view (Streamlit-native)

## Concepts Practiced
- Python classes and functions
- Kinematics & physics formulas
- NumPy arrays and time-stepping
- Streamlit UI development
- File handling & logging (optional)

## Future Enhancements
- Projectile motion simulation (angle + gravity)
- Multiple object comparisons
- CSV uploads for motion data
- Lightweight animation and visualization

Motion_Simulator_App/ ├── app.py                  # Main Streamlit interface ├── motion.py              # Handles motion calculations ├── simulator.py           # Runs simulation logic ├── utils.py               # Utility functions ├── history.json           # Logs user simulation history ├── requirements.txt       # Dependency file └── README.md              # This file

---

## ⚙️ Setup Instructions

##1. **Clone the repository**
   ```bash
   git clone https://github.com/Zahab163/Motion_Simulator_App.git
   cd Motion_Simulator_App

##- Create virtual environment (optional but recommended)
python -m venv env
env\Scripts\activate
- Install dependencies
pip install -r requirements.txt

- Run the app
streamlit run app.py



##📊 Graphs & Visualization
This app uses [Matplotlib/Plotly] to generate:
- Velocity-Time Graph
- Displacement-Time Graph
- Acceleration-Time Graph

-## 🧪 Physics Behind the Scenes
The app simulates uniformly accelerated motion using formulas:
- Velocity: v = u + at
- Displacement: s = ut + (1/2)at²
- Acceleration: Constant input by user

Absolutely, Zahabia! Here's a fully drafted README.md template tailored for your Motion Simulator app. I've structured it so you can plug in details easily, especially for sections like graphs or visual outputs. You can tweak and expand it as your project evolves.

# 🚀 Motion Simulator App

The Motion Simulator App is an interactive tool built with **Python** and **Streamlit** that visualizes physics-based motion in real time. Users can input motion parameters, simulate movement, and view dynamic graphs representing velocity, displacement, and acceleration.

---

## 📸 Demo

Include a screenshot or GIF here once your app is deployed.  
Example:  
App Screen video
https://github.com/user-attachments/assets/53fa79fa-71d0-428c-bb6d-caa1d13a8684



## 🧠 Features

- 🎛 Real-time input of motion parameters (initial velocity, acceleration, time)
- 📈 Dynamic graph generation with Matplotlib/Plotly for:
  - Velocity vs. Time
  - Displacement vs. Time
  - Acceleration vs. Time
- 📁 History tracking using JSON
- 🧮 Custom physics formulas through modular Python files
- 🛠 Modular structure for easy scalability

---

## 📂 Project Structure


Motion_Simulator_App/ ├── app.py                  # Main Streamlit interface ├── motion.py              # Handles motion calculations ├── simulator.py           # Runs simulation logic ├── utils.py               # Utility functions ├── history.json           # Logs user simulation history ├── requirements.txt       # Dependency file └── README.md              # This file

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Zahab163/Motion_Simulator_App.git
   cd Motion_Simulator_App


- Create virtual environment (optional but recommended)
python -m venv env
env\Scripts\activate
- Install dependencies
pip install -r requirements.txt


- Run the app
streamlit run app.py



📊 Graphs & Visualization
This app uses [Matplotlib/Plotly] to generate:
- Velocity-Time Graph
- Displacement-Time Graph
- Acceleration-Time Graph
To customize or expand graphing features, explore simulator.py and motion.py.

🧪 Physics Behind the Scenes
The app simulates uniformly accelerated motion using formulas:
- Velocity: v = u + at
- Displacement: s = ut + (1/2)at²
- Acceleration: Constant input by user

🗂 Version Control
This project uses Git for version control.
Branch strategy: main for stable releases.
Feel free to fork or contribute via pull requests.

📬 Connect
Created with 💡 by Zahabia
🔗 LinkedIn
📂 GitHub Portfolio

📄 License
MIT License








- 




