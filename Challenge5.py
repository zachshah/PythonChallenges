from random import randint
numOne=randint(1,10)
numTwo=randint(1,10)
print("what is the product of "+str(numOne)+" and "+str(numTwo)+"?")
ans=input("answer here: ")
if int(ans)==numOne*numTwo:
    print("Excellent!")
else:
    print("Sorry, no cigar!")
