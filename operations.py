from helper import getDateRangeFromWeek, getEntriesBetween

def getWeeklyData(startDate, endDate, rangedData):
  weeklyData = getEntriesBetween(rangedData, startDate, endDate)
  weeklyTotal = 0
  print(f'Report from {startDate} to {endDate}')
  for index, row in weeklyData.iterrows():
    print(row['Date'], row['Name'], row['Amount'])
    weeklyTotal += int(row['Amount'])
  print(f'The Weekly total for this week is {weeklyTotal}\n') 
  return weeklyTotal 


def printWeeklyData(numOfWeeks, startDate, endDate, rangedData):
  '''
  Function to return the sliced data in a formatted manner
  '''
  print(f'\n Displaying report from Date {startDate} to {endDate}\n')
  weekCounter = numOfWeeks
  while True:
    year = endDate.year
    week = endDate.isocalendar()[1] - weekCounter + 1
    if weekCounter == 0:
      break
    else:
      [ weekStartDate, weekEndDate ] = getDateRangeFromWeek(year, week)
      getWeeklyData(weekStartDate, weekEndDate, rangedData)
      
    weekCounter -= 1
  return 'Report printed succesfully'