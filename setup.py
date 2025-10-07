from setuptools import setup
from Cython.Build import cythonize

setup(
    name="fast_common",
    ext_modules=cythonize("fast_common.pyx", compiler_directives={'language_level': "3"}),
)

