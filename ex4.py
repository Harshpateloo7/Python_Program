#Write correct Python code to complete the following tasks. Solutions that do not incorporate a list will receive a grade of O.
#Use the variable years = [2017,1977,2016,1978,2015,1980,2008,1983,1984,1985,1999,2002,2005,2019] to
#answer the following instructions:
#[11 a) Remove 1978 from the list
#[1] b) Add 2018 to the list
#[2] c) Write the code to check if 1978 is still in the list, and if it is, remove it.
#[1] d) Sort the list using either list functions or list methods.
#years= [2017,1977,2016,1978,2015,1980,2008,1983,1984,1985,1999,2002,2005,2019]

#remove 1978 from the list
years.remove(1978)
print(years)

#Add 2018 to the list
years.append(2018)
print(years)

# Write the code to check if 1978 in the list, and if it's remove it.
for year in years:
    if year == 1978:
        years.remove(year)
print(years)

#sort a list using list method
years.sort()
print(years)