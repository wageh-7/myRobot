from setuptools import find_packages, setup

package_name = 'my_laser_package'

setup(
    name=package_name,
    version='0.0.0',
   packages=find_packages(include=['my_laser_package', 'my_laser_package.*']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy', 'sensor_msgs'],
    zip_safe=True,
    maintainer='wageh',
    maintainer_email='wageh@todo.todo',
    description='A ROS2 package to subscribe to laser scan data',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lider_node = my_laser_package.lider_node:main',
        ],
    },
)
