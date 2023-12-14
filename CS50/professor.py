import random as r

def main():
    l = get_level()
    probs = generate_integer(l)
    ca = 0
    for i in probs:
        s = True
        c = 0
        while (s):
            if c == 3:
                print(str(probs[i][0])+" + "+str(probs[i][1])+ " = "+ str(probs[i][2]))
                s = False
            else:
                a = input(str(probs[i][0])+" + "+str(probs[i][1])+ " = ")
                if a.isdigit() and int(a) == probs[i][2]:
                    s = False
                    ca += 1
                else:
                    c += 1
                    print("EEE")
    print("Score: "+str(ca))


def get_level():
    while (True):
        t = input("Level: ")
        if t.isdigit() and t in ["1","2","3"]:
            return t


def generate_integer(l):
    probs = {}
    ra = {"1":[0,10],"2":[10,100],"3":[100,1000]}
    for i in range(10):
        a,b = r.randrange(ra[l][0],ra[l][1]),r.randrange(ra[l][0],ra[l][1])
        probs[i] = [a,b,a+b]
    return probs

if __name__ == "__main__":
    main()