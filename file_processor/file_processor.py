from file_processor.file_reader import FileReader
from file_processor.data_processor import DataProcessor
from file_processor.csv_writer import CSVWriter

class FileProcessor:
  def __init__(self, input_folder, output_folder):
    self.file_reader = FileReader(input_folder)
    self.data_processor = DataProcessor()
    self.csv_writer = CSVWriter(output_folder)

  def process_files(self):
    data = self.file_reader.read_files()

    processed_data, second_highest_salary, average_salary = self.data_processor.process_data(data)

    self.csv_writer.write_csv(processed_data, second_highest_salary, average_salary)
    print("File processing completed successfully.")
    