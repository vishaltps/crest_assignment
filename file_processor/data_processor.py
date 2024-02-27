class DataProcessor:
  def process_data(self, data):
    unique_data = [dict(t) for t in {tuple(d.items()) for d in data}]

    for entry in unique_data:
      entry['Gross Salary'] = float(entry['basic_salary']) + float(entry['allowances'])

    salaries = [float(entry['Gross Salary']) for entry in unique_data]
    sorted_salaries = sorted(set(salaries), reverse=True)
    second_highest_salary = sorted_salaries[1] if len(sorted_salaries) > 1 else None
    average_salary = sum(salaries) / len(salaries) if salaries else None

    return unique_data, second_highest_salary, average_salary
