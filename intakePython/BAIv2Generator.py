import faker
import re
from formattingFunctions import createFourLengthCode as makeFour


class BAIv2Gen:
    def __init__(self):
        self.fake = faker.Faker()
        self.BAIv2 = {}

    def genBAIv2FileHeader(self, genObj):
        bankCodeSending = makeFour(genObj.sendingBank)
        bankCodeReceiving = makeFour(genObj.receivingBank)
        fileHeaderDate = genObj.date
        fileHeaderTime = genObj.time
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
        pass

    def genBAIv2GroupTrailer(self, genObj):
        pass

    def genBAIv2FileTrailer(self, genObj):
        pass
