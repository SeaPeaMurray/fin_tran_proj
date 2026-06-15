import bankEmulator
import BAIv2ObjectGenerator

myGen = bankEmulator.myGen()
myBAIv2 = BAIv2ObjectGenerator.BAIv2Gen()
myGen.genBankSending()
myGen.genBankReceiving()
myGen.genTransaction()
# print(dir(myBAIv2.myGen))
print(myGen.transaction_id)
myBAIv2.genBAIv2FileHeader(myGen)
print(myBAIv2.fileHeader)
myBAIv2.genBAIv2Transaction(myGen)
print(myBAIv2.transactionDetail)
print(dir(myBAIv2))
