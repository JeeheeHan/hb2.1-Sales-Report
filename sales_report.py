"""Generate sales report showing total melons each salesperson sold."""

#local variables for list of sales names and melons sold
salespeople = []
melons_sold = []

f = open('sales-report.txt')  #Open the file by directly adding in the address
for line in f:    #For loop of every unbroken down line in the sale-report.txt

    line = line.rstrip()   #list of lines stripped by spaces
    entries = line.split('|')    #list seperated by "|"

    salesperson = entries[0]    #Indexing in the list entries but only return 1 thing despite in the for loop
    melons = int(entries[2])     #Converting into integer for item in entries just 1 time       

    if salesperson in salespeople: 
    #Poor if statement that is repetitive and just checked to that 1 var in list cause the for loop wasn't used properly
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

#Will print just 1 statement as the file was not fully read
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
