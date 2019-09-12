  
from setuptools import setup, find_packages

setup(
    name='decodem_stats',
    version='0.0.6',
    author='Decode_M Data Science',
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