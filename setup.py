from setuptools import find_packages, setup
from dbxtest10 import __version__

setup(
    name="dbxtest10",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="Databricks Labs CICD Templates Sample Project",
    author="",
)
