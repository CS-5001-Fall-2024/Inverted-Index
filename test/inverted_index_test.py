import os
import unittest
import subprocess
import pycodestyle
import shutil

PYTHON_FILE_NAME = 'inverted_index.py'

def execute_program(input, output):
    command = ['python3', PYTHON_FILE_NAME, '-input', input, '-output', output]
    subprocess.run(command)

def remove_leading_trailing_blank_lines(list):
    while not list[0].strip():
        list.pop(0)
        print('Removing leading blank lines.')
    while not list[len(list)-1].strip():
        list.pop()
        print('Removing trailing blank lines.')
    return list

def compare_files(expected_file, actual_file):
    line = 1
    with open(expected_file) as expected, open(actual_file) as actual:
        expected_lines = expected.readlines()
        expected_lines = remove_leading_trailing_blank_lines(expected_lines)

        actual_lines = actual.readlines()
        actual_lines = remove_leading_trailing_blank_lines(actual_lines)

        if len(expected_lines) != len(actual_lines): 
            print(f'Compare: {expected_file} and {actual_file}')           
            print(f'Expected {len(expected_lines)} and actual {len(actual_lines)} do not contain the same number of lines')
            # return False
        for line1, line2 in zip(expected_lines, actual_lines):
            if line1.strip() != line2.strip():
                print(f'Comparing...{expected_file} and {actual_file}')           
                print(f'Mismatch at line {line}')    
                return False
            line += 1

    return True
    

def compare(expected_dir, actual_dir):
    files = ['index.txt', 'inverted_index.txt', 'scores.txt']
    for file in files:
        if not compare_files(
            os.path.join(expected_dir, file),
            os.path.join(actual_dir, file),):
            return False
    return True


def clean_actual_dir(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)


class TestInvertedIndex(unittest.TestCase):

    def test_short_texts(self):
        clean_actual_dir('short_texts_actual')
        execute_program('short_texts', 'short_texts_actual')
        self.assertTrue(compare('short_texts_expected', 'short_texts_actual'))


    def test_full_texts(self):
        clean_actual_dir('full_texts_actual')
        execute_program('full_texts', 'full_texts_actual')
        self.assertTrue(compare('full_texts_expected', 'full_texts_actual'))


    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(['inverted_index.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")