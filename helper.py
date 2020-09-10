import pandas as pd
from datetime import datetime, timedelta, date

def getDateRangeFromWeek(p_year,p_week):
    firstdayofweek = datetime.strptime(f'1-W{int(p_week )- 1}-{p_year}', "%w-W%W-%Y").date()
    lastdayofweek = firstdayofweek + timedelta(days=6.9)
    return [firstdayofweek, lastdayofweek]

def getEntriesBetween(dataframe, startDate, endDate = date.today()):
  '''
  Get all the entries from the dataframe which lies between the two dates
  '''
  endDate = pd.to_datetime(endDate)
  startDate = pd.to_datetime(startDate)

  after_start_date = dataframe['Date'] >= startDate
  before_end_date = dataframe['Date'] <= endDate
  between_two_dates = after_start_date & before_end_date
  filtered_dates = dataframe.loc[between_two_dates]
  return filtered_dates

def getWeeklyData(startDate, endDate, rangedData):
  weeklyData = getEntriesBetween(rangedData, startDate, endDate)
  weeklyTotal = 0
  for index, row in weeklyData.iterrows():
    weeklyTotal += int(row['Amount'])
  return weeklyTotal 