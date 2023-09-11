def main():

    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):

    float_dollars = float(d.strip('$'))
    print(f"Price is {float_dollars:.1f}")
    return float_dollars

def percent_to_float(f):

    float_percent = float(f.strip('%')) / 100
    print(f"Percentage is {float_percent:.1f}")
    return float_percent

main()
