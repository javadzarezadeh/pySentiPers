from setuptools import setup

setup(
    name='pysentipers',
    version='0.1',
    description='Python API for SentiPers Dataset',
    author='Javad Zarezadeh',
    author_email='jayzee1992@gmail.com',
    url='https://github.com/jayzee1992/pySentiPers',
    keywords='sentiptwine upload dist/*ers sentiment analysis',
    license='GPLv3',
    scripts=['pySentiPers.py'],
    python_requires='>=3',
    install_requires=['beautifulsoup4']
)
