# Collecting Data

The easiest way to collect data is to use the evaluation software theat comes with the devices and post-process it later. This won't let you do any real-time processing but is used to verify the sensors are working and can be used to collect the data required to build a dataset like Kitti.

| Data type | Source | Software |
| --------- | ------ | -------- |
| Point cloud | OS2-128 | Ouster-Studio or Ouster SDK |
| Images    | Realsense-D455 | Realsense-viewer or Realsense SDK |
| IMU       | Ouster or Realsense | Realsense-viewer* |
| GPS       | U-Blox7 or Garmin 18x LVC | PyGPSClient

* Although the lidar does have its own IMU, the data is broadcast to a port that Ouster-Studio is not listening to. A script can be written to record this data or the realsense IMU can be read by the realsense-viewer as long as a USB 3.0 or 3.1 cable and interface is used to support high data rate.

### 1. Enable PTP on network interface

PTP (Precision time protocol) is important to ensure synchronization between devices and timestamps given to data by the PC are as accurate to their true values as possible. 
```
sudo ptp4l -S -i enp118s0 -m
```
In this example, **enp118s0** is the network interface for Junaid's laptop. type `ifconfig` to see a list of network interfaces. For more information on setting up PTP with the lidar sensor, see [PTP Quickstart](https://static.ouster.dev/sensor-docs/image_route1/image_route2/appendix/ptp-quickstart.html)

### 2. Launch and configure Realsense-Viewer

*If using a port or cable below USB3.0, the realsense software will have issues transmitting both IMU and camera data due to insufficient bandwidth.*

1. Launch the realsense-viewer, open the terminal and type 
```
# Launch the application
realsense-viewer
```
2. Configure the camera to be triggered by the sync cable
`Stereo Module > Controls > Inter-cam sync mode: 4`
3. Enable Camera and IMU
4. Click Record

### 3. Launch Ouster-Studio

If you downloaded the .appimage you may need to allow it to be executed before it will run. 

1. Navigate to the file in the terminal and run the following commands.
```
# Modify permissions to allow execution
chmod a+x Ouster-Studio*.AppImage

# Run program
./Ouster-Studio*.AppImage
```

2. Configure timestamps to be stamped by PTP
``

3. Configure ouster to trigger camera frame capture
`MultipurposeIO = Output on encoder angle`

4. View output

5. Click record

### 4. Launch pyGPSClient

PyGPSClient is a cross platform gps tool which was used since the evaluation software for the GPS used was not compatible with Linux. 

```
pygpsclient
```