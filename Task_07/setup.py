from setuptools import setup, find_packages

with open("README.MD","r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="DB_Integration",
    version="0.0.1",
    author="Victor Yazigi",
    description="Test integration using MongoDB and SQL",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oyazigi/super-duper-octo-funicular/tree/main/Task_07",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>3.6',
)