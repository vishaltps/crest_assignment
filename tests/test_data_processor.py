import unittest
from data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
  def setUp(self):
    self.data_processor = DataProcessor()

  def test_process_data(self):
    sample_data = [
        {'id': '30462', 'first_name': 'Chaddy', 'last_name': 'Lassen', 'email': 'classen0@cocolog-nifty.com', 'job_title': 'Physical Therapy Assistant', 'basic_salary': '7958', 'allowances': '1502'},
        {'id': '30563', 'first_name': 'Clarine', 'last_name': 'Denerley', 'email': 'cdenerley1@blogger.com', 'job_title': 'Senior Developer', 'basic_salary': '9024', 'allowances': '816'}
    ]

    unique_data, second_highest_salary, average_salary = self.data_processor.process_data(sample_data)

    self.assertEqual(len(unique_data), 2) 
    self.assertEqual(unique_data[0]['Gross Salary'], 9460.0)
    self.assertEqual(unique_data[1]['Gross Salary'], 9840.0)
    self.assertEqual(second_highest_salary, 9460.0)
    self.assertEqual(average_salary, 9650.0)


  def test_process_data_with_duplicates(self):
    sample_data = [
        {'id': '30462', 'first_name': 'Chaddy', 'last_name': 'Lassen', 'email': 'classen0@cocolog-nifty.com', 'job_title': 'Physical Therapy Assistant', 'basic_salary': '7958', 'allowances': '1502'},
        {'id': '30462', 'first_name': 'Chaddy', 'last_name': 'Lassen', 'email': 'classen0@cocolog-nifty.com', 'job_title': 'Physical Therapy Assistant', 'basic_salary': '7958', 'allowances': '1502'},  # Duplicate entry
        {'id': '30563', 'first_name': 'Clarine', 'last_name': 'Denerley', 'email': 'cdenerley1@blogger.com', 'job_title': 'Senior Developer', 'basic_salary': '9024', 'allowances': '816'}
    ]

    unique_data, _, _ = self.data_processor.process_data(sample_data)

    self.assertEqual(len(unique_data), 2) 

if __name__ == '__main__':
    unittest.main()
