from setuptools import find_packages, setup

setup(
    name="chapter4",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["pytest"],
)
