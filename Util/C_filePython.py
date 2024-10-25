listTest = ["un deux", "troix quatre", "cinq six", "seven"]


def OpenFile(filePath: str = "_data.txt") -> list:
    """return a list object,each line is an element"""
    with open(filePath, "r") as fObj:
        # create the list object
        rawList = fObj.readlines()
        # create a new list obj
        outList = []
        # remove \n at the end of the line
        for line in rawList:
            outList.append(line.strip())
        # return the list
        return outList


def WriteFile(listWrite: list, filePath: str = "_data.txt"):
    """write a list to a file, the list must only contain string"""
    writeList = []

    # add /n to all element of the list , but the last one
    for val, el in enumerate(listWrite):
        # check all element are string
        if isinstance(el, str) != True:
            print(f"ERROR ,{el} is not of type string")

        # check if it is the last element
        if val == (len(listWrite) - 1):
            writeList.append(el)
        else:
            el += "\n"
            writeList.append(el)

    with open(filePath, "w") as fObj:
        fObj.writelines(writeList)
    pass


# WriteFile(listTest)
