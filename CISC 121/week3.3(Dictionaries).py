########################    Dictionaries
####    A container object that stores a collection of key/value pairs
####    { <key 1>:<value 1>, ... }

##  Creating Dictionary
starWarsEpisodes = {"IV":"A New Hope", "V":"The Empire Strikes Back", \
                    "VI":"Return of The Jedi", "VII":"The Force Awakens", \
                    "VIII":"???"}
print(starWarsEpisodes)

##  Empty Dictionary
d = {}

##  Change value
starWarsEpisodes["VIII"] = "The Last Jedi"
print(starWarsEpisodes)

##  Insert value
starWarsEpisodes["IX"] = "???"
print(starWarsEpisodes)

##  Delete key
del starWarsEpisodes["IX"]
print(starWarsEpisodes)
##      Or
x = starWarsEpisodes.pop("VIII")
print(starWarsEpisodes)
print(x)

##  Looping through a dictionary with key and value
for number, title in starWarsEpisodes.items():
    print("Episode",number,":",title)

##  Looping with just keys
for number in starWarsEpisodes.keys():
    print("Episode", number,":", starWarsEpisodes[number])

####    Need keys to access values

##  Dictionary with a mix of key/value types
residencesOnAStreet = {12:"House", 14:["Apt. 1", "Apt. 2 "], 14.5:None, "16":0}
print(residencesOnAStreet)

for number, value in residencesOnAStreet.items():
    if isinstance(number,int):
        print(number, "is an int")
    elif isinstance(number, float):
        print(number, "is a float")
    elif isinstance(number,str):
        print(number, "is a string")
    else:
        print("I have no idead what this is", number)




