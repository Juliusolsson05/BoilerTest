import ast
import os


class TestFileGenerator:

    """
    A TestFileGenerator class is a utility for automatically creating a testing script for a given Python file.
    It scans the target Python file, identifies the classes and methods, and creates a testing file where each method has a corresponding test method.

    Attributes:
        python_file (str): Path to the Python file to generate tests for.
        test_file_folder (str): Path to the folder to create the test file in.
        classes (dict): Stores class names and their respective test methods.
        functions (str): Stores the test methods for functions that are not defined inside a class.
    """

    def __init__(self, python_file, test_file_folder, is_directory=False):
        """
        The constructor for TestFileGenerator class.

        Parameters:
            python_file (str): Path to the Python file or directory to generate tests for.
            test_file_folder (str): Path to the folder to create the test file in.
            is_directory (bool): If True, python_file will be treated as a directory. Defaults to False.
        """
        self.python_file = python_file
        self.test_file_folder = test_file_folder
        self.classes = {}
        self.functions = ""
        self.is_directory = is_directory
        self.files = []

        # If the provided path is a directory, get all Python files in it
        if self.is_directory:
            if not os.path.isdir(self.python_file):
                raise ValueError(f"{self.python_file} is not a directory.")
            self.files = [os.path.join(self.python_file, f) for f in os.listdir(self.python_file) if f.endswith(".py")]
        else:
            self.files = [self.python_file]


    def extract_class_methods(self):
        """
        Extract the class names and methods from the Python file.
        """

        self.classes = {}
        self.functions = ""

        try:
            with open(self.python_file, "r") as source:
                tree = ast.parse(source.read())
                for node in tree.body:
                    if isinstance(node, ast.ClassDef):
                        class_name = node.name  # Extract the class name
                        self.classes[class_name] = ""
                        for func in node.body:
                            if isinstance(func, ast.FunctionDef):
                                self.classes[class_name] += self.generate_test_method(
                                    func)
                    elif isinstance(node, ast.FunctionDef):
                        self.functions += self.generate_test_method(
                            node, is_class_method=False)
        except FileNotFoundError:
            print(f"The file {self.python_file} does not exist.")
            return False
        return True

    def generate_test_method(self, func, is_class_method=True):
        """
        Generate a test method for the given function.

        Parameters:
            func (ast.FunctionDef): The function node.
            is_class_method (bool): True if the function is a method inside a class, False otherwise.

        Returns:
            str: The generated test method.
        """

        method_name = func.name
        parameters = ", ".join(
            arg.arg for arg in func.args.args) if func.args.args else ""
        method_prefix = "test_" if is_class_method else "test_func_"
        docstring = ast.get_docstring(func) if ast.get_docstring(
            func) else f"Test {method_name}"
        return f'\n    def {method_prefix}{method_name}(self):' \
               f'\n        """{docstring}"""' \
               f'\n        # TODO: Add test logic for {method_name} here' \
               f'\n        # Example: self.assertEqual({method_name}({parameters}), expected_result)' \
               f'\n        pass\n\n'

    def generate_test_file(self):
        """
        Generate test files with the boilerplate and the extracted class methods for all Python files.
        """

        for python_file in self.files:
            self.python_file = python_file  # Update current file
            if not self.extract_class_methods():
                continue

            base_name = os.path.basename(self.python_file).replace(".py", "")
            test_file_path = os.path.join(self.test_file_folder, f"{base_name}_testing.py")

            try:
                os.makedirs(self.test_file_folder, exist_ok=True)

                with open(test_file_path, "w") as test_file:
                    for class_name, test_methods in self.classes.items():
                        test_boilerplate = f'''
import unittest

class Test{class_name}(unittest.TestCase):

    {test_methods}

if __name__ == '__main__':
    unittest.main()
    '''
                        test_file.write(test_boilerplate)

                    if self.functions:
                        test_file.write(f'''
    import unittest

    class TestFunctions(unittest.TestCase):

    {self.functions}

    if __name__ == '__main__':
        unittest.main()
    ''')
            except FileNotFoundError:
                print(f"The folder {self.test_file_folder} does not exist.")
                return

            print(f"Test file created at {test_file_path}")


if __name__ == "__main__":
    generator = TestFileGenerator("src/main", "tests", is_directory=True)
    generator.generate_test_file()