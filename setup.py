#!/usr/bin/python

from setuptools import setup, find_packages

install_requires = \
    [

    ]

setup(
    name='bittrex_websocket',
    version='0.0.0.1',
    author='Stanislav Lazarov',
    author_email='s.a.lazarov@gmail.com',
    license='MIT',
    url='https://github.com/slazarov/python-bittrex-websocket-aio',
    packages=find_packages(exclude=['tests*']),
    install_requires=install_requires,
    description='The unofficial Python websocket (AsyncIO) client for the Bittrex Cryptocurrency Exchange',
    download_url='https://github.com/slazarov/python-bittrex-websocket-aio.git',
    keywords=['bittrex', 'bittrex-websocket', 'orderbook', 'trade', 'bitcoin', 'ethereum', 'BTC', 'ETH', 'client',
              'websocket', 'exchange', 'crypto', 'currency', 'trading'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
