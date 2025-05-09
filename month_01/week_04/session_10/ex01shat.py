# special characters
special_chars = "New line: \n\tTabulator"
print(special_chars)

# raw string
speacial_chars = r"New line: \n\tTabulator"
print(speacial_chars)


text = "Mongol"
text = " Mongol uls"
words = text.split(" ")
print(type(words))
joined = ", ".join(words)
print(joined) # Mongol, uls

padded = "Mongol"
print(padded.strip()) # "Mongol"
print(padded.lstrip()) # "Mongol"
print(padded.rstrip()) # " Mongol "

print("123".isdigit()) # True
print("abc".isalpha()) # True
print("abc123".isalnum()) # True
print(" ".isspace()) # True
name = "Berkhee"
age = 33
print(f"Sain uu, {name}! Tanii nas {age}")

pi = 3.14159
print(f"Pi too: {pi:.2f}") # pi too 3.14
print(f"Xuvi: {0.25:.1%}") # Xuvi: 25.0% jishee 100% gevel 100-(0 garj irne)

message = "Hi "
message += "Berkhee"
print(message)
number = 10 
number += 1
print(number)

text = "Hello, World!"
# list comprehesion
vowels= [char for char in text if char.lower() in "hlw"]
print(vowels)
# Temdegt moriig horvuuleh 
uppercase = [sda.upper() for sda in text]
print(uppercase) # ['H', 'E', 'L', 'O', ',' ' ', 'W', 'O', 'R', 'L', 'D', '!']