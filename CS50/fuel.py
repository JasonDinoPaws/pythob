def main():
    num = round(getxandy()*100)
    if num <= 1:
        num = "E"
    elif num >= 99:
        num = "F"
    else:
        num = str(num)+"%"
    print(num)

def getxandy():
    while (True):
        txt = input("Fraction: ")
        try:
            x,y = txt.split("/")
            x = int(x)
            y = int(y)
            if x > y:
                continue
            else:
                return x/y
        except (ValueError, ZeroDivisionError):
            continue
main()