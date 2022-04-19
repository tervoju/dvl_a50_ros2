
# custom ROS2 package

dependencies

`rosdep install -i --from-path src --rosdistro foxy -y`

build package
`colcon build --packages-select dvl_a50`

check setup.py and package.xml that match the maintainer, maintainer_email, description and license fields to your package.xml
