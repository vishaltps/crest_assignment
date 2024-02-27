import csv
import os

class CSVWriter:
  def __init__(self, output_folder):
    self.output_folder = os.path.expanduser(output_folder)

  def write_csv(self, processed_data, second_highest_salary, average_salary):
    output_filepath = os.path.join(self.output_folder, "output.csv")
    if processed_data:
      fieldnames = list(processed_data[0].keys())

      with open(output_filepath, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(processed_data)

        writer.writerow({field: '' for field in fieldnames})
        footer_writer = csv.writer(file)
        footer_writer.writerow([f"Second Highest Salary={second_highest_salary}", f"Average Salary={average_salary}"])
    else:
      print("No data to write to the CSV file.")

      