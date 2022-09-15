firstName=input('First name: ')
while firstName == "":
    firstName=input('First name: ')
midInit=input('Middle initial(you can leave blank): ')
lastName=input('Last name: ')
while lastName == "":
    lastName=input('Last name: ')
if midInit=="":
    print("Nice to meet you, "+firstName+" "+lastName+"!")
else:
    print("Nice to meet you, "+firstName+" "+midInit+". "+lastName+"!")
