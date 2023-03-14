"""Demonstrations of dictionary capabilities."""
 

# Declaring the type of dictionary
schools: dict[str, int]

# Initialize to an empty dict
schools = dict()

# Set a key-value pairing in the dict
schools["UNC"] = 19_400 
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# Print a dictionary literal expression
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dict
# by its key 
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools

print(f"Duke is present: {is_duke_present}")

if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools.")

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200


print(schools)

# Demo of dictionary literals

# Empty dictionary literal
schools = {}  # same as dict(), just shorter hand notation
print(schools)

# Alternatively, intialize key-value pairs
schools = {
    "UNC": 19400, 
    "Dukie": 6717, 
    "NCSU": 26150
}
print(schools)

# What happens when a key does not exist?
print(schools["UNCC"])