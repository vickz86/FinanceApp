exLi = ["hello;12;booby", "bonjour;12;james", "allo;15;billie"]


def TuppleFromRawList(rawList: list) -> tuple:
    """convert a list of string separated by ; , into a tupple of tupple"""
    for str in rawList:
        element = str.split(";")
        print(element)


TuppleFromRawList(exLi)
