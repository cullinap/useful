  
from setuptools import setup, find_packages

setup(
    name='useful-stuff',
    version='0.0.6',
    author='patrick',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'pandas >= 0.25',
        'plotly >= 4.0',
        'numpy',
        'scipy',
    ],
)