from setuptools import setup

setup(
    name = 'animuxbot',
    version = '0.6.0',
    packages = ['animuxbot'],
    author = 'nahuelwexd',
    license = 'GPL-3.0'
    entry_points = {
        'console_scripts': [
            'animuxbot = animuxbot.__main__:main'
        ]
    }
)
