# import libraries
import requests
from pyfiglet import figlet_format
from termcolor import colored
from random import choice


# print the header
header = figlet_format("DAD JOKE 3000")
color_header = colored(header, color="magenta")
print(color_header)


# take the uder input
user_input = input("What joke you want to hear?")
# set url
url = "https://icanhazdadjoke.com/search"

# connect to the api
res = requests.get(url,
                   headers={"Accept": "application/json"},
                   params={"term": user_input}).json()

# fetch the total jokes count in the response
total_jokes = res["total_jokes"]
results = res["results"]

# define logic for showing jokes
if total_jokes > 1:
    print("There are many jokes for {}...Below is the one of them..".format(user_input))
    print(choice(results)["joke"])
elif total_jokes == 1:
    print("Only one joke for the search term {}".format(user_input))
    print(results[0]['joke'])
else:
    print("Sorry no search result for {}".format(user_input))
