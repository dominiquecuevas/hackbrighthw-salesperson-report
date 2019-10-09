"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] # empty list of salespeople
melons_sold = [] # empty list of melons sold

f = open('sales-report.txt') # opens data txt file
for line in f:               # only unpacks 2 items in each line, 
    line = line.rstrip()        # should also unpack total amount $
    entries = line.split('|')
    salesperson = entries[0]
    melons = int(entries[2])

    if salesperson in salespeople:
        position = salespeople.index(salesperson) # returns lowest index of the item in salespeople list
        melons_sold[position] += melons           # reassigns melons_sold list every time more melons sold,
    else:                                         # doesn't differentiate between who sold the melons
        salespeople.append(salesperson)     # appends names to salespeople list
        melons_sold.append(melons)          # appends melons


for i in range(len(salespeople)):           # prints each salesperson and all melons sold including ones by different people
    print(f'{salespeople[i]} sold {melons_sold} melons')

# REFACTOR
# make a dictionary with each salesperson as a key
    # the values would be another dictionary with keys of price and count
# add to price and count for each salesperson order
# print the salesperson with their total price and count