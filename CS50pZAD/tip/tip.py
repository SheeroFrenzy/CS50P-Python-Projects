def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_dollars_to_float = d.replace("$","")
    return float(d_dollars_to_float)

def percent_to_float(p):
    p_percent_to_float = p.replace("%","")
    return float(p_percent_to_float)/ 100

main()
