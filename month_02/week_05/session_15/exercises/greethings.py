"""Mendchilnii funktsuudiig aguulsan moduli"""

# Togtmol utga
DEFAULT_LANGUAGE = "Mongol"

# "Huviin" huvisagch (nernii omnoh dooguur zuraas ni huviin gedgiig ilerhiilne)
_counter = 0

def greet(name, language=DEFAULT_LANGUAGE):
    """Hereglegchid mendchilgee heleh."""
    global _counter
    _counter += 1

    if language.lower() == "mongol":
        return f"Sain baina uu, {name}!"
    elif language.lower() == "angli":
        return f"Hello, {name}!"
    else: 
        return f"Mendchilgee, {name}!"
    

def get_greeting_count():
    """Mendchilgee heden udaa helsniig butsaah."""
    return _counter

# Ene heseg zovhon failiig shuud ajilluulahad guitsetgene
if __name__ == "__main__":
    print("greetings.py failiig shuud ajilluulj baina")
    print(greet("Bat"))
    print(greet("John", "Angli"))
    print(f"Mendchilgee {get_greeting_count()} udaa helegdsen")
   



    