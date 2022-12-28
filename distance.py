#input:my_row[4,10], partner_row[4,10], my_column[4,8], my_partnercolumn[4,8]

my_row =int(input("My row:"))
my_column = int(input("My column:"))
partner_row= int(input("Partner row:"))
partner_column = int(input("Partner column:"))


#processing

distance =((my_row - partner_row)**2 + (my_column - partner_column)**2)**.05
print("Distance =%.1f" %distance)

print("The choice of partner is aprroved:" +str(distance>3))


#output: choice_of_partner

