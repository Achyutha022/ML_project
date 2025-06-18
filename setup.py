from setuptools import find_packages,setup

setup(
    name='mlproject',
    version = '0.0.1'
    author='Achyutha'
    author_email='achyuthabp@gmail.com'
    packages = find_packages()
    install_requires = ['pandas','numpy','seaborn']
)