# get an int value from the user
def GetInteger(question: str, maxRange: int = 10_000_000, minRange: int = 0) -> int:
    """get integer from user based on question, option to specify max and min value"""
    while True:
        # print the input
        print(question)
        # get the input from the user
        rawInput = input()
        # check if the value contain only number
        if rawInput.isdigit():
            # convert to an int
            rawInput = int(rawInput)
            # check if input is not higher than max value
            if rawInput > maxRange:
                print(f"{rawInput} is higher than max value {maxRange} \nTry again")
                continue
            if rawInput < minRange:
                print(f"{rawInput} is lower than min value {minRange} \nTry again")
                continue
            # return int value
            return int(rawInput)
        else:
            print(f"{rawInput} is not an integer \nTry again")
