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
git clone https://github.com/semisubzero/PerceptionTools.git
```  

### 2. Install Nvidia SDK Manager

Follow the instructions here to install the Nvidia SDK manager for your system.  This requires a linux host system and an nvidia edge compute platform.  
```
# Install nvidia jetson tools
https://developer.nvidia.com/sdk-manager  
```

### 3. Install Realsense SDK

Follow the instructions here to install the Realsense SDK for your system for recording camera data. This will include python tools, realsense viewer, and real-time support  
```
# Install realsense camera software
https://www.intelrealsense.com/sdk-2/
```

### 4. Install Ouster Studio

Follow the instructions here to install Ouster Studio for your system for recording lidar data.  
```
# Install ouster lidar software
https://ouster.com/products/software/ouster-studio
```

### 5. Install python

Install python 3.11

```
# Install version 3.11 of python if it's not already installed
sudo apt-get update
sudo apt-get install python3.11
```
### 6. Set up virtual environment

Before downloading and installing all of the required libraries its important to set up a virtual environment. This will allow us to install conflicting software into different "virtual environments" which will act as software "presets". This allows us to install different versions of the same library into different virtual environments so we can switch between them if some tools require specific versions.  If you're comfortable with a package manager such as conda, feel free to use that to install everything. These instructions will only use tools that come with python

```
# Create virtual environment called "perc"
python -m venv perc

# Activate the environment 
./perc/bin/Activate

# Install repository requirements
python -m pip install -r requirements.txt  
```

### 7. Compile SensorsCalib Lidar2Camera tool

```
# Enter project directory
cd SensorsCalibration

# Enter lidar2camera directory
cd lidar2camera

# Enter auto_calib tool directory
cd auto_calib_v2.0

# Create and enter build directory
mkdir -p build && cd build

# Compile
cmake .. && make
```

### 8. Install Segment-Anything

Segment-anything is used to create a mask for automatic calibration this is not needed for matlab or manual calibration

### 10. Install PTP Support

ptp4l

### 11. Install PyGPSClient

If your GPS has evaluation software compatible with linux feel free to use that. This software was used for reading a U-blox 7 GPS since the U-Center evaluation software was only compatible with windows. 

```
# Install PyGPSClient dependencies
sudo apt install python3-pip python3-tk python3-pil python3-pil.imagetk libjpeg-dev zlib1g-dev

# Add yourself to the tty group to access the serial port
usermod -a -G tty <username>
```

### 12. Profit!

Now that you've installed the repository, the sections below will guide you through some of the things you can do with the tools.

# Calibration

There are several methods for calibration. For more information, see [Calibration](/Docs/Calibration.md)

### SensorsCalibration - Auto_Calib_2.0 automatic

Uses AI models to generate a mask of straight objects within a scene, projects lidar points onto the mask, and then reduces error to create the calibration transformation matrix

### SensorsCalibration - Auto_Calib_2.0 manual

No AI models, use keyboard controls to overlay and align point clouds ontop of image features

### Matlab

Take calibration images of a checkerboard pattern. Select features on image and point cloud within matlab
see [Matlab calibration](https://www.mathworks.com/help/lidar/ug/get-started-lidar-camera-calibrator.html)

# Data collection

For a step by step process to collecting data, see [Collecting Data](/Docs/CollectingData.md)

# Dataset creation (Postprocessing)

For a step by step process to postprocessing data into a dataset, see [Creating a dataset](/Docs/Creatingadataset.md)