import csv
# Create list of items to set durability to not unbreakable, and set everything else to unbreakable
# Create a list of changes to weapons so I can easily change the list

with open('Tables\\NightmareModules\\Items\\ItemTable.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    data = [row for row in csv_reader]
print(data)