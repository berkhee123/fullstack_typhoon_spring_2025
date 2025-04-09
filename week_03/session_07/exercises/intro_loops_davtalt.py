# python loops 

friuts = ["alim", "banana", "guzeelzgene"]

#Problem -- 100 shirheg jimsnii toroltoi list baival 
print(friuts[0])
print(friuts[1])
print(friuts[2])

mongolz = ["senzu1", "9102", "blitz3", "mzino4", "techno5"]
print(mongolz[3], mongolz[4])

# Solution - Loop buyu davtalt 

# 1. For loop 
for friut in friuts:
    print(friut)

# 0 - ees 5 xurtel (5 orohgui)
for i in range (5):
    print(i) # 0, 1, 2, 3, 4

# 2-oos 8 hurtel 
for i in range(2,8):
    print(i) # 2, 3, 4, 5, 6, 7

# 1-ees 10 xurtel, 2 alhmaar 
for i in range(1, 10, 2 ):
    print(i) # 1, 3, 5, 7, 9

for i in range(0, 10, 2 ):
    print(i) # 0, 2, 4, 8

# string buyu text 
message = "Python"

# Temdegt bureer davtalt 
for i in message: 
    print(i)

# enumarate 
fruits = ["alim", "banana", "guzeelzgene"]

# Indeks bolon elementiig avah 
for index, friut in enumerate(friuts):
    print(f"Indeks {index}: {friut}")

# Garalt: 
#Indeks 0: alim 
#Indeks 1: banana
#Indeks 2: guzeelzgene

#Todorhoi indeksees ehleh 
for index, friut in enumerate(friuts, start=1):
    print(f"{index}. {friut}") # 1. alim, 2. banana, 3. guzeelzgene

# break
for i in range(10):
    if i == 5:
        break
    print (i) #0, 1, 2, 3, 4

# continue 
for i in range(10): 
    if i % 2 == 0:
        continue
    print(i) # 1, 3, 5, 7, 9

# break heregleegui ued else heseg ajillana
for i in range(5):
    print(i)
else:
    print("Davtalt amjilttai duuslaa!")

# break hereglesen ued else heseg ajillahgui
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Ene heseg ajillahgui")

# double loop 
# Urgeljuuleh husnegt 
for i in range(1,4):
    for j in range(1,4):
        print(f"{i} x {j} = {i * j}")
        print("----")

# Engiin davtalt 
squares = []
print(squares)
for i in range(1, 6):
    squares.append(i ** 2)
print(squares) # [1, 4, 9, 16, 25]

# Jagsaaltiin oilgolt 
squares = [i ** 2 for i in range(1, 6)]
print(squares) # [1, 4, 9, 16, 25]

shat = []
print(shat)
shat.append (1234)
shat.append (2345) 
shat.append (3456)
shat.append (4567)
print(shat)


for a in range(1, 10):
    shat.append(a ** 2)
print(shat)

# Nohtsoltoi jagsaaltiin oilgolt
even_squares = [i ** 2 for i in range(1,11) if i % 2 == 0]
print(even_squares) # [4, 16, 36, 64, 100]



