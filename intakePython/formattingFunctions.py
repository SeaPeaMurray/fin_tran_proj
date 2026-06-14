import re

def createFourLengthCode(nameToSplit):
    nameToSplitDone = nameToSplit.split(" ")
    nameCode = None
    try:
        for index, word in enumerate(nameToSplitDone):
            if len(word) == 4 and word.lower() != "bank":
                    nameCode = word.upper()
            elif nameCode is None and index == len(nameToSplitDone) - 1:
                nameCode = max(nameToSplitDone, key=len)[:4].upper()
    except:
        nameCode = "XXXX" 
    return nameCode