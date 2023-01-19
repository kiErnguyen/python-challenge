# University of California Irvine School of Continuing Education
# Data Analytics & Visualization Boot Camp Module 3 Challenge
# Erik Arbelo-Nguyễn

# Importing necessary module(s).
import csv

path = '/home/kiernguyen/Desktop/python-challenge/PyBank/Resources/budget_data.csv'
file = open(path)
reader = csv.reader(file)

header = next(reader)

data = []
for row in reader:
    date = row[0]
    profit_losses = int(row[1])
    data.append([date, profit_losses])

months = []
for row in data:
    months.append(row[0])

total_profit_losses = []
for row in data:
    total_profit_losses.append(row[1])
total = sum(total_profit_losses)

monthly_change = []
for i in range(len(total_profit_losses)-1):
    monthly_change.append(total_profit_losses[i+1]-total_profit_losses[i])
average_change = round(sum(monthly_change) / (len(months) - 1), 2)

greatest_increase = max(monthly_change)
increase_month = monthly_change.index(max(monthly_change)) +1
greatest_increase_in_profits = (months[increase_month])

greatest_decrease = min(monthly_change)
decrease_month = monthly_change.index(min(monthly_change)) +1
greatest_decrease_in_profits = (months[decrease_month])

print('Financial Analysis')
print('----------')
print('Total Months: ' + str(len(months)))
print('Average Change: $' + str(average_change))
print('Greatest Increase in Profits: ' + greatest_increase_in_profits + ' ($' + str(greatest_increase) +')')
print('Greatest Decrease in Profits: ' + greatest_decrease_in_profits + ' ($' + str(greatest_decrease) +')')

analysis = '/home/kiernguyen/Desktop/python-challenge/PyBank/analysis/analysis.txt'

with open(analysis, 'w') as file:
    file.write('Financial Analysis')
    file.write('----------')
    file.write('Total Months: ' + str(len(months)))
    file.write('Average Change: $' + str(average_change))
    file.write('Greatest Increase in Profits: ' + greatest_increase_in_profits + ' ($' + str(greatest_increase) + ')')
    file.write('Greatest Decrease in Profits: ' + greatest_decrease_in_profits + ' ($' + str(greatest_decrease) + ')')