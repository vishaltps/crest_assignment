import os
import csv

class FileReader:
  def __init__(self, folder_path):
    self.folder_path = folder_path

  def read_files(self):
    data = []
    for filename in os.listdir(self.folder_path):
      if filename.endswith(".dat"):
        with open(os.path.join(self.folder_path, filename), 'r') as file:
          reader = csv.DictReader(file, delimiter='\t')
          data.extend(reader)

    return data
