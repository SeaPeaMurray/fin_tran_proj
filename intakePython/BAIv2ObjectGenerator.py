import faker
import re
from bankEmulator import myGen
from formattingFunctions import createFourLengthCode as makeFour
from formattingFunctions import formatDate
from formattingFunctions import formatTime


class BAIv2Gen:
    def __init__(self):
        self.fake = faker.Faker()
        self.myGen = myGen()

    def genTest(self):
        self.myGen.genBankSending()
        self.myGen.genBankReceiving()
        self.myGen.genCreditCard()
        print(self.myGen.sendingBank)

    def genBAIv2FileHeader(self, genObj):
        bankCodeSending = makeFour(genObj.sendingBank)
        bankCodeReceiving = makeFour(genObj.receivingBank)
        fileHeaderDate = formatDate(genObj.date)
        fileHeaderTime = formatTime(genObj.time)
        self.fileHeader = (
            "01,"
            + bankCodeSending
            + ","
            + bankCodeReceiving
            + ","
            + fileHeaderDate
            + ","
            + fileHeaderTime
            + ","
            + "0000000"
        )

    def genBAIv2GroupHeader(self):
        self.groupHeader = "02,"

    def genBAIv2AccountIdentifier(self):
        self.accountIdentifier = "03,"

    def genBAIv2Transaction(self, genObj):
        self.transactionDetail = "16," + "000," + str(genObj.amount)

    def genBAIv2GroupTrailer(self):
        pass

    def genBAIv2FileTrailer(self):
        pass

    def genAllObjects(self, genObj, numberOfTransactions=1):
        self.myTransactions = []
        genObj.genBankSending()
        genObj.genBankReceiving()
        genObj.genCreditCard()
        for i in range(numberOfTransactions):
            genObj.genTransaction()
            self.myTransactions.append(genObj.transaction_id)

    def genBAIv2Complete(self):
        with open("BAIv2.txt", "w") as file:
            file.write(self.fileHeader + "\n")
            file.write(self.transactionDetail + "\n")
            file.write(self.fileTrailer + "\n")
