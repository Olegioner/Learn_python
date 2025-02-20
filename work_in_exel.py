from openpyxl import load_workbook
from datetime import datetime

inv = load_workbook('C:/new/inv.xlsx', False)

sheet = inv['Лист1']
sheet.append(['1', 'Pantum', datetime.today()])

inv.save('C:/new/inv.xlsx')


