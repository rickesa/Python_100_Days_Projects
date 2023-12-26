print("Welcome to the tip calculator")
bill_total = float(input("What was the total bill?"))
tip_response = input("What percentage tip would you like to give? 10, 12, or 15?")
split_ways = input("How many people will be splitting the bill?")
# bill_total = 124.56
# tip_response = 12
# split_ways = 7
tip_as_percentage = tip_response / 100 + 1
print(tip_as_percentage)
bill_plus_tip = bill_total * tip_as_percentage
print(bill_plus_tip)
final_bill_per_person = round(bill_plus_tip / int(split_ways),2)
print("Each person should pay", str(final_bill_per_person))