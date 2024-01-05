# def my_function():
#     return 3*2
#
#
# output = my_function()  # return statement sets the call of my_function() to equal 6
# print(output)

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "one of your inputs was blank"
    cap_f_name = f_name.title()
    cap_l_name = l_name.title()
    return f"Result: {cap_f_name} {cap_l_name}"


first_name = input("What is the first name?\n")
last_name = "RICKE"
formatted = format_name(first_name,last_name)
print(formatted)


