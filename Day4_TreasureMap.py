line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = "C2" # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# one option is to use if/elifs:
# if str(position[0]).upper() == "A":
#     column = 0
# elif str(position[0]).upper() == "B":
#     column = 1
# elif str(position[0]).upper() == "C":
#     column = 2

#Alternative option to if/elifs:
abc = ["A","B","C"]
column = abc.index(position[0].upper())

row = int(position[1]) -1
map[row][column] = "x"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")