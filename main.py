from exceptions import GlobalExceptionHandler
from file_processor.file_processor import FileProcessor

def main():
  try:
    input_folder = "./"
    output_folder = "~/Desktop/Crest-Output/"

    file_processor = FileProcessor(input_folder, output_folder)
    file_processor.process_files()
  except Exception as e:
    GlobalExceptionHandler.handle_exception(e)
    print(f"File processing failed. Error: {e}")

if __name__ == "__main__":
    main()
