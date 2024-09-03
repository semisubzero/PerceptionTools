# Introduction

!!IMPORTANT!! This guide was written specifically for the 3rd party manufacturer Seeed Studio and the drivers available for the jetson in 2023. If you are following this guide, double check the linked resources to determine if the steps have changed.

This page will walk you through setting up an Nvidia Jetson AGX Xavier H01 with a fresh operating system and required software to get started with running AI applications on the device. Once set up, you'll be ready to follow another guide to set up an AI model, like this [YOLOv8 guide](https://github.com/semisubzero/YOLOv8-Xavier/wiki/Setting-up-YOLOv8). 

Please pay close attention to software versions mentioned in the guide. The Nvidia jetson from Seeed Studio only supports a subset of Nvidia software which only support specific versions of other software.   

Setting up the Jetson consists of two main steps. 
1. Installing the drivers and OS
2. Installing Jetpack for all the required Nvidia software packages

_Resources: https://wiki.seeedstudio.com/Jetson_Xavier_AGX_H01_Driver_Installation/_

# Drivers and OS
### Materials to get started
1. A PC with Ubuntu installed. (This guide was tested with Ubuntu 18.04 and 20.04)
2. Nvidia Jetson AGX Xavier H01 manufactured by seeed studio
3. USB-C Data cable
4. Mouse, Keyboard, and monitor to use the Jetson

### Step 1 - Download drivers and operating system files
First, we will begin by downloading Nvidia's drivers, Seeed Studio's drivers, and a sample filesystem that we will use to set up the device. This guide covers installing the environment required for Jetpack 5.0.2

**Download:** https://files.seeedstudio.com/wiki/H01Driver/H01_Driver_for_5.0.2.zip  
**Download:** https://developer.nvidia.com/embedded/l4t/r35_release_v1.0/release/jetson_linux_r35.1.0_aarch64.tbz2  
**Download:** https://developer.nvidia.com/embedded/l4t/r35_release_v1.0/release/tegra_linux_sample-root-filesystem_r35.1.0_aarch64.tbz2

### Step 2 - Unzip files
Next, unzip the H01_Driver_for_5.0.2.zip and the jetson_linux_r25.1.0_aarch64.tbz2. Commands for doing this are provided below. Make sure these files are inside the same folder, ie Downloads.

```
sudo apt-get install unzip  
unzip H01_Driver_for_5.0.2.zip  
tar xf Jetson_Linux_R35.1.0_aarch64.tbz2
```

### Step 3 - Apply filesystem
Open the Linux_for_Tegra folder and run the following commands to set up our filesystem.

```
cd Linux_for_Tegra/rootfs  
sudo tar xfp ../../Tegra_Linux_Sample-Root-Filesystem_R35.1.0_aarch64.tbz2  
cd ..  
sudo ./apply_binaries.sh
```

### Step 4 - Apply drivers
Boot the Jetson into recovery mode. You can do this by holding the middle button (next to the power button) while powering on. Using the command line, we will copy the drivers over and flash the device.

```
cd ..  
cp -a -f H01_Driver_for_5.0.2/Linux_for_Tegra/kernel Linux_for_Tegra/  
cd Linux_for_Tegra/  
sudo ./flash.sh jetson-xavier mmcblk0p1
```

### Step 5 - Flash device
Once flashing is complete, the Jetson will restart and you will be able to finish making a user for the OS.

# Jetpack

Installing Jetpack is more straightforward and done by the Nvidia SDK Manager.  

### Step 1 - Download
**Download:** https://developer.nvidia.com/sdk-manager

### Step 2 - SDK Manager setup

Open the SDK manager and select Jetpack version 5.0.2 (rev 2), Nvidia Jetson AGX Xavier as the board, and make sure that DeepStream is checked to be installed.

### Step 3 - Installation

Since we installed custom drivers and OS, we can uncheck []Install drivers and []Install OS. Make sure everything else is checked and hit next.

### Step 4 - Post installation

The last two things we need to do is install a few more dependencies and update the software. The following commands are for the Jetson's terminal, not the host PC.

This can be pasted into the terminal all at once
```
sudo apt install \
libssl1.1 \
libgstreamer1.0-0 \
gstreamer1.0-tools \
gstreamer1.0-plugins-good \
gstreamer1.0-plugins-bad \
gstreamer1.0-plugins-ugly \
gstreamer1.0-libav \
libgstreamer-plugins-base1.0-dev \
libgstrtspserver-1.0-0 \
libjansson4 \
libyaml-cpp-dev
```

Update software
```
sudo apt update  
sudo apt install -y python3-pip  
pip3 install --upgrade pip  
```

If all goes well you should have a fresh OS and software to get started working with AI. [Check out how to set up YOLOv8](https://github.com/semisubzero/YOLOv8-Xavier/wiki/Setting-up-YOLOv8)
