from setuptools import setup, find_packages

setup(
    name="pathfinding-simulation",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pygame>=2.5.0",
        "numpy>=1.24.0",
    ]
)
