try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='c3pyo',
    version='0.0.3',
    description="Python C3 - Chart Library for d3.js",
    keywords=['plot, graph, c3, d3', 'data', 'visualization'],
    author='Ben Keen',
    author_email='bak@benalexkeen.com',
    url='http://github.com/benalexkeen/C3PyO',
    license="MIT",
    test_suite='tests/',
    packages=[
        'c3pyo',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Jinja2>=2.8'
    ],
)

