import bankEmulator
import BAIv2Generator

myGen = bankEmulator.myGen()
myBAIv2 = BAIv2Generator.BAIv2Gen()
myGen.genBankSending()
myGen.genBankReceiving()
myGen.genTransaction()
print(myGen.transaction_id)
myGen.genTransaction()
print(myGen.transaction_id)
myBAIv2.genBAIv2FileHeader(myGen)
print(myBAIv2.fileHeader)
myBAIv2.genBAIv2Transaction(myGen)
print(myBAIv2.transactionDetail)
