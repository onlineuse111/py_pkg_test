
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    description='My git test project',
    author= 'Online Use',
    url= 'URL to get it at.',
    download_url= 'Where to download it.',
    author_email= 'onlineuse11@yahoo.com`',
    install_requires= ['nose'],
    packages= ['ram_test'],
    scripts= ['bin/ram_test'],
    name= 'test_git_name'
)
