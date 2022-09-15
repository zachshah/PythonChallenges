inputNum=input('integer:')
inputSmallNum=input('integer smaller than '+str(inputNum)+":")
inputNumInt=float(inputNum)
inputSmallNumInt=float(inputSmallNum)
timesWentIn=0
print(str(inputNumInt)+" % "+str(inputSmallNumInt)+" = "+str(inputNumInt%inputSmallNumInt))
while inputNumInt>=inputSmallNumInt:
    inputNumInt=inputNumInt-inputSmallNumInt
    timesWentIn +=1
print(str(timesWentIn)+" times")
