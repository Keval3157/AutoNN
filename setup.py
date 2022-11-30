from distutils.core import setup
from pathlib import Path
from setuptools import find_packages


currect_file = Path(__file__).resolve()
readme = currect_file.parent/"README.md"


setup(
    name = "autonn",
    version = "1.0.0",
    description="An AutoML framework for deep learning",
    long_description=readme.read_text(),
    long_description_content_type = "text/markdown",
    url= "https://github.com/AutoNN/AutoNN",
    keywords=['AutoNN','autonn','AutoML','Deep Learning','CNN'],
    install_requires=[
        'torch',
        'torchvision',
        'torchaudio',
        'ttkbootstrap==0.5.1',
        'pytorchsummary',
        'tensorflow==2.8.0',
        'sklearn',
        'pandas',
        'dask',
        'dask-ml',
        'tqdm',
        'psutil',
    ],
    entry_points={
        'gui_scripts': [
            'autonn = AutoNN.__main__:main',
        ]
    },
    authors = "Anish Konar, Arjun Ghosh, Rajarshi Banerjee, Sagnik Nayak.",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
    ],
    license="Apache License 2.0",
    packages=find_packages(exclude=("*test*",)),

)