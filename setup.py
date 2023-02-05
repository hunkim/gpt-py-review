from setuptools import setup, find_packages

setup(
    name='gpt-py-review',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'gpt-py-review=gpt_py_review.extract:main',
        ],
    }
)
