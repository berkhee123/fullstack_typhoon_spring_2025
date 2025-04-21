# Recapture 
# tuple ashiglaad create_point gedeg funkts uusgene uu 
# enehuu funkts ni x, y gedeg parametruud avdag bogood 
# ene 2 parametraar tuple butsaana 


def create_point(x, y):
    return (x, y)

# calculate_distance gedeg funkts todorhoilood point1, point2 gedeg 
# tuple parametraar avaad kartesian produkt oldog bolgooroi. 
def calculate_distance (point1, point2):
    import math

    return math.sqrt ((point2[0] - point1[0])**2 + (point2[1] - point1[1]))

# Heregleenii jishee 
point_a = create_point (0, 0)
point_b = create_point (3, 4)
distance = calculate_distance(point_a, point_b)
print(f" Xoyr tseg hoorondiin zai : {distance}") # 5.0

# Python sets 
# Husnegt haaltaar olonlog uusgeh 
set1 = [1, 2, 3, 4, 5]

# Davtagdsan elementuud avtomataar arilna 
set2 = {1, 2, 2, 3, 4, 4, 5}
print(set2) # {1, 2, 3, 4, 5}

#set (), funktseer olonlog uusgeh 
set3 = set([1, 2, 3, 4, 5])

# Hooson olonlog 
empty_set = set() # Hooson husnegt haalt{} ni dictionary uusgedeg 

# Temdegt mornoos olonlog uusgeh 
letters= set ("hello")
print(letters)#{'h', 'e', 'i', 'o'}

# Olonlogiin unedsen uildluud 
# Olonlog uusgeh 
friuts = {"alim", "banana", "jurj"}

# Element nemeh 
friuts.add("usan uzem")
print(friuts) # ('alim', 'banana', 'jurj', 'usan uzem')

# Olon element nemeh 
friuts.update (["mango", "kivi"])
print(friuts) # ('alim', 'banana', 'jurj', 'usan uzem', 'mango', kivi)
friuts.discard("liir") # Element baihgui bol aldaa zaahgui 

# Element hasah 
friuts.remove("banana") # Element baihgui bol aldaa zaana
print(friuts) # {'alim', 'jurj', 'usam uzem', 'mango' kivi'}

friuts.discard("liir") # Element baihgui bol aldaa zaahgui 

# Suuliin elementiig hasah 
popped = friuts.pop() # Ali element hasagdah ni todorhoigui 
print(popped)
print(friuts)

# Buh elementiig ustgah 
friuts.clear()
print(friuts) # set()

# Olonlogiin logik uildluud 
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7,8}

# Negdel (Union) - xoyr olonlogiin buh elementuud
print(A | B) # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B)) # {1, 2, 3, 4, 5, 6, 7, 8}

# Ogtloltsol (Intersection) - xoyr olonlogt baigaa niitleg elementuud
print(A & B) # {4, 5}
print(A.intersection(B)) # {4, 5}

# Ylgavar(Diffference) - neg olonlogt baigaa, nogood baihgui elementuud
print(A - B) # {1, 2, 3}
print(A.difference(B)) # {1, 2, 3}
print(B - A)
print(B.difference(A))

# Simmetrik ylgavar (Symmetric Difference) - ali neg olonlot baigaa
# xoyuland baihgui elemtentuud 
print(A ^ B) # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B)) # {1,2,3,6,7,8}

# Olonlogiin shalgah uildluud
A = {1,2,3,4,5}
B = {1,2,3}
C = {6,7,8}

# Ded olonlog mon esehiig shalgah 
print(B.issubset(A)) # True - B ni A-n ded olonlog 
print(A.issuperset(B)) # True - A ni B-g aguulsan

# Ogtloltsolgui esehiig shalgah 
print(A.isdisjoint(C)) # True - A, C hoyrt niitleg element baihgui 

# Tentsuu esehiig shalgah 
D = {1, 2, 3, 4, 5}
print(A == D) # True - A, D hoyr ijil elementuudtei \

# Olonlogiin hereglee 

# Davhardliig arilgah: Jagsaaltiin davhardsan elementuudiig arilgahad
numbers= [1, 2, 2, 3, 4, 4, 5]
unique_numbers=list(set(numbers))
print(unique_numbers) # [1,2,3,4,5]

# Gishuunchleliig shalgah : Element olonlogt baigaa esehiig hurdan shalgahad
friuts={"alim", "banana", "jurj"}
print("alim" in friuts) # True -O(1) hugatsaand shalgana

# Matetatik uildluud: Negdel, ogtloltsol. ylgavar zereg uildluuded
# Hoyor teksted baigaa niitleg usguudiig oloh
text1="hello"
text2="world"
common_letters=set(text1)&set(text2) # & ni 2land ni baigaa usgiig gargaj ireh 
print(common_letters) # {'l', 'o'}

# Ogogdliig shuuh: Davtagdashgwi utguudiig olohod
# Hoyr jarsaaltiin niitleg elementuudiig oloh 
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
common_elements=list(set(list1)&set(list2))
print(common_elements) # (4,5)

# Frozen set uusgeh 
frozen=frozenset([1,2,3,4,5])

# Logik uildluud hiih bolomjtoi
A=frozenset([1,2,3,4,5])
B=frozenset([4,5,6,7,8])
print(A|B) # frozenset({1,2,3,4,5,6,7,8})

# Element nemeh bolomjgui 
# frozen.add(6) # AttributeError: 'frozenset' object has no attribute 'add'

# Dictionary tulhuur bolgon ashiglah bolomjtoi
data={frozen:"Frozen set tulhuur"}
print(data[frozen]) # "Frozen set tulhuur"

# Exercise 01 - enehuu funkts ni ogogdson tekstiin ugnuudiig toolood 
# tegeed heden shirheg ugnuudiig davtagdahgwi hereglegdej baigaag 
# olood butsaana
def count_unique_words(text):
    words=text.lower().split()
    unique_words=set(words)
    return len(unique_words)

text= "Bi Python hel surch baina. Python bol mash sonirholtoi xel"
print(f"Davtagdashgwi ugsiin too:{count_unique_words(text)}")

# Davtagdashgui ugsiin too: 9 



      

                     













