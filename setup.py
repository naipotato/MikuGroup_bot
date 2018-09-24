from setuptools import setup

setup(
    name = 'animuxbot',
    version = '0.5.0',
    packages = ['animuxbot'],
    author = 'nahuelwexd',
    entry_points = {
        'console_scripts': [
            'animuxbot = animuxbot.__main__:main'
        ]
    }
)
