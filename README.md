# BoilerTest - Python Test File Generator (CLI Application)

BoilerTest is a command-line interface (CLI) utility packaged and available on PyPI, which serves the purpose of automatically generating test files for Python classes and standalone functions. It is designed to streamline the process of creating boilerplate testing code, allowing developers to focus on writing specific test cases.

## Key Features

- **CLI-Based**: Accessible directly from the command line, ideal for integrating into development workflows.
- **Package Installation**: Easily installable via `pip` from the Python Package Index (PyPI).
- **Automatic Test File Creation**: Analyzes Python files or directories and generates test files with unittest structures.
- **Directory Support**: Capable of processing a directory containing multiple `.py` files, creating corresponding test files for each.
- **Customizable Test Directory**: Users can specify the directory where the test files should be created.
- **Comprehensive Error Handling**: Provides clear error messages if target files or directories are not found.

## Installation

BoilerTest can be installed using `pip`:

```bash
pip install BoilerTest
```

## Usage

Once installed, you can use BoilerTest as a CLI application. Here's how you can generate test files:

```bash
boilertest -f <path_to_python_file_or_directory> -t <path_to_test_folder> [-d]
```

- `-f` specifies the path to the Python file or directory to generate tests for.
- `-t` specifies the path to the folder where the test file will be created.
- `-d` is an optional flag to indicate that the provided file path is a directory.

## Example

To generate a test file for `example.py` located in the `src` directory and place the test file in the `tests` directory, the command would be:

```bash
boilertest -f src/example.py -t tests
```

## Generated Test File Example

Here is how a test file would look after running BoilerTest on a simple `Calculator` class:

### Input Python Class

```python
class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.

    Attributes:
        total (int): The current total held by the calculator.
    """

    def __init__(self):
        """
        Initializes the calculator with a total of 0.
        """
        self.total = 0

    def add(self, a, b):
        """
        Adds two numbers and updates the total.

        Parameters:
            a (int): The first number to add.
            b (int): The second number to add.

        Returns:
            int: The sum of a and b.
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtracts one number from another and updates the total.

        Parameters:
            a (int): The number to be subtracted from.
            b (int): The number to subtract.

        Returns:
            int: The result of the subtraction.
        """
        return a - b
```

### Output Test Boilerplate

```python
import unittest

class TestCalculator(unittest.TestCase):
    """
    Test methods for the Calculator class.
    """

    def setUp(self):
        """
        Set up method to prepare the test fixture before each test method.
        """
        self.calculator = Calculator()

    def test_add(self):
        """
        Adds two numbers and updates the total.

        Parameters:
            a (int): The first number to add.
            b (int): The second number to add.

        Returns:
            int: The sum of a and b.
        """
        # TODO: Add test logic for add here
        # Example: self.assertEqual(self.calculator.add(a, b), expected_result)
        pass

    def test_subtract(self):
        """
        Subtracts one number from another and updates the total.

        Parameters:
            a (int): The number to be subtracted from.
            b (int): The number to subtract.

        Returns:
            int: The result of the subtraction.
        """
        # TODO: Add test logic for subtract here
        # Example: self.assertEqual(self.calculator.subtract(a, b), expected_result)
        pass

if __name__ == '__main__':
    unittest.main()
```

## Package Details

- **Version**: 1.0.4
- **License**: MIT License
- **Supported Python Versions**: Python 3.8, 3.9, and above.

The source code is available on GitHub, and contributions or bug reports can be made through the repository's issue tracker.

## Developer Notes

- The `BoilerTest` class can be customized to suit different test templates or testing frameworks.
- The `generate_test_method` function within the class can be tailored to include more complex test scenarios or test setups.

## Packaging and Distribution

This application is packaged using `setuptools`, making it straightforward to distribute and install. The `setup.py` script includes all the necessary metadata
