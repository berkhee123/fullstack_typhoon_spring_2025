# Python strings

single_quotes = "This is single quotation text"
double_quotes = "This is double quotation text"
multi_line_string = """
        Multi Line String 
        Text
    """

# special characters
special_chars = "New line: \n\tTabulator"
print(special_chars)

# raw string
speacial_chars = r"New line: \n\tTabulator"
print(speacial_chars)

text = "Mongol"
# Indekseer handah
print(text[0]) # M
print(text[-1]) # l
# Hesegchleh
print(text[0]) # M
print(text[:3]) # Mon
print(text[3:]) # gol
print(text[::-1]) # lognoM

text = " Mongol uls"
# Urt 
print(len(text))
# Tom, jijig useg 
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
# Xaix 
print(text.find("gol"))
print(text.find("oros"))
print("gol" in text)  # True
print(text.count("o"))

# Orluulah 
print(text.replace("uls", "xel")) # Mongol hel
# Temdegt moriig huvaah
words = text.split(" ")
print(words) # ["Mongol", "uls"]
#Temdegt moruudiig negtgeh 
joined = ", ".join(words)
print(type(joined)) # Mongol, uls

# Ehlel, togsgol shalgah 
print(text.startswith("Mon")) # True
print(text.endswith("uls")) # True
# Xooson zai arilgah 
padded = "Mongol"
print(padded.strip()) # "Mongol"
print(padded.lstrip()) # "Mongol"
print(padded.rstrip()) # " Mongol "
# Temdegt moriin buttsiig shalgah 
print("123".isdigit()) # True
print("abc".isalpha()) # True
print("abc123".isalnum()) # True
print(" ".isspace()) # True

# % operator ashiglah ( xuuchin arga )
name = "Bat" 
age = 25 
print("Sain uu, %s! Tanii nas %d." % (name, age))      # Sain uu Bat! Tanii nas 25.0
# format () arga ashiglah 
print("Sain uu, {}! Tanii nas {}.".format(name, age))  # Sain uu Bat! Tanii nas 25.
print("Sain uu, {0}! Tanii nas {1}.".format(name, age)) # Sain uu Bat! Tanii nas 25.
print( 
       "Sain uu, {name}! Tanii nas {age}.".format(name=name, age=age)
    ) # Sain uu, Bat! Tanii nas 25.
# f-string ashiglah (Python 3.6+)
print(f"Sain uu, {name}! Tanii nas {age}.") # Sain uu, Bat! Tanii nas 25.
print(f"Tanii 5 jiliin daraah nas: {age + 5}")

# Toonuudiig formatlah 
pi = 3.14159
print(f"Pi too: {pi:.2f}") # pi too 3.14
print(f"Xuvi: {0.25:.1%}") # Xuvi: 25.0%

first = "Mongol"
last = "Uls"
# + operator ashiglah 
full = first + " " + last
print(full) # Mongol uls
# += operator ashiglah 
message = "Sain uu, "
message += "Bat!"
print(message) # Sain uu, Bat!
# Olon temdegt moriig negtgeh 
words = ["Python", "hel", "surah", "hylbar"]
sentence = " ".join(words)
print(sentence) # Python hel surah hylbar 

# Temdegt moriin oilgolt 
text = "Hello, World!"
# list comprehesion
vowels= [char for char in text if char.lower() in "aeiou"]
print(vowels)
# Temdegt moriig horvuuleh 
uppercase = [char.upper() for char in text]
print(uppercase) # ['H', 'E', 'L', 'O', ',' ' ', 'W', 'O', 'R', 'L', 'D', '!']