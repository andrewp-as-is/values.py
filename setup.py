import setuptools

setuptools.setup(
    name='values',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
