def get_name():
  """Prompt the user to enter the name of a new budget and return it."""
  name_input = input('Enter the name of your new budget: ')
  return name_input.strip()

def get_total_amount():
  """Prompt the user to enter the total amount to divide and return it as a float."""
  while True:
    amount_input = input('Enter the total amount you want to divide: ')
    try:
      amount = float(amount_input)
      return amount
    except ValueError:
      print('Invalid entry, use only numbers and fractions.')

def slice_making():
  """Prompt the user to enter slice names separated by commas and return a list of cleaned slice
  names."""
  raw_slices = input('Enter the name of the slices divided by a coma: ')
  splitting_slices = raw_slices.split(',')
  splitted_slices = []
  
  for slice in splitting_slices:
    splitted_slices.append(slice.strip())
  return splitted_slices

def percentage_definition(slices):
  """Prompt the user to define percentages for each slice and return a list of percentages
  as decimals for calculation."""
  percentages = []
  while True:
    for slice in slices:
      percentage = input(f'What\'s the percentage for {slice} (only whole numbers): ')
      try:
        percentage = int(percentage) * 0.01
        percentages.append(percentage)
      except ValueError:
        print('Invalid input. Please enter a valid number.')
        return percentage_definition(slices)
    
    if sum(percentages) > 1:
      print(f'Your percentages surpass 100%, try again. ({sum(percentages) * 100}%)')
      percentage_definition(slices)
    elif sum(percentages) < 1:
      percent_total = sum(percentages)
      remaining_percent = float(1 - percent_total) * 100
      print(f'Your percentages do not get to a 100%, you\'re leaving {remaining_percent:.2f}% behind.')
      percentage_definition(slices)
    
    return percentages

def calculate_amounts(amount, slices, percentages):
  """Calculate and return a dictionary mapping slices to their respective amounts based on
  percentages."""
  slices_with_amounts = {}

  for slice, percentage in zip(slices, percentages):
    slice_amount = amount * percentage
    slice_amount = float(slice_amount)
    slices_with_amounts[slice] = slice_amount

  return slices_with_amounts

def print_budget(budget_data):
  print('\n----------Budget information----------\n')
  print(f'Budget name: {budget_data["Budget name"]}')
  print(f'Total amount: ${budget_data["Total amount"]}')
  print('\nSlices:')
  for slice, amount in budget_data['Division'].items():
    print(f'{slice}: ${amount:,}')
  print('\n--------------------------------------\n')

def confirmation():
  while True:
    selection = input('Enter Y/y for yes or N/n for no: ')

    if selection.lower() == 'y':
      return True
    elif selection.lower() == 'n':
      return False
    else:
      print('Invalid input.')