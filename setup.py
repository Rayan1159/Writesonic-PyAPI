from setuptools import setup, find_packages

setup(
    name='writesonic-pyapi',
    version='1.0.0',
    description='A Python API for Writesonic',
    url='https://docs.writesonic-pyapi.dev',
    author='Rayan1159 (Niveus)',
    github='https://github.com/Rayan1159/Writesonic-PyAPI',
    requires=['requests'],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable'
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
