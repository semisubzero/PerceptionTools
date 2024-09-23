# PerceptionTools

[Installation]() |
[Calibration]() |
[Data collection]() |
[Dataset creation]() |
[Setting up jetson]() |
[Realtime YoloV8]()
### Submodules  
[PyGPSClient]() |
[Segment-anything]() |
[SensorsCalibration]()

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