from setuptools import setup, find_packages

# A Python API for Writesonic
# Made by niveus (Rayan1159) -> https://github.com/Rayan1159

setup(
    name='writesonic_pyapi',
    version='1.0.0',
    description='A Python API for Writesonic',
    url='https://docs.writesonic-pyapi.dev',
    author='Rayan1159 (Niveus)',
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
    entry_points = {
        'console_scripts': [
            'wsset = writesonic_pyapi.cli_commands.token:set_token',
            'wsdelt = writesonic_pyapi.cli_commands.token:clear_token',
        ]
    }
)
