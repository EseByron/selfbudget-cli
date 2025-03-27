# MODULES

import json
import secondary_functions
import os

# MAIN FUNCTIONS

def new_budget():
  """
  Creates a new budget by gathering user input for the budget name, total amount, 
  categories, and their percentages. Calculates amounts for each category and 
  optionally saves the data to a JSON file.

  Returns:
    None
  """
  budget_name = secondary_functions.get_name()
  amount = secondary_functions.get_total_amount()
  slices = secondary_functions.slice_making()
  percentages = secondary_functions.percentage_definition(slices)
  slices_with_amounts = secondary_functions.calculate_amounts(amount, slices, percentages)
  budget_data = {
    'Budget name': budget_name,
    'Total amount': amount,
    'Division': slices_with_amounts,
  }

  """Printing the last made budget info."""
  secondary_functions.print_budget(budget_data)

  print('Would you like to save a .json file with this information?')
  if secondary_functions.confirmation():
    file_name = input('Name your file: ')
    with open(f'{file_name}.json', 'w') as budget_file:
      json.dump(budget_data, budget_file, indent=4)
    print(f'Your budget has been saved as "{file_name}.json\n')
  else:
    return budget_data

def load_budget():
  """
  Prompts the user to load a budget file in JSON format, handles file not found errors, 
  and displays the loaded budget details.

  Returns:
    dict: The loaded budget data if the file is successfully found and parsed.
  """
  while True:
    budget_selection = input('Enter the name of the budget file you want to load: ')
    try:
      with open(f'{budget_selection}.json') as budget_file:
        loaded_budget = json.load(budget_file)
    except FileNotFoundError:
      print(f'The file {budget_selection}.json was not found, try again.')
    else:
      secondary_functions.print_budget(loaded_budget)
      return loaded_budget

def delete_budget():
  while True:
    budget_selection = input('Enter the name of the budget file your want to delete: ')
    file_path = f'{budget_selection}.json'

    if os.path.exists(file_path):
      print(f'You sure you want to delete {file_path}?')
      if secondary_functions.confirmation():
        os.remove(file_path)
        print(f'{file_path} has been deleted.\n')
        return
      else:
        print('Deletion canceled.')
        return
    else:
      print(f'The file {file_path} doesn\'t exists.')
      return
       


# WORKFLOW

welcome_message = '\n Hello, welcome to the budget calculator by EseByron.\n'
print(welcome_message)

while True:
  main_menu = 'MAIN MENU:\n' \
  '1) New budget\n' \
  '2) Load budget\n' \
  '3) Delete budget\n' \
  '4) Edit budget\n' \
  '0) Exit program'
  print(main_menu)
  loaded_budget = ''
  if loaded_budget:
    print(f'Loaded budget: {loaded_budget}')

  selection = input('Select an option: ')
  if selection == '1':
    loaded_budget = new_budget()
  elif selection == '2':
    loaded_budget = load_budget()
  elif selection == '3':
    delete_budget()
  elif selection == '0':
    break
  