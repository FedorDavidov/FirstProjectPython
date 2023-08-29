from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['Name', 'Age', 'City']
table.add_row(['Petr', 11, 'Moscow'])
table.add_row(['Fyodor', 30, 'Tashkent'])
table.add_row(['Nastya', 31, 'Tashkent'])

print(table)