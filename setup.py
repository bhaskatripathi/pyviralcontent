from setuptools import setup, find_packages

setup(
    name='pyviralcontent',
    version='0.1.0',
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
    keywords='readability virality content-analysis'
)
