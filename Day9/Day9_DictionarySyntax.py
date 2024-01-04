#  Dictionary syntax
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected."
    ,"Function": "A piece of coce that lets you easily call over and over again"
}
# print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again"
# print(programming_dictionary)
empty_dict = {}
empty_dict["key1"] = "value1"

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# nesting dictionaries
travel_log = {
    "England": "London"
    ,"France": ["Paris", "Lille", "Dijon"]
    ,"Germany": ["Berlin", "Hamburg", "Stuttgart"]
    ,"USA": {"cities_visited":["Los Angeles", "San Francisco", "San Diego"], "total visits":[2, 3, 1]}
}
# print(travel_log["USA"])
# print(travel_log["USA"]["cities_visited"][0])

# Nesting dicitonaries in a list
travel_log = [
{
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
 }
,{
        "country":"Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
,{
        "country": "Engalnd",
        "cities_visited": ["London", "Manchester"],
        "total_visits": 8
    }
,{
        "country":"Spain",
        "cities_visited": ["Barcelona", "Mallorca"],
        "total_visits": 2
    }
]
# print(travel_log[2])
country = "USA" # Add country name
visits = 4 # Number of visits
list_of_cities = ["New York","Los Angeles","Columbus"] # create list from formatted string


travel_log.append({"country": country, "cities": list_of_cities, "visits": visits})

for item in range(len(travel_log)):
    print(travel_log[item])