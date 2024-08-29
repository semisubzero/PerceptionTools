# Time Synchronization

[Intel realsense](https://dev.intelrealsense.com/docs/multiple-depth-cameras-configuration#:~:text=For%20HW%20sync%2C%20pins%205%20%28SYNC%29%20and%20pins,pin%205%20and%20pin%209%20to%20pin%209)  
[Alignment and calibration video](https://developer.cepton.com/video/calibrate_align_camera_lidar)  
[Helpful sensor time synchronization thread](https://discourse.ros.org/t/experience-with-ptp-precision-time-protocol-for-mobile-robots/24707/6)

### PTP 

There are both software and hardware PTP implementations to choose from. The hardware implementation requires hardware that supports timestamp transmission and should be accurate to 100s of nanoseconds. Software PTP requires drivers that support timestamp transmission and is accurate to the system clock. Most windows PCs have an error of ~16ms.

**Software** - We rely on PTP as the network topology is fixed. Software PTP allows for broader compatibility across hardware devices, but comes more drift, and jitter in synchronization of the clock compared to PTP in hardware. For most of the high level applications (i.e. monitoring) this can be sufficient.

**Hardware** - When tighter accurate is needed PTP implemented in a combination of hardware and firmware; this has the added cost of verifying interoperability between the hardware components. There is effort involved to have the computer, switches, and sensors all support PTP in HW.

For sensors, time synchronization methods are more fragmented. We strive to have the highest accuracy for the acquisition time of the sensor data when we need it. We measure acquisition time where possible, and derive acquisition time from arrival time at the computer; acquisition time is when the sensor reads measurements (i.e. photons | waves). When we are unable to measure acquisition time, we strive for the lowest jitter on arrival time of the sensor data at the computer to more reliably derive the acquisition time.

In practice for sensors we timestamp key events using timestamping hardware in our computer with 2us accuracy. We use this hardware timestamp as the singular common clock source, to align the multiple concurrent clock domains where acquisition and arrival time measurements occur. timestamps are captured by the hardware for the linux kernel clock, PTP, PPS, and several camera interface events (i.e. frame sync, frame start, frame stop), so we can convert time between the various fragmented clocks. This is the most effort invested method for time synchronization as it’s used to provide the highest accuracy for recorded sensor streams which are inputs to sensor fusion functions, offline development of perception systems, and offline re-simulation of open loop perception systems real data for testing. Accuracy of acquisition time for these operations correlates to accuracy in three dimensions of perception.

LIDAR is used with PTP over ethernet, and PPS measuring acquisition time. In indoor applications, the computer generates PPS as GPS does not work. In both cases we hardware timestamp PPS to accurately derive acquisition time. RADAR is typically PTP on Ethernet, and hardware measured on a CAN interface, both providing arrival time. Camera and IMU are very precise with timestamps in hardware as we connect them directly to the computer; frame synchronization is used to trigger all the camera’s to capture at the same time for an aligned observation of data.

Hardware timestamping mechanisms allow the platform to maintain accuracy under heavy load.

## Motion Compensation

Only required for temporal point cloud stitching such as SLAM.