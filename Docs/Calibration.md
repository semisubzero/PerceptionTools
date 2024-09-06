# Calibrating sensors

There are two types of sensor calibration, extrinsic and intrinsic calibration. Extrinsic calibration is related to the sensors position in 3D space relative to each other, and it is a matrix containing the transformation and rotation required to superimpose sensor data from one ontop of the other, seen in the image below.

## Intrinsic Calibration

Intrinsic calibration consists of the transformations required to correct errors within the sensor itself. Since camera and lidar are both optical devices, there is some refraction as light passes through the lense which creates distortion in the final image. Application of the transformation matrix will remove this distortion. Both the Lidar and Camera should have pre-calibrated intrinsic values.

### Lidar intrinsic

Lidar intrinsic values are provided by Ouster Studio. The OS2-128 is calibrated at the factory so manual calibration is not neccessary. When recording data, both a .pcap containing points and a .json containing intrinsic calibration will be generated. Both of these files are required to read the sensor data.

### Camera intrinsic

Camera intrinsic values are provided by Realsense-Viewer and are also calibrated at the factory. The realsense viewer provides tools to automatically recalibrate the camera if the intrinsics are not correct.

## Extrinsic Calibration

Extrinsic calibration depends on how you place the sensors in 3D space relative to each other. Generally it's desireable to mount the sensors to some kind of fixture so the calibration remains unchanged when taking the sensors on and off the vehicle.

### Lidar 2 camera extrinsic
![PointSuperimpose](../SensorsCalibration/lidar2camera/auto_calib_v2.0/refined_proj_seg.png)


[Lidar-Camera Calibration](https://www.mathworks.com/help/lidar/ug/lidar-camera-calibration.html)

### IMU2Camera extrinsic

IMU extrinsics come from the device it is packaged with. Each devices respecive evaluation software can create the IMU extrinsics of its own packaged IMU. This can then be combined with the lidar2camera extrinsic data to align all 3 sensors in 3D space.