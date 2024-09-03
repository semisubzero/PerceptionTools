# PerceptionTools

PerceptionTools is a collection of python scrips to aid in sensor calibration and basic data collection for the Ouster OS2 LiDAR and Intel Realsense d455 camera. If you are using VSCode, you can get a nicer looking view of these pages by right clicking and selecting "Open Preview"

# Introduction

The intention of this repository is to provide a basic set of tools to begin data collection and dataset creation with camera, lidar, gps, and IMU. Data collection is done via the respective evaluation softwares for the following devices.

| Device | Type | Software |
| ------ | ---- | -------- |
| Intel realsense D455 | RGB and Depth camera | Realsense-Viewer  
| Ouster OS2-128       | Lidar | Ouster SDK  
| UBLOX7 GPS           | GPS | U-Center or Python script  
| IMU                  | Inertial Measurement Unit | Ouster SDK / Realsense-Viewer  

#### The goal of these tools is to provide a platform to:

1. Collect perception data from vehicle sensors
2. Perform sensor calibration
3. Create structured datasets from collected sensor data

# Installation

### 1. Clone Repo 

```  
git clone <repo url>
```  

### 2. Install Nvidia SDK Manager

Follow the instructions here to install the Nvidia SDK manager for your system.  This requires a linux host system and an nvidia edge compute platform.  
```
# Install
https://developer.nvidia.com/sdk-manager  
```

### 3. Install Realsense SDK

Follow the instructions here to install the Realsense SDK for your system for recording camera data. This will include python tools, realsense viewer, and real-time support  
```
# Install
https://www.intelrealsense.com/sdk-2/
```

### 4. Install Ouster Studio

Follow the instructions here to install Ouster Studio for your system for recording lidar data.  
```
# Install
https://ouster.com/products/software/ouster-studio
```

### 5. Install python

Install a version of python between 3.6 - 3.11  
```
sudo apt-get update
sudo apt-get install python3.11
```
### 6. Set up virtual environment

Before downloading and installing all of the required libraries its important to set up a virtual environment. This will allow us to install conflicting software into different "virtual environments" which will act as software "presets". This allows us to install different versions of the same library in case some tools require specific versions.  If you're comfortable with a package manager such as conda, feel free to use that to install everything. These instructions will only use tools that come with python
```
# Create virtual environment called "perc"
python -m venv perc

# Activate the environment 
./perc/bin/Activate

# Install repository requirements
python -m pip install -r requirements.txt  
```

### 7. Install SensorsCalib
### 8. Install Segment-Anything
### 9. Install repo
### 10. ???
### 11. Profit!

Now that you've installed the repository, the sections below will guide you through some of the things you can do with the tools.

# Calibration

There are several methods for calibration.

### SensorsCalibration - Auto_Calib_2.0 automatic
### SensorsCalibration - Auto_Calib_2.0 manual
### Matlab

For more information, see [Calibration](/Docs/Calibration.md)

# Data collection

For a step by step process to collecting data, see [Collecting Data](/Docs/CollectingData.md)

# Dataset creation (Postprocessing)

For a step by step process to postprocessing data into a dataset, see [Dataset Creation](/Docs/DatasetCreation.md)
