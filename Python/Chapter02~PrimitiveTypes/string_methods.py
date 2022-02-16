"""
String Methods Practice 
"""
string = "   i like CODE, I want to code!    "

# Capitalisation
print(string.upper())

# Lowercase
print(string.lower())

# Strip all whitespace
print(string.strip())

# Strip Left whitespace
print(string.lstrip())

# Strip Right Whitespace
print(string.rstrip())

# find starting index of "CODE"
print(string.find("CODE"))

# Replace "i" with "OZKAR"
print(string.replace("i", "OZKAR"))

# Check if "code" exists in string
print("code" in string)

# Check if "Sasquach" does NOT exist in string
print("Sasquach" not in string)
