import faker
import re
from formattingFunctions import createFourLengthCode as makeFour
from formattingFunctions import formatDate
from formattingFunctions import formatTime


class BAIv2Gen:
    def __init__(self):
        self.fake = faker.Faker()
        self.BAIv2 = {}

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

    def genBAIv2GroupHeader(self, genObj):
        pass

    def genBAIv2AccountIdentifier(self, genObj):
        pass

    def genBAIv2Transaction(self, genObj):
        self.transactionDetail = "16," + "000," + str(genObj.amount)

    def genBAIv2GroupTrailer(self, genObj):
        pass

    def genBAIv2FileTrailer(self, genObj):
        pass

    def genBAIv2Complete(self, genObj):
        pass
