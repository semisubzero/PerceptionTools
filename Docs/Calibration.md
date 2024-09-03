# Calibrating sensors

There are two types of sensor calibration, extrinsic and intrinsic calibration. Extrinsic calibration is related to the sensors position in 3D space relative to each other, and it is a matrix containing the transformation and rotation required to superimpose sensor data from one ontop of the other, such as  

### Lidar 2 camera extrinsic
![PointSuperimpose](../SensorsCalibration/lidar2camera/auto_calib_v2.0/refined_proj_seg.png)


[Lidar-Camera Calibration](https://www.mathworks.com/help/lidar/ug/lidar-camera-calibration.html)

### Lidar intrinsic

Lidar intrinsic values are provided by Ouster Studio. When recording data, a .pcap containing points and a .json containing intrinsic calibration will be generated.

### Camera intrinsic

Camera intrinsic values are provided by Realsense-Viewer. 