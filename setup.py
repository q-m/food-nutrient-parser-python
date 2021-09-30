from setuptools import setup, find_packages
#from nutrients_parser.version import VERSION

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='nutrients_parser',
    version='0.0.1',
    #url='https://github.com/q-m/nutrients-parser-python',
    author='wvengen',
    author_email='willem@thequestionmark.org',
    description='Extracts structured nutritional information from HTML.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Dutch',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],

    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3',

    install_requires=[
        "lxml>=4.5.0",
        "jsonpath-ng>=1.5.0",
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
