
cup_of_coffee = int(input ("How mnay cups of coffee?"))
number_of_cream = int(input("How many number of cream?"))
number_of_sugar = int(input ("How many spoons of sugar?"))
tips = float(input("How much tips(%)?"))

sub_total = cup_of_coffee (*2.5 + number_of_cream *0.75 + number_of_sugar *0.25)

tips_amount = sub_total * tips /100
tax_amount =sub_total *13 /100
total = sub_total + tips_amount + tax_amount

print("sub_total: %.2f" %sub_total)
print("Taqxes: %.2f" %tax_amount)
print("total: %.2f" %total)

