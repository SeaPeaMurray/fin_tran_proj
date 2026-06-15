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


def formatDate(dateString):
    # Example format: "2023-10-05" -> "051023"
    dateParts = dateString.split("-")
    return f"{dateParts[2]}{dateParts[1]}{dateParts[0][-2:]}"


def formatTime(timeString):
    # Example format: "14:30:00" -> "1430"
    timeParts = timeString.split(":")
    return f"{timeParts[0]}{timeParts[1]}"


def formatNegativeTransaction(amount):
    if amount < 0:
        newAmount = round(np.abs(amount))
    return newAmount
