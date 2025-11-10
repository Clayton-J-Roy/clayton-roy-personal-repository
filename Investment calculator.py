

def main():

    year = int(input("How many years: "))
    s = float(input("Starting amount: "))
    i = float(input("Yearly Interest: ")) / 100
    reccuring = float(input("How much monthly: "))
    year = year * 12
    x = 0
    y = 0

    while year > 0:
        year = year - 1
        s = s + reccuring
        x = x + 1
        if x == 12:
            x = 0
            y = y + 1
            sum = (s * i) + s
            print("Investment: {:,} Year: {}".format(sum, y))





if  __name__ == "__main__":
    main()