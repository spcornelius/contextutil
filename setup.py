from setuptools import setup
import os


pkg_name = 'contextutil'
url = 'https://github.com/spcornelius/' + pkg_name
license = 'GPLv3'
version = '0.1.1'

classifiers = [
    "Development Status :: 3 - Alpha",
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: OS Independent',
]


def _path_under_setup(*args):
    return os.path.join(os.path.dirname(__file__), *args)


_author, _author_email = open(_path_under_setup('AUTHORS'), 'rt').readline().split('<')

setup_kwargs = dict(
    name=pkg_name,
    version=version,
    description="Some handy Python context managers",
    classifiers=classifiers,
    author=_author,
    author_email=_author_email.split('>')[0].strip(),
    url=url,
    license=license,
    packages=[pkg_name]
)

if __name__ == '__main__':
    setup(**setup_kwargs)
