# imports
import pandas as pd
import datetime as dt
from datetime import date

from display import displayOptions, renderMessage
from helper import getDateRangeFromWeek, getEntriesBetween, getWeeklyData
from operations import printWeeklyData


class EditExpenses:
    def __init__(self):
        self.dataframe = pd.DataFrame()
        self.weeklyLimit = None

    def writeToCsv(self):
        '''
        Initializing csv file with an initial data 
        comment the method call if you wish to start afresh
        '''
        dates = pd.date_range('2020-08-01', '2020-09-02', periods=15)
        initialData = {
            'Date':
            list(dates),
            'Name': [
                'Pens', 'Books', 'Petrol', 'Car', 'Chips', 'food', 'burger',
                'dominos', 'McD', 'KFC', 'Bike Service', 'Friendly Loan',
                'repairs', 'tolls', 'stationaries'
            ],
            'Amount': [
                10, 20, 300, 200, 450, 120, 35, 360, 1100, 250, 1220, 5050,
                355, 230, 450
            ]
        }

        self.dataframe = pd.DataFrame(
            initialData, columns=['Date', 'Name', 'Amount'])

    def readFromFile(self):
        return str(self.dataframe)

    def addExpense(self):
        try:
            date = input('Enter the Date (dd-mm-yy): ')
            datetime_object = dt.datetime.strptime(date, '%d-%m-%y')
            name = input('Enter Name of the purchase: ')
            amount = input('Enter amount spent: ')

            newDataFrame = pd.DataFrame([[datetime_object, name, amount]],
                                        columns=['Date', 'Name', 'Amount'])
            self.dataframe = self.dataframe.append(newDataFrame)
            if self.weeklyLimit:
                if self.checkLimit(datetime_object, amount):
                    print(renderMessage('warn'))
            return (renderMessage('addEntry-success'))
        except:
            return renderMessage('input-error')

    def getWeeklyReport(self):
        numOfWeeks = int(input(renderMessage('askWeek-length')))
        today = date.today()
        startWeek = today.isocalendar()[1] - numOfWeeks + 1
        [startDate, lastDate] = getDateRangeFromWeek(today.year, startWeek)
        rangedData = getEntriesBetween(self.dataframe, startDate)
        result = printWeeklyData(numOfWeeks, startDate, today, rangedData)
        return result

    def setReminder(self):
        if self.weeklyLimit and self.weeklyLimit != 0:
            print(renderMessage('change-preset-limit', self.weeklyLimit))
            decision = input('Do you wish to update your limit ? (Y/N)\n')
            if decision and (decision == 'y' or decision == 'Y'):
                newLimit = int(input(renderMessage('setLimit-request')))
                self.setLimit(newLimit)
                return renderMessage('setLimit-success', self.weeklyLimit)
            else:
                return None
        else:
            print(renderMessage('set-new-limit'))
            decision = input('Do you wish to set a new limit ? (Y/N)\n')
            if decision and (decision == 'y' or decision == 'Y'):
                newLimit = int(input(renderMessage('setLimit-request')))
                self.setLimit(newLimit)
                return renderMessage('setLimit-success', self.weeklyLimit)
            else:
                return None

    def checkLimit(self, endDate, amount=0):
        [startDate, lastDate] = getDateRangeFromWeek(endDate.year,
                                                     endDate.isocalendar()[1])
        weeklyTotal = getWeeklyData(startDate, lastDate, self.dataframe)
        return weeklyTotal > self.weeklyLimit

    def setLimit(self, newLimit):
        self.weeklyLimit = newLimit


def renderOption(expense, choice):
    choices = {
        1: expense.addExpense,
        2: expense.readFromFile,
        3: expense.getWeeklyReport,
        4: expense.setReminder,
    }
    return choices.get(choice, None)


if __name__ == '__main__':
    editor = EditExpenses()
    editor.writeToCsv()
    exitAt = 5
    while True:
        userChoice = displayOptions()
        if userChoice == exitAt:
            print(renderMessage('exit'))
            break
        function = renderOption(editor, userChoice)
        if function != None:
            result = function()
            if result != None:
                print(result)
        else:
            print(renderMessage('error'))
