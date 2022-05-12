
# set source
`. ~/ros2_foxy/ros2-linux/setup.bash`

# create package
`ros2 pkg create dvl_a50 --dependencies std_msgs rclpy --build-type ament_python`


# make sure of the  ROS2 version - it is foxy
`printenv ROS_DISTRO`

# install dependencies
`rosdep install -i --from-path src --rosdistro foxy -y`

# requires to install 
`sudo apt install python3-rosdep2`

# custom interfaces
[tutorial for custom messages](https://docs.ros.org/en/foxy/Tutorials/Custom-ROS2-Interfaces.html)

DVLBeam and DVL messages in the same msg folder 

#  build custom interface and msg
build clean
`rm -r build install`

build interface
`colcon build --packages-select dvl_interface`

show dvl interface
`ros2 interface show dvl_interface/msg/DVL`

# build selected component
`colcon build --packages-select sim_dvl_a50`
`colcon build --packages-select dvl_a50`

# source the setup files (path must be dev  root), this has be done before custom made packages are visible
`. install/setup.bash`

`ros2 run py_pubsub talker`

# import extra py
seems to be very complicated but this does the trick

[link](https://stackoverflow.com/questions/57426715/import-modules-in-package-in-ros2)

``` 
import sys
sys.path.append("/home/jte/ros2_ws/trial_2/build/install/sim_dvl_a50/lib/python3.8/site-packages/sim_dvl_a50")

from sim_dvl_a50.dvl import dvl_data
```

requires also

c++

sudo apt install build-essential 

OpenSSL

sudo apt-get install libssl-dev



`colcon build --packages-select dvl_beam_interface`