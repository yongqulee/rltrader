from setuptools import find_namespace_packages, setup

setup(
    name='rltrader',
    version='3.2.1',
    description='Quantylab Reinforcement Learning for Stock Trading',
    author='YQLEE',
    # author_email='quantylab@gmail.com',
    # url='https://github.com/quantylab/rltrader',
    packages=find_namespace_packages(where='src', include=['quantylab.*']),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'mplfinance',
        'tqdm',
        'scikit-learn',
        'tensorflow==2.16.0',
        'torch==2.2.0',
    ]
)
