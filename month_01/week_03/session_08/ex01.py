# Python loop - For

# Recapture 

colors = ["red", "yellow", "blue", "green", "purple"] #
print(colors)

# print out "blue"

print(colors[2]) # blue
print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])
print(colors[4])

# Solution - loop 
# For - Loop
for a in colors:
    print(a)

# For - range 
for i in range(9):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(3,10, 3):
    print(i)

# While - Loop 
i = 1
while i < 9:
    print(i) # infinite loop     # garah control c
    i = i +1   # i += 1 

# tsaashaagaa urgeljleh 

# Exercise 

# While loop ashiglan 10-aas 100 hurtelh toonuudiig hevleh

i = 10
while i < 100:
    print(i)
    i = i + 1 

# 20-oos 60 hurtelh toonuudiig zovhon tegsh toonuudiig ni xevlene uu 

i = 20 
while i < 60: 
    print(i)
    i = i + 2

i = 20 
while i <= 60:
    if i %2 == 0:
        print(i)
        i = i + 1
        




