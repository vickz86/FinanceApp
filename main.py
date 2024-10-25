from Money.money import Income, LoadIncome
from pathlib import Path


# - - - - - LOGIC- - - - -


def main():
    # list of income
    # create the path for the income
    pathIncome = Path.cwd() / "Money" / "income.txt"
    # load all the income
    listIncome = LoadIncome(pathIncome)

    for el in listIncome:
        print(el)


# FUNCTION


main()
