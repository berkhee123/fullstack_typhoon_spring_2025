# advance ile operations

with open('advanced.txt', 'r') as file:
    position = file.tell()
    
    content = file.read(5)
    print(content)
    file.seek(10) # ehnii gishuunuudiig delete hiideg 

    content = file.read()
    print(content)

# iterate with line numbers
with open('output.txt', 'r') as file:
    for i, line in enumerate(file, 1): # (1) index eer eheldeg 
        print(f"line {i}: {line}")

# CSV Files handling
with open('data.csv', 'r', encoding='utf-8') as file: # zaaval encoding='ut-8' bichne
    for line in file:
        values = line.strip().split(',')
        print(values)

with open('output.csv', 'w') as file:               # \n er ni enter geed oilgochih 
    file.write('Name,Age,City\n')
    file.write('john,25,New York\n')
    file.write('Alice,30,Boston\n')
    file.write('Berkhee,33,Ulaanbaatar\n')
    file.write('Shat,35,Ulaanbaatar')





