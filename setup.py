# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='jads-nhs-proms',
    version='0.1.0',
    description='fA data science case study of the NHS Digital PROMs data of hip and knee replacements.',
    python_requires='==3.*,>=3.7.0',
    author='Daniel Kapitan',
    author_email='daniel@kapitan.net',
    license='MIT',
    packages=[],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'imbalanced-learn==0.*,>=0.7.0', 'ipykernel==5.*,>=5.3.4',
        'jupyter==1.*,>=1.0.0', 'matplotlib==3.*,>=3.3.0',
        'numpy==1.*,>=1.19.1', 'pandas==1.*,>=1.0.0', 'pyarrow==1.*,>=1.0.0',
        'seaborn==0.*,>=0.10.1', 'toolz==0.*,>=0.10.0',
        'yellowbrick==1.*,>=1.1.0'
    ],
    extras_require={
        "dev": ["black==19.*,>=19.10.0.b0", "dephell==0.*,>=0.8.3"]
    },
)
