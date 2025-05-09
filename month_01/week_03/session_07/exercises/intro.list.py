# intro into python list 

# Problem - Variables
b = 7 
print(b)

# Solution - Lists
friuts = ["alim", "banana", "guzeelzgene" ]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "xoyr", 3.0, True]
empty_list = []

print(type(friuts))
print(friuts)

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
friuts[0] = "uzem"
print(friuts) #['uzem', 'banana', 'guzeelzgene', 'kivi']

# Element nemeh 
friuts.append("kivi")
print(friuts) # ['uzem', 'banana', 'guzeelzgene', 'kivi']

# Todorhoi bairlald element oruulah 
friuts.insert(1,"mango")
print(friuts) # ['uzem', 'banana', 'guzeelzgene', 'kivi']
 # Elements ustgah 
friuts.remove("banana")
print(friuts) # ['uzem', 'banana', 'guzeelzgene', 'kivi']

# Indekseer element ustgah 
removed_friut = friuts.pop(1) # mango-g ustgaj. xuvisagchij hadgalna
print(removed_friut) # mango 
print(friuts) # ['uzem, 'guzeelgzgene', 'kivi']

#buh elementiig ustgah 
friuts.clear()
print(friuts) #[]

# List methods 
friuts = ['alim', 'banana', 'guzeelzgene']

#Jagsaaliin urt 
print(len(friuts)) # 3 

# Jagsaaltiig erembleh
friuts.sort()
print(friuts) # ['alim', 'banana', 'guzeelzgene']

# Jagsaaltiig urvuu erembeleh 
friuts.reverse()
print(friuts) # ['guzeelzgene', 'banana', 'alim']

# Elementiin indeksiig oloh 
print(friuts.index("banana")) # 1 

# Elementiin toog toolloh 
print(friuts.count("banana")) # 1 

# Jagsaaltiig xuulbarlah 
friuts_copy = friuts.copy()
print(friuts_copy) # ['guzeelzgene', 'banana', 'alim']

# Jagsaaltuudiiig negtgeh 
more_friuts = ["kivi", "mango"]
friuts.extend(more_friuts)
print(friuts) # ['guzeelzgene', 'banana', 'alim']

## List Slicing 
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

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
