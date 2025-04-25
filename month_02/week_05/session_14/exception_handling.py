# exception handling 
# problem

print('This line will prin')
x = 10 
y = 0 

if x == 5:
    print('Hello')

print('Next line')

# Division by Zero 
# print(x / y)

print('Third line')

# Undsen butets - Exception Handler 
try:
    # aldaa garch bolzoshgui kod
    result = 10 / 0 
except ZeroDivisionError:
    # Aldaa garval hiih uildel 
    print("tegeer huvaah bolomjgui")

print("Fourth line")

# Olon torliin aldaag barih 
try: 
    number= int(input("Too oruulna uu:"))
    result = 10 / number
except ValueError:
    print("Zov too oruulna uu!")
except ZeroDivisionError:
    print("Tegeer huvaah bolomjgui!")

print('Fifth line')
# hed heden aldaag neg dor barih 
try:
    number = int(input("Too oruulna uu: "))
    result = 10 / number
except (ValueError, ZeroDivisionError):
    print("Buruu orolt esvel tegeer huvaah oroldlogo!")

# Xervee ymar aldaag busdaas ylgaj chadahgui bol 
# Buh aldaag barih (bolgoomjtoi heregleh)
# file = open("nonexistent.txt", 'r')

try:
#      # Ersdeltei kod
    file = open("nonexistent.txt", 'r')
except Exception as e:
    print(f"Aldaa garlaa: {e}")

print("Sixth line")

# Aldaanii medeelel avah:
try:
    x = 10 / 0 
except Exception as e:
    print(f"Aldaanii torol: {type(e).__name__}")
    print(f"Aldaanii messej: {str(e)}")

# else blok - aldaa garaagui ued ajillana: 
try:
    number = int(input("Too oruulna uu!"))
    result = 10 / number
except ValueError:
    print("Zov too oruulna uu!")
except ZeroDivisionError:
    print("Tegeer huvaah bolomjgui!")
else:
    # Aldaa garaagui bol ajillana
    print(f"Ur dun: {result}")

# finally blok - aldaa garsan esehees ul hamaaran ajillana:
try:
    # Ersdeltei kod
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File oldoogui!")
else: 
    print(f"File ner: {file.name}")
    print(f"file undes: {file.undest}")
finally:
    # ul hamaaran ajillana
    if 'file' in locals() and not file.closed:
        file.close()

# aldaa damjuulah (re-raising):
try:
    x = int("too bish")
except ValueError:
    print("ValueError bolovsruulj baina ...")
    # Aldaag damjuulah
    # raise

# Oor aldaa uusgeh:
try:
    age = int(input("Nasaa oruulna uu: "))
    if age < 0:
        raise ValueError("Nas sorog too baij bolohgui")
except ValueError as e:
    if "invalid literal" in str(e):
        print("Zov too oruulna uu")
    else:
        print(e)

# Exception chainin: (aldaa holboh):
try:
    # anhnii aldaa
    x = int("too bish")
except ValueError as e:
    # Shine aldaa uusgej, anhnii aldaatai holboh
    # raise RuntimeError("Bolovsruulalt amjiltgui bolson") from e
    print(e)
# traceback moduli ashiglah:
import traceback

try: 
    # aldaa garch bolzoshgui kod
    1 / 0 
except Exception:
    # delgerengui traceback medeelel hevleh
    traceback.print_exc()

# Exercise divide gedeg funkts bicheed a, b gedeg parametr avdag bolgono uu 
# enehuu funkts ni tuhain parametruudiiig too esehiig shalgaad too bish bol
# ValueError aldaa ogdog harin 0-d huvaaval ZeroDivisionError ogdog bailgaarai.

def divide(a, b):
    try:
        int(a)
        int(b)
        result = a / b
    except ValueError:
        print("Give me correct numbers")
    except ValueError:
        print("Give me correct numbers")
    except ZeroDivisionError:
        print("Do not divide number by Zero")
    except Exception:
        print('Error occurred')
    else:
        print(result)

divide(4, 0) # Do not divide number by Zero
divide('4', 5 ) # Do not divide number by Zero
divide('hi', 'hi') # Give me correct numbers










