from setuptools import setup

package_name = 'learn_ros'

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
    maintainer='srini',
    maintainer_email='srini@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'draw_square=learn_ros.draw_square:main',##ADDED MANUALLY FOR REGISTERING AS NODE
            'talker=learn_ros.talker:main',
            'listener=learn_ros.listener:main',
            'add_service=learn_ros.add_service:main',
        ],
    },
)
