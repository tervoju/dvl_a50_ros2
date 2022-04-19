
# custom ROS2 package

dependencies

`rosdep install -i --from-path src --rosdistro foxy -y`

source
`. ~/ros2_foxy/ros2-linux/setup.bash`

build package
`colcon build --packages-select dvl_a50`

package to be used
`. install/setup.bash`

run ros package
`ros2 run dvl_a50 dvl_a50`


check setup.py and package.xml that match the maintainer, maintainer_email, description and license fields to your package.xml
