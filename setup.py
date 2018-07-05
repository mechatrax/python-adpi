from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='adpi',
    version='1.0.0',
    description='Python module to control the ADPi family',
    long_description=readme(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: System :: Hardware',
    ],
    keywords='adpi raspberrypi',
    url='https://github.com/mechatraix/python-adpi',
    author='Masahiro Honda',
    author_email='honda@mechatrax.com',
    license='MIT',
    packages=[
        'adpi',
        'adpi/ADC',
        'adpi/EEPROM',
        'adpi/GPIO'
    ],
    install_requires=[
        'spidev',
        'smbus-cffi',
    ],
    include_package_data=True,
    zip_safe=False,
)

