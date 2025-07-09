from setuptools import setup

APP = ['DownVid/DownVid.py']
DATA_FILES = []
OPTIONS = {
    'includes': [],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
)