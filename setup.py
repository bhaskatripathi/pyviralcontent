from setuptools import setup, find_packages
import codecs
import os

# read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyviralcontent',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'pandas', 
        'numpy', 
        'matplotlib', 
        'seaborn'
    ],
    author='Bhaskar Tripathi',
    author_email='bhaskar.tripathi@gmail.com',
    description='A package for analyzing content readability and virality potential.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='readability virality content-analysis',
    url='https://github.com/bhaskatripathi/pyviralcontent',
)
