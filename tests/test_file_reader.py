import unittest
from unittest.mock import patch, mock_open
from file_reader import FileReader

class TestFileReader(unittest.TestCase):
  @patch('builtins.open', new_callable=mock_open, read_data="id\tname\n1\tJohn\n2\tJane\n3\tBob\n")
  def test_read_files(self, mock_open_func):
    file_reader = FileReader("tests/test_folder")


    data = file_reader.read_files()

    self.assertEqual(len(data), 3, "Number of records should match")
    self.assertEqual(data[0]["id"], "1", "First record should match")
    self.assertEqual(data[0]["name"], "John", "First record should match")
    self.assertEqual(data[1]["id"], "2", "Second record should match")
    self.assertEqual(data[1]["name"], "Jane", "Second record should match")
    self.assertEqual(data[2]["id"], "3", "Third record should match")
    self.assertEqual(data[2]["name"], "Bob", "Third record should match")

if __name__ == '__main__':
    unittest.main()
