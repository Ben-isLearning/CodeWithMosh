"""
Type conversions Practice
"""

variable_one = "sauce"
variable_two = 1
variable_thr = True
variable_fou = 3.14

print("Starting Variable;")
print(variable_two)
print(type(variable_two))
print("-----")

float_two = float(variable_two)
print(float_two)
print(type(float_two))
print("-----")

bool_two = bool(float_two)
print(bool_two)
print(type(bool_two))
print("-----")

string_two = str(bool_two)
print(string_two.lower())
print(type(string_two))
print("-----")


x = input("I'll double whatever you give me! ~")
y = int(x) * 2
print(f"Given: {x}, Receive: {y}")
