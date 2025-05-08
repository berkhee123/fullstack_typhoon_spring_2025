class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, breed):
        self.name = name # Instance attribute
        self.breed = breed # Intrance attribute


fido = Dog("Fido", "Golden Retriever") # object fido 
rex = Dog("Rex", "German Shepherd")  # rex object 

print(Dog.species) # Outout: Canis familiaris 
print(fido.species) # Outout: Canis familiaris 
print(rex.species) # Outout: Canis familiaris 

# Changing class attribute affects all instances 
Dog.species = "Canis lupus familiaris"
print(fido.species) # Outout: Canis lupus familiaris 
print(rex.species) # Outout: Canis lupus familiaris 

# But setting the attribute on an instance creates an instance attribute 
fido.species = "Changed for Fido"
print(fido.species) # Output: Changed for Fido
print(rex.species) # Output: Canis lupus familiaris 
