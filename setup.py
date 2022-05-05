from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='pysentipers',
    version='0.2',
    description='Python API for SentiPers Dataset',
    author='Javad Zarezadeh',
    author_email='jvd.zarezadeh@gmail.com',
    packages=['pysentipers'],
    url='https://github.com/javadzarezadeh/pySentiPers',
    keywords='sentipers sentiment analysis',
    license='GPLv3',
    python_requires='>=3',
    install_requires=['beautifulsoup4'],
    classifiers=[],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
