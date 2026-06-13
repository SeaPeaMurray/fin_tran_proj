import bankEmulator
import BAIv2Generator

myGen = bankEmulator.myGen()
myBAIv2 = BAIv2Generator.BAIv2Gen()
myGen.genBankSending()
myGen.genBankReceiving()
print(myGen.sendingBank)
print(myGen.receivingBank)
myBAIv2.genBAIv2FileHeader(myGen)
print(myBAIv2.fileHeader)