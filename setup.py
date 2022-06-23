from setuptools import setup, find_packages

setup(
    name='showtemp',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'psutil==5.9.1',
        'importlib-metadata; python_version >= "3.6"',
    ],
    entry_points={
        'console_scripts': [
            'showtemp = showtemp.command_line:main',
        ]
    },
)
