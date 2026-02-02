from setuptools import setup, find_packages

setup(
    name="LAMMPS_Tutorials",
    version="1.1.2",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "LAMMPS_Tutorials": ["*.so"],  # include compiled shared libraries
    },
    description="Educational tutorials and example scripts for learning molecular dynamics simulations using LAMMPS.",
    author="Vikki Varma",
    author_email="vikkivarma16@gmail.com",
    url="https://github.com/vikkivarma16/LAMMPS_Tutorials",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires=">=3.6",
)

