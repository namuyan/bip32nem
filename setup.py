#!/usr/bin/env python

from setuptools import setup

setup(
    name='bip32nem',
    version='0.3-4',
    author='Johnathan Corgan, Corgan Labs',
    author_email='johnathan@corganlabs.com',
    maintainer='Pavol Rusnak',
    url='http://github.com/namuyan/bip32utils',
    description='Utilities for generating and using Bitcoin Hierarchical Deterministic wallets (BIP0032).',
    license='MIT',
    install_requires=['ecdsa'],
    packages=['bip32nem']
)
