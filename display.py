
def displayOptions():
  print('\nChoose your option')
  return int(input('1: Add an expenditure 2: Show All Data 3: Get Weekly Reports 4: Set Weekly Reminder 5: Exit \n'))

def renderMessage(status, data = None):
  renderOptions = {
    'error': 'You have made an invalid selection. Please choose a correct option \n',

    'exit': 'Exiting application \n',

    'askWeek-length': 'Enter the number of weeks for which you wish to get the data for: ',

    'input-error': 'Something went wrong. Please stick to the format',

    'change-preset-limit':  f'Your currently set weekly limit is {data}',

    'set-new-limit': 'You do not have a limit set.\n',

    'setLimit-success': f'Limit set to {data} successfully \n',

    'setLimit-request': 'Please set your new Limit',

    'addEntry-success': 'Entry added successfully\n ',

    'warn' : '\n Warning!: Your weekly limit has been surpassed.'

  }
  
  return renderOptions.get(status, None)