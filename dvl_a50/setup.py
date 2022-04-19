from setuptools import setup

package_name = 'dvl_a50'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jte',
    maintainer_email='jutervo@outlook.com',
    description='DVL A50 ROS2 package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dvl_a50 = dvl_a50.dvl_a50:main'
        ],
    },
)
