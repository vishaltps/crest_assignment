import unittest
from file_processor.csv_writer import CSVWriter
import os
import tempfile
import csv

class TestCSVWriter(unittest.TestCase):
  def setUp(self):
    self.output_folder = tempfile.mkdtemp()
    self.csv_writer = CSVWriter(self.output_folder)

  def test_write_csv(self):
    processed_data = [
        {'id': '30462', 'first_name': 'Chaddy', 'last_name': 'Lassen', 'email': 'classen0@cocolog-nifty.com', 'job_title': 'Physical Therapy Assistant', 'basic_salary': '7958', 'allowances': '1502'},
        {'id': '30563', 'first_name': 'Clarine', 'last_name': 'Denerley', 'email': 'cdenerley1@blogger.com', 'job_title': 'Senior Developer', 'basic_salary': '9024', 'allowances': '816'}
    ]

    second_highest_salary = 9460.0
    average_salary = 9650.0

    self.csv_writer.write_csv(processed_data, second_highest_salary, average_salary)

    output_filepath = os.path.join(self.output_folder, "output.csv")
    self.assertTrue(os.path.exists(output_filepath), "Output file should be created")

    with open(output_filepath, 'r') as file:
      reader = csv.reader(file)
      rows = list(reader)

      self.assertEqual(rows[0], ['id', 'first_name', 'last_name', 'email', 'job_title', 'basic_salary', 'allowances'])

      self.assertEqual(rows[1], ['30462', 'Chaddy', 'Lassen', 'classen0@cocolog-nifty.com', 'Physical Therapy Assistant', '7958', '1502'])
      self.assertEqual(rows[2], ['30563', 'Clarine', 'Denerley', 'cdenerley1@blogger.com', 'Senior Developer', '9024', '816'])

      self.assertEqual(rows[3], ['', '', '', '', '', '', ''])
      self.assertEqual(rows[4], [f"Second Highest Salary={second_highest_salary}", f"Average Salary={average_salary}"])

if __name__ == '__main__':
    unittest.main()
