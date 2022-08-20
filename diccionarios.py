"""Dictionaries allows to store keys, or pair values,
it's something like a database, each key has to be unique,
their names can't be repeated, and its value has to be
unique too"""

customer = {
	
	#Names are sensible to lower and uppercase
	"Name": "Allan",
	"Age": 18,
	"is_verified": True
}

#It returns an error if the key doesn't exist
print(customer["Name"])

#It returns "none" if the key doesn't exist
print(customer.get("Birthdate"))

#Gets also allows to assign a value that doesn't exist
print(customer.get("Birthdate", "April 24 2003"))

#Same process can be done like this:
customer["Birthdate"] = 24042003
print(customer["Birthdate"])


numbers = {
	
	"1": "One",
	"2": "Two",
	"3": "Three",
	"4": "Four",
	"5": "Five",
	"6": "Six",
	"7": "Seven",
	"8": "Eight",
	"9": "Nine",
	"0": "Zero"
}

phone = input("Type a phone number: ")
out = ""
for ch in phone:
	out += numbers.get(ch, "!") + " "
print(out)