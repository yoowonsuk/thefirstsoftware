#gspread package
#search google api console => create project => enable apis and services => google drive api => create credential (application data) => Project & Editor
#Service Accounts => Keys => ADD KEY => CREATE new key => JSON
#menu => APIs and services => enable apis and services again => google sheets api
#client_email to googlesheets share

import gspread
import re
gc = gspread.service_Account('secrets.json')
spreadsheet = gc.open('weather_price') #name of googlesheet
# Get a worksheet by index
worksheet1 = spreadsheet.get_worksheet(0)

# Get a worksheey by name
worksheet1 = spreadsheet.worksheet('2013')
data = worksheet1.get_all_records()
print(data[10])

# Get a row or rows by cells
data = worksheet1.get_values('A5:E5')
print(data) # list of list [[ ]]

data = worksheet1.get_values('A5:F7')
print(data) # list of list [[ ]]

# Get a row by index
rows = worksheet1.row_values(3)

# Get a column by index
column = worksheet1.col_values(2)[1:]

# Get cell
data = worksheet1.get_values('D5')[0][0]
# Get cell using acell
data = worksheet1.acell('D5').value
# Search for a cell
data = worhsheet1.find('-10')
print(data.row, data.col)

# Search for many cells
data = worksheet1.findall('-9')
for cell in data:
    print(cell.row, cell.col)

# Search for partial matches
reg = re.compile(r'99')
data = worksheet1.findall(reg)


# Update a cell
worksheet1.update('E5', -29)
# Update a cell based on row-column
worksheet1.update_cell(5, 5, -39)

existing_column = worksheet1.get_value('E2:E25')
#print(existing_column)
new_column = [[round(float(i[0]) * 9/5 + 32)] for i in existing_column]
#print(new_column)
#worksheet1.update('E2:E25', new_column)
worksheet1.update('G1:G25', [['Fahreheit']] + new_column)

# Exercise!

import statistics
statistics.mean([1,2,3])


existing_column = worksheet1.get_value('G2:G25')

# Flatten the existing column
existing_column = [float(i[0]) for i in existing_column]

# Calculate average and add to Worksheet
average = statistics.mean(existing_column)
worksheet1.update('G26', average)

import time
worksheet2 = spreadsheet.worksheet('Watch')

while True:
    value1 = worksheet1.acell('G26').value
    print(value1, type(value1))
    time.sleep(2)
    value2 = worksheet1.acell('G26').value
    if value1 != value2:
        worksheet2.update('A1', 'CHANGED')

