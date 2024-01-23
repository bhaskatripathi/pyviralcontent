from setuptools import setup, find_packages
import codecs
import os

# read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
long_description = ""  # Define the variable in the outer scope

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    with codecs.open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='pyviralcontent',
    version='0.1.1',
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
    long_description=long_description,  # Use the variable
    long_description_content_type='text/x-rst' if 'pypandoc' in locals() else 'text/markdown',
    keywords='readability virality content-analysis',
    url='https://github.com/bhaskatripathi/pyviralcontent',
)
