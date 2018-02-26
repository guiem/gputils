# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gputils',
    version='1.0.5',
    description='Variety of utilities that may come handy in diverse projects. ',
    long_description=long_description,
    url='https://github.com/guiem/gputils',
    author='Guiem Bosch',
    author_email='g@guiem.info',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    #packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    py_modules=["gputils"],
    install_requires=[],
    python_requires='>=3',
    extras_require={
        # 'dev': ['check-manifest'],
        'test': ['coverage','numpy'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/guiem/gputils/issues',
        'Say Thanks!': 'https://saythanks.io/to/guiem',
        'Source': 'https://github.com/guiem/gputils/',
    },
)