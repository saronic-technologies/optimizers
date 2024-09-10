from setuptools import find_packages, setup
import os

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files('distributed_shampoo')

setup(
    name="distributed_shampoo",
    version="0.1.0",
    description="PyTorch implementation of Distributed Shampoo",
    license="BSD 3-clause",
    packages=find_packages(),
    package_data={'distributed_shampoo': extra_files},
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
