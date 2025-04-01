# python variables 
name = "John" # string 
age = 25  # integer 
height = 1.75  # float, double 
is_student = True # boolean  

print(type(name))
print(type(age))

print(type(height)) #<class 'float'>
print(type(is_student)) #<class 'bool'>

x = y = z = 0

a, b, c = 1, 2, 3
print(a, b, c)
coordinates = (3, 4)
x, y = coordinates
print(x, y) # 3 4 

a, b = 5, 10
a, b = b, a # Python-ii toonii utgiig solih arga 
print(a, b) # 10 5





x = 10 
print(type(x)) #<class 'str'>

float_number = float(10) # 10.0
integer = int(3.14) # 3
string_number = str(42) # "42"

print(type(float_number))  #<class 'float'>
print(type(integer)) #<class 'int'>
print(type(string_number))  #<class 'str'>

# Logic utguud
is_active = True
is_completed = False

# and logic - 2 utga 2-uulaa unen ued unen baidag 
print(False and False) # False 
print(False and True) # False
print(True and False) # False
print(True and True) # True

#OR Logic- ali neg utga ni unen baival unen boldog ter tohioldliig 
print(False or False) #False
print(True or False) # True
print(False or True) # True
print(True or True) # True

# Not logic - tuhain boolean utgiin esreg 
print(not False)  # True
print(not True)  # False 

# Logic uildluud 
print(True and False) # False
print(True or False)  # True

# Jagsaalt uusgeh 
friuts = ["alim", "banana" "intoor"]
mixed_list = [1, "sain baina", 3.14, True]

# Elementuud ruu handah 
first_friut = friuts[0]    # "alim"
last_friunt = friuts[-1]   # "intoor"

# Jagsaaltiig oorchloh 
friuts.append("ulaan looli") # Togsgold nemeh 
friuts.insert(1, "mango") # Todorhoi bairlald oruulah
friuts.remove("banana")  # Utgaar ni hasah 
popped_fruid = friuts.pop()  # Suuliin elementiig hasaj butsaah 

# Jagsaaltiin hesegchlel
numbers = [0, 1, 2, 3, 4, 5]
subset = numbers [1:4] # [1, 2, 3]


# Xyzgaar uusgeh 
numbers = range(5)    # 0, 1, 2, 3, 4
print(numbers)
# range (ehlel, togsgol, alham)
even_numbers = range(0, 10, 2)   # 0, 2, 4, 6, 8

#Xyzgaariig jagsaalt bolgoh
number_list = list(range(5)) # [0, 1, 2, 3, 4]
print(numbers_list)

x = 10 #undsen onoolt 

# Niilmel onoolt 
x += 5 # x = x + 5 (15)
x -= 3 # x = x - 3 (12)
x *= 2 # x = x * 2 (24)
x /= 4 # x = x / 4 (6.0)
x //= 2 # x = x // 2 (3.0)
x %= 2 # x = x % 2 (1.0)
x **= 3 # x = x ** 3 (1.0)

# Olon onoolt 
a, b, c = 1, 2, 3

a = 10 
b = 5 

equal = a == b #False
not_equal = a != b #True
greather_than = a > b #True
less_than = a < b  #False 
greather_equal = a >=b #True 
less_equal = a <= b  #False 

# Ginjin haritsuulalt 
result = 1 < 3 < 5  #True (1 < 3 and 3 < 5 gesentei adil)
result = 5 > 3 < 1 # False (5 > 3 and 3 < 1 gesentei adil)