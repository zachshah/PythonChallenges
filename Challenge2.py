numOne=input("Type an integer: ")
while numOne.isnumeric()==False:
    numOne=input("Type an integer: ")
numTwo=input("Type another: ")
while numTwo.isnumeric()==False:
    numTwo=input("Type another: ")
workingNum=int(numOne)
goalNum=int(numTwo)
if int(numOne)>int(numTwo):
    workingNum=int(numTwo)
    goalNum=int(numOne)
while workingNum<=goalNum:
    if workingNum%3==0:
        print(str(workingNum))
    workingNum+=1


