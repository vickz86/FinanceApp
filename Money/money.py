# import the function to open the file
from Util.G_pathPython import PathOpenFile, PathWriteFile
from pathlib import Path


class Income:
    # Init
    def __init__(self, name: str, amount: int, time: str, description: str):
        # create the name of the income
        self.name = name

        # Check time is a string , should be m for monthly or y for yearly
        if not isinstance(time, str):
            raise TypeError("Error, time should be string")
        # Check time is either m or y
        if time not in ("m", "y"):
            raise TypeError("Error, time should be either 'm' or 'y'")
        self.time = time

        self.description = description

        # Create month amount
        self.amount = amount
        if time == "y":
            self.monthAmount = round(amount / 12)
        elif time == "m":
            self.monthAmount = amount

    def __str__(self):
        result = (
            f"name: {self.name}\n"
            f"amount: {self.amount}\n"
            f"monthAmount: {self.monthAmount}\n"
            f"income is {'monthly' if self.time == 'm' else 'yearly'}\n"
            f"description: {self.description}\n"
        )
        return result

    def income_year(self) -> int:
        """Return the yearly income of the current instance."""
        if self.time == "y":
            return self.amount

        if self.time == "m":
            yearInc = self.amount * 12
            return yearInc

    pass


def LoadIncome(thePath: Path) -> list:
    """return a list of class income"""
    # load the income file to a list
    rawIncomeList = PathOpenFile(thePath)
    # split the list into multiple list
    separateList: list = []
    for el in rawIncomeList:
        separateList.append(el.split(";"))

    # list of instance of clase Income
    listIncome: list = []
    # Add all el in separateList into listIncome convert the second element into an int
    for el in separateList:
        try:
            el[1] = int(el[1])
        except:
            raise TypeError(f"{el[0]} second value is not an int")
        newIncome = Income(el[0], el[1], el[2], el[3])
        listIncome.append(newIncome)
    return listIncome
