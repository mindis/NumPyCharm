from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='NumPyCharm',
    version='',
    packages=[''],
    url='',
    license='',
    author='yoavram',
    author_email='',
    description='',
    ext_modules = cythonize("primes.pyx")
)
