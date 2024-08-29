# Introduction

This guide assumes you have [Followed this guide](https://github.com/semisubzero/YOLOv8-Xavier/wiki/Setting-up-the-Jetson) to install the OS and required software packages for DeepStream on the Nvidia Jetson. The entirety of this guide will use the Jetson so the host computer is no longer needed.

To set up YOLOv8 we will be using two code repositories. [The original](https://github.com/ultralytics/ultralytics) YOLOv8 repository, and a [DeepStream](https://github.com/marcoslucianops/DeepStream-Yolo) repository for the Jetson. We will only use the original repository to generate the model weights for the DeepStream application.

_Resources: https://wiki.seeedstudio.com/YOLOv8-DeepStream-TRT-Jetson/_

# Required software packages

We start by downloading the original repository and installing its dependencies. Navigate to the folder you want to download the code into, and open a terminal there.

### Step 1 - Clone repo

```
git clone https://github.com/ultralytics/ultralytics.git
```

### Step 2 - Edit requirements.txt

The Jetson only supports very specific versions of torch and torchvision depending on the version of Jetpack installed. We will assume you installed 5.0.2 per the previous guide. Because of this, we will need to comment out those dependencies from the requirements.txt file and install them ourselves. To do this, we will add a # to the beginning of the lines with those dependencies.

```
sudo apt-get install nano  
cd ultralytics  
nano requirements.txt
```

Add a \# to the following lines

```
# torch>=1.7..0  
# torchvision>=0.8.1
```

### Step 3 - Install requirements

Install all the other packages from requirements.txt
```
pip3 install -r requirements.txt
```

It'll probably give you an warning about python-dateutil during the process
```
pip3 install python-dateutil --upgrade
```

# Install PyTorch & Torchvision

Since the Jetson uses ARM based architecture, we cannot install PyTorch and Torchvision via pip. [Here](https://forums.developer.nvidia.com/t/pytorch-for-jetson) is the list of downloads from Nvidia. We will be using PyTorch 1.12.0 and Torchvision 1.13.0 since we installed Jetpack version 5.0.2

### Step 1 - PyTorch
You may need to change the filenames to what you downloaded from nvidia

```
cd ..
wget https://developer.download.nvidia.com/compute/redist/jp/v50/pytorch/torch-1.12.0a0+2c916ef.nv22.3-cp38-cp38-linux_aarch64.whl
sudo apt-get install python3-pip libopenblas-base libopenmpi-dev libomp-dev  
pip3 install Cython  
pip3 install numpy torch-1.12.0a0+2c916ef.nv22.3-cp38-cp38-linux_aarch64.whl
```

### Step 2 - Torchvision

```
sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libopenblas-dev libavcodec-dev libavformat-dev libswscale-dev  
git clone --branch v0.13.0 https://github.com/pytorch/vision torchvision  
cd torchvision  
export BUILD_VERSION=0.13.0  
python3 setup.py install --user  
cd ../  
pip install 'pillow<7'
```

### Step 3 - Verification

You can verify that PyTorch and Torchvision installed correctly by printing their versions in the python console.

```
python3

import torch
import torchvision

print(torch.__version__)
print(torchvision.__version__)

exit()
```


# Configure DeepStream

Now we will finish setting up DeepStream and run YOLOv8

### Step 1 - Clone Repo
Navigate back to the folder where

```
git clone https://github.com/marcoslucianops/DeepStream-Yolo
cd DeepStream-Yolo
git checkout 68f762d5bdeae7ac3458529bfe6fed72714336ca
```

### Step 2 - Generate weights

```
cp utils/gen_wts_yoloV8.py ../ultralytics 
cd ../ultralytics
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s.pt
```

You can change inference size by adding -s <height> <width>

```
python3 gen_wts_yoloV8.py -w yolov8s.pt
```

### Step 3 - Copy Weights

```
cp yolov8s.cfg ../DeepStream-Yolo
cp yolov8s.wts ../DeepStream-Yolo
cp labels.txt ../DeepStream-Yolo
```

### Step 4 - Compile library

```
cd ~/DeepStream-Yolo
CUDA_VER=11.4 make -C nvdsinfer_custom_impl_Yolo
```

### Step 5 - Configure

```
```

### Step 6 - Run

```
deepstream-app -c deepstream_app_config.txt
```

