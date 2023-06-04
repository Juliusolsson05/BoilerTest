from setuptools import setup

setup(
    name="BoilerTest",
    version="1.0.3",
    description="Python test file generator",
    long_description="A utility for automatically creating test files for Python classes",
    author="Julius Olsson",
    author_email="julius.olsson05@gmail.com",
    url="https://github.com/Juliusolsson05/BoilerTest.git",
    packages=["BoilerTest"],
    entry_points={
        "console_scripts": [
            "boilertest=BoilerTest.main:main",
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
