from PyTestGen import PyTestGen
import argparse


def main():
    parser = argparse.ArgumentParser(description="Generate test files for Python classes.")
    parser.add_argument("-f", "--file", type=str, help="Path to the Python file or directory to generate tests for.")
    parser.add_argument("-t", "--testfolder", type=str, help="Path to the folder to create the test file in.")
    parser.add_argument("-d", "--is_directory", action='store_true', help="Set this flag if the file path is a directory.")

    args = parser.parse_args()

    generator = PyTestGen(args.file, args.testfolder, args.is_directory)
    generator.generate_test_file()