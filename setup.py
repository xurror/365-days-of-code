try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Year of Code',
    'author': 'Yemdjih Kaze Nasser',
    'url': 'null',
    'download_url': 'null',
    'author_email': 'kaze.nasser@outlook.com',
    'version': '0.1',
    'install_requires': ['pygame'],
    'packages': ['projects/Numbers'],
    'scripts': [],
    'name': 'Year of Code'
}

setup(**config)