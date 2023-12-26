print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combined = name1 + name2
combined_lower = combined.lower()

t = combined_lower.count("t")
r = combined_lower.count("r")
u = combined_lower.count("u")
e = combined_lower.count("e")
dig1 = t+r+u+e
print(dig1)

l = combined_lower.count("l")
o = combined_lower.count("o")
v = combined_lower.count("v")
e = combined_lower.count("e")
dig2 = l+o+v+e
print(dig2)

tens = dig1*10
score = tens+dig2
print(f"score = {score}")

if 10 >= score or score <= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"your score is {score}")