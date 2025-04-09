# intro into python list 

# Problem - Variables
b = 7 
print(b)

# Solution - Lists
friuts = ["alim", "banana", "guzeelzgene"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "xoyr", 3.0, True]
empty_list = []
print(type(friuts))
print(friuts)
print(type(numbers))
print(numbers)
print(type(mixed))
print(mixed)

# list index 
# Eyreg indeks ( ehnees ni toolno)
print(friuts[0]) # alim
print(friuts[1]) # banana
print(friuts[2]) # guzeelzgene

# Sorog indeks (tossgoloos ni toolno)
print(friuts[-1]) # guzeelzgene
print(friuts[-2]) # banana
print(friuts[-3]) # alim

# Change list 

# Element oorchloh 
print(friuts[0])
friuts[0] = "uzem"
print(friuts) #['uzem', 'banana', 'guzeelzgene', 'kivi']
print(friuts[0])
friuts = ["alim", "banana", "guzeelzgene", "toms"]
print(friuts)

friuts.append ("liir")
print(friuts)
friuts.insert (0, "cherry")
print(friuts)

# Elements ustgah 
friuts.remove("banana")
print(friuts) # ['uzem', 'banana', 'guzeelzgene', 'kivi']

# Indekseer element ustgah 
friuts.pop(0) # mango-g ustgaj. xuvisagchij hadgalna
print(friuts)

#buh elementiig ustgah 
friuts.clear()
print(friuts) #[]

# List methods 
friuts = ['alim', 'banana', 'guzeelzgene', 'cherry']
print(friuts)

#Jagsaaliin urt 
print(len(friuts)) # 4 

# Jagsaaltiig erembleh
friuts.sort()
print(friuts) # ['alim', 'banana', 'guzeelzgene, 'cherry']

# Jagsaaltiig urvuu erembeleh 
friuts.reverse()
print(friuts) # ['guzeelzgene', 'banana', 'alim', 'cherry']

# Elementiin indeksiig oloh 
print(friuts.index("banana")) # 1 

# Elementiin toog toolloh 
print(friuts.count("banana")) # 1 



# Jagsaaltiig xuulbarlah 
friuts_copy = friuts.copy()
print(friuts_copy) # ['guzeelzgene', 'banana', 'alim']


print("index:", friuts.index("banana"), friuts_copy.index("banana"))
print("count:", friuts.count("banana"), friuts_copy.count("banana"))


# Jagsaaltuudiiig negtgeh 
more_friuts = ["kivi", "mango"]
friuts.extend(more_friuts)
print(friuts) # ['guzeelzgene', 'banana', 'alim']
print(more_friuts)
more_friuts.extend(friuts)
print(more_friuts)


print("count:", more_friuts.count('kivi'))
print(more_friuts.count("mango"))

## List Slicing 
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ehelel :togsgol
print(numbers[2:5]) # [2, 3, 4]

# Ehlehlees togsgol xurtel 
print(numbers[:5]) # [0, 1, 2, 3, 4]

# Ehlelees jagsaaltiin togsgol xurtel 
print(numbers[5:]) # [5, 6, 7, 8, 9]

# Alham todorxoiloh 
print(numbers[1:9:2]) # [1, 3, 5, 7]

# Jagsaaltiig xuulbarlah 
numbers_copy = numbers[:]
print(numbers_copy)
numbers.reverse()
print(numbers)



numbers.sort(reverse=True)
print(numbers)


