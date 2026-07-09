# MAUV Test Robot

## Overview
This repository provides a mockup MAUV robot for ROS 2 MVP (Marine Vehicle Package) framework development and simulation, where MAUV refers to Multi Autonomous Underwater Vehicle. It includes the robot package, bringup files, configuration files, and robot description required to run the MAUV platform in the Stonefish simulation environment.

Unlike the previous single-vehicle package, this repository supports a multi-agent setup, where multiple underwater vehicles are simulated together and controlled through a cooperative multi-agent control framework.

## Tested Environment
- ROS 2: Jazzy
- Ubuntu: 24.04

## Repository Structure
- `mauv_test_robot`  
  Core robot package files.

- `mauv_test_robot_bringup`  
  Bringup package for launching the MAUV in simulation.
  - `launch`
    - `bringup_simulation.launch.py`: launches the simulation environment
    - `bringup_simulation_mauv.launch.py`: launches the MAUV-specific simulation setup
  - `config`
    - ROS parameter files in `.yaml` format

- `mauv_test_robot_config`  
  MVP-related configuration files.
  - `mvp_control_config`
    - Control-layer configuration files
  - `mvp_mission_config`
    - Mission-layer configuration files

- `mauv_test_robot_description`  
  Robot description files.
  - `urdf`
    - Robot URDF files
  - `mesh`
    - Mesh files used by the robot model
  - `config`
    - Additional description-related configuration files

## Simulation Setup

### Stonefish Simulator
We use the Stonefish simulator for underwater robot simulation and development.

#### Installation
Clone the Stonefish repository:
```bash
git clone https://github.com/patrykcieslak/stonefish.git
```

Install required dependencies:
```bash
sudo apt install libglm-dev libsdl2-dev libfreetype6-dev
```

You may also need:
```bash
sudo apt install libpcl-dev
```

Build Stonefish:
```bash
cd stonefish
mkdir build
cd build
cmake ..
make -j$(nproc)
sudo make install
```

If you encounter a build error related to `Sample.h`, add:
```cpp
#include <cstdint>
```

to:
```bash
/stonefish/Library/include/sensors/Sample.h
```

### Stonefish ROS 2 Wrapper
Install the ROS 2 wrapper for Stonefish:
```bash
git clone https://github.com/patrykcieslak/stonefish_ros2.git
```

### World of Stonefish
All simulator files related to the Stonefish environment are included in the `world_of_stonefish` repository. This repository contains Stonefish scenario files and drivers that connect Stonefish sensor messages to MVP-compatible messages.

Clone it with:
```bash
git clone https://github.com/GSO-soslab/world_of_stonefish.git
cd world_of_stonefish
git checkout jazzy-devel
```

Typical directory structure:
- `data`: simulator assets
- `metadata`: material and visual settings
- `vehicles`: vehicle scenario files
- `world`: world scenario files
- `include` and `src`: source files for Stonefish sensor drivers

If needed, the USBL driver uses a customized `acomms_msgs` package:
```bash
https://github.com/GSO-soslab/acomms_msgs.git
```

## MVP Framework in ROS 2
The MVP framework is used as the guidance, navigation, and control framework for the marine vehicle platform.

### Robot Localization
The localization pipeline uses:
```bash
sudo apt install ros-jazzy-robot-localization
```

### MVP Utilities
```bash
git clone https://github.com/uri-ocean-robotics/mvp_utilities.git
cd mvp_utilities
git checkout jazzy-devel
```

### MVP Control
```bash
git clone https://github.com/uri-ocean-robotics/mvp_control.git
cd mvp_control
git checkout jazzy-devel
```

Install GSL if needed:
```bash
sudo apt-get install libgsl-dev
```

### MVP Messages
```bash
git clone https://github.com/uri-ocean-robotics/mvp_msgs.git
cd mvp_msgs
git checkout jazzy-devel
```

### MVP Mission
```bash
git clone https://github.com/uri-ocean-robotics/mvp_mission.git
cd mvp_mission
git checkout jazzy-devel
```

## Build
After installing the required packages, build the ROS 2 workspace:
```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

## Run the MAUV Simulation
Launch the simulation:
```bash
ros2 launch mauv_test_robot_bringup bringup_simulation.launch.py
```

or:
```bash
ros2 launch mauv_test_robot_bringup bringup_simulation_mauv.launch.py
```

## Multi-Agent Control Integration
This repository is used together with `simple_controller_pkg`, which provides the cooperative controller for the multi-agent MAUV system. While `mauv_test_robot` defines the robot, simulation, and bringup environment, the control logic for coordinating multiple agents is implemented in `simple_controller_pkg`.

Launch the multi-agent controller:
```bash
ros2 launch simple_controller_pkg swarm_control.launch.py

For yaw extraction:
```bash
ros2 run simple_controller_pkg yaw_extractor_node \
  --ros-args \
  -p world_odom_topic:=/mauv_1/world_odom \
  -p wp_odom_topic:=/mauv_1/waypoint_odom
```

## Visualization and Logging

### Foxglove
```bash
ros2 launch foxglove_bridge foxglove_bridge_launch.xml
```

Then open:
```bash
foxglove-studio
```

### Bag Recording
To record all topics:
```bash
ros2 bag record -a -o /home/soslab-p330/ros2_ws/my_run_bag
```

## Notes
- This repository is intended for MAUV simulation and MVP framework integration in ROS 2.
- Some components depend on external repositories and packages, including the Stonefish ROS 2 wrapper (`stonefish_ros2`), `world_of_stonefish`, `mvp_control`, `mvp_msgs`, `mvp_utilities`, and `mvp_mission`.
- Topic names, namespaces, and launch configurations may need to be adjusted depending on the specific experiment setup.