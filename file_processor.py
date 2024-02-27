from exceptions import GlobalExceptionHandler
from file_reader import FileReader
from data_processor import DataProcessor
from csv_writer import CSVWriter

class FileProcessor:
  def __init__(self, input_folder, output_folder):
    self.file_reader = FileReader(input_folder)
    self.data_processor = DataProcessor()
    self.csv_writer = CSVWriter(output_folder)

  def process_files(self):
    try:
      data = self.file_reader.read_files()

      processed_data, second_highest_salary, average_salary = self.data_processor.process_data(data)

      self.csv_writer.write_csv(processed_data, second_highest_salary, average_salary)
      print("File processing completed successfully.")
    except Exception as e:
      GlobalExceptionHandler.handle_exception(e)
      print(f"File processing failed. Error: {e}")


if __name__ == "__main__":
  input_folder = "./"
  output_folder = "~/Desktop/Crest-Output/"

  file_processor = FileProcessor(input_folder, output_folder)
  file_processor.process_files()