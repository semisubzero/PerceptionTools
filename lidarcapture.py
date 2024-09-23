from ouster.sdk import open_source
from ouster.sdk import client


#  create empty config
config = client.SensorConfig()

# set the values that you need: see sensor documentation for param meanings
config.operating_mode = client.OperatingMode.OPERATING_NORMAL
config.lidar_mode = client.LidarMode.MODE_1024x10
config.udp_port_lidar = 7502
config.udp_port_imu = 7503
hostname = 'os-122414001752.local'

# set the config on sensor, using appropriate flags
client.set_config(hostname, config, persist=True, udp_dest_auto=True)