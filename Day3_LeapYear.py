yearToCheck = int(input("What year do you want to check?\n"))
if yearToCheck % 4 == 0:
    mod4 = yearToCheck % 4
    print(f"{yearToCheck} % 4 = {mod4}")
    if yearToCheck % 100 == 0:
        mod100 = yearToCheck % 100
        print(f"{yearToCheck} % 100 = {mod100}")

        if yearToCheck % 400 == 0:
            mod400 = yearToCheck % 400
            print(f"{yearToCheck} % 400 = {mod400}")
            print(f"{yearToCheck} is a leap year. Although {yearToCheck} is divisible by 100, it is also divisible by 400.")
        else:
            print(f"{yearToCheck} is not a leap year")
    elif yearToCheck % 100 != 0:
        mod100 = yearToCheck % 100
        print(f"{yearToCheck} is a leap year. {yearToCheck} % 100 is {mod100}")
    else:
        print(f"{yearToCheck} is not a leap year.")
else:
    print(f"{yearToCheck} is not a leap year.")


# if yearToCheck % 4 == 0:
#     if yearToCheck % 100 == 0:
#         if yearToCheck % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     elif yearToCheck % 100 != 0:
#         print("Leap year")
#     else:
#         print("Not leap Year")
# else:
#     print("Not leap year")