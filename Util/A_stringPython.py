example = "abc3def"


# return a letter from question
def GetSpecificLetter(theQuestion: str) -> str:
    while True:
        # ask for the letter you want to get
        answer: str = input(theQuestion)
        # check that is only a single letter
        if len(answer) != 1:
            print("your answer is too long\nOnly type 1 letter")
            continue
        # check the answer is.Alpha
        if answer.isalpha() == False:
            print("your answer is not a letter")
            continue
        return answer


# Get the first index of inputed Word
def GetIndexWord(strToFind: str, strToCheck: str) -> int:
    firstIndex = strToCheck.find(strToFind)
    print("hello my dear")


def GetIndexOfFirstNumbers(theStr: str) -> tuple:
    """return the start and end index of number in the string, return the number"""
    # TODO , out int
    # variable
    start: int
    end: int
    isPreviousInt: bool = False

    # loop through all letters
    for nb, el in enumerate(theStr):
        # get the index of the first digit value
        # check if previous is digit
        if theStr[(nb - 1)].isdigit():
            end = nb - 1
            continue

        if el.isdigit():
            start = nb

    number = theStr[start : end + 1]
    # print(start, end, number)

    return (start, end, int(number))


def IncreaseNumberString(theString: str) -> str:
    """return a string with number increased by 1"""
    # get values from above function
    start, end, nb = GetIndexOfFirstNumbers(theString)
    # start list
    startString = theString[:start]
    # DB print(startString)
    endString = theString[end + 1 :]
    # DB print(endString)
    # increase number by 1
    nb += 1
    # merge al element together
    returnString = str(startString + str(nb) + endString)
    return returnString
