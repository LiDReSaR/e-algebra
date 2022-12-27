import setuptools

import ealgebra

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='e-algebra',
    version=ealgebra.__version__,
    scripts=[],
    author='Yahor Shyshkin',
    author_email='lidresar@gmail.com',
    description='Elementary Algebra Algorithms',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/LiDReSaR/algebra',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
