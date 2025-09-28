from prettytable import PrettyTable

my_table = PrettyTable()

my_table.add_column("Name", ["Messi", "Neymar", "Ronaldo", "Beckham"])
my_table.add_column("Age", [19, 18, 21, 27])
print(my_table)
