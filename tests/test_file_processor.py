import unittest
from unittest.mock import patch, mock_open
from io import StringIO
from file_processor import FileProcessor 
import os
import tempfile
import pdb

class TestFileProcessor(unittest.TestCase):
  @patch('file_processor.FileReader')
  def test_successful_processing(self, mock_file_reader):
    mock_file_reader.return_value.simulate_error = False
    
    with tempfile.TemporaryDirectory() as input_folder, tempfile.TemporaryDirectory() as output_folder:
      test_input_data = """id	first_name	last_name	email	job_title	basic_salary	allowances
30462	Chaddy	Lassen	classen0@cocolog-nifty.com	Physical Therapy Assistant	7958	1502
30563	Clarine	Denerley	cdenerley1@blogger.com	Senior Developer	9024	816
30312	Christina	Geroldini	cgeroldini2@ca.gov	Occupational Therapist	5476	1252
"""         
      test_input_path = os.path.join(input_folder, "test_input.dat")
      
      with open(test_input_path, 'w') as test_input_file:
          test_input_file.write(test_input_data)

      mock_open_func = mock_open()
      
      with patch('builtins.open', mock_open_func), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        file_processor = FileProcessor(input_folder, output_folder)
        file_processor.process_files()
        
        output_file_path = os.path.join(output_folder, "output.csv")
        self.assertTrue(os.path.exists(output_file_path), "Output file should be created")

  @patch('file_processor.FileReader')
  def test_failure_processing(self, mock_file_reader):
    mock_file_reader.return_value.simulate_error = True  

    with tempfile.TemporaryDirectory() as input_folder, tempfile.TemporaryDirectory() as output_folder:
      test_input_data = """id	first_name	last_name	email	job_title	basic_salary	allowances
30462	Chaddy	Lassen	classen0@cocolog-nifty.com	Physical Therapy Assistant	7958	1502
30563	Clarine	Denerley	cdenerley1@blogger.com	Senior Developer	9024	816
30312	Christina	Geroldini	cgeroldini2@ca.gov	Occupational Therapist	5476	1252
"""
      test_input_path = os.path.join(input_folder, "test_input.dat")
      with open(test_input_path, 'w') as test_input_file:
        test_input_file.write(test_input_data)

      mock_open_func = mock_open()
      with patch('builtins.open', mock_open_func), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        file_processor = FileProcessor(input_folder, output_folder)
        file_processor.process_files()

        output_file_path = os.path.join(output_folder, "output.csv")
        self.assertFalse(os.path.exists(output_file_path), "Output file should not be created in case of failure")

if __name__ == '__main__':
  unittest.main()
