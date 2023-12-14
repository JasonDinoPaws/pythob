def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def GetNumberPlace(s): # gets the place to where a int is found
    for i in range(len(s)):
        try:
            n = int(s[i])
        except ValueError:
            continue
        return i

def findpun(s): # checks if the string has puncuation
    for i in [" ",",",".",":",";"]:
        if s.find(i) > 0:
            return False
    return True

def is_valid(s):
    l = len(s)
    nplace = GetNumberPlace(s)
    haspun = not findpun(s)
    if 2 > l or l > 6 or haspun: # checks if the length is less than 2 or more than 6 or has puncuation
        return False
    elif nplace:
        if s[nplace] == "0": # check if the place that the number was found is 0
            return False
        else:
            try:
                n = int(s[nplace:l]) # checks if from where the number was found to the rest can be a int
            except ValueError:
                return False


    return True



main()