from distutils.core import setup

setup(
    name='pyatomiadns',
    version='1.3',
    author='Jochen Maes',
    author_email='jochen@sejo-it.be',
    packages=['pyatomiadns',],
    url='http://pypi.python.org/pypi/pyatomiadns/',
    license='LICENSE.txt',
    description='Manage AtomiaDNS instances with python',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
)