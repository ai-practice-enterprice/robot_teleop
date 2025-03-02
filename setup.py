from setuptools import find_packages, setup
import glob

package_name = 'robot_teleop'

launch_files = glob.glob('launch/*.launch.py')
config_files = glob.glob('config/*.yaml')

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', launch_files),
        ('share/' + package_name + '/config', config_files),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='arno',
    maintainer_email='arno.joosen@outlook.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'twist_stamper = robot_teleop.twist_stamper:main',
            'twist_unstamper = robot_teleop.twist_unstamper:main',
        ],
    },
)
