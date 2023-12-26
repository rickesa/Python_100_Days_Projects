print("Thank you for choosing Python Pizza Deliveries!")
def costCalc (size, add_pepperoni, extra_cheese):
    final_price = 0
    if size.upper() == "S":
        final_price += 15
        if add_pepperoni.upper() == "Y":
            final_price += 2
    elif size.upper() == "M":
        final_price += 20
        if add_pepperoni.upper() == "Y":
            final_price += 3
    elif size.upper() == "L":
        final_price += 25
        if add_pepperoni.upper() == "Y":
            final_price += 3
    if extra_cheese.upper() == "Y":
        final_price += 1
    print(f"Your total for your pizza is {final_price}.")

while True:
    size = input("What size\n")
    if size.upper() in ("S","M","L"):
        print("Size is in SML")
        add_pepperoni = input("Add Pepp?\n")
        if add_pepperoni.upper() in ("Y","N"):
            # print("Pepperoni is in YN")
            extra_cheese = input("Extra Cheese?\n")
            if extra_cheese.upper() in ("Y", "N"):
                # print("extra cheese is in YN")
                costCalc(size,add_pepperoni,extra_cheese)
                break
            else:
                print("invalid extra cheese response. Please type 'Y' or 'N' only.")
        else:
            print("invalid pepperoni response. Please type 'Y' or 'N' only.")
    elif size.upper() not in ("S","M","L"):
        print("invalid size. Please type 'S', 'M', or 'L' only.")