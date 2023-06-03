from setuptools import setup

setup(
    name="PyTestGen",
    version="1.0.0",
    description="Python test file generator",
    long_description="A utility for automatically creating test files for Python classes",
    author="Julius Olsson",
    author_email="julius.olsson05@gmail.com",
    url="https://github.com/Juliusolsson05/PyTestGen.git",
    packages=["PyTestGen"],
    entry_points={
        "console_scripts": [
            "pytestgen=PyTestGen.main:main",
        ],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.8",
)
