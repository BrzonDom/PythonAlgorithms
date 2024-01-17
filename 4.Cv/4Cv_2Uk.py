"""
Záměna slova

    Napište program, který čte standardní vstup a v načteném řetězci zamění slovo Ahoj za slovo Cau.
    Můžete využít vestavěné funkce find, replace, nebo Vaše funkce z předchozí úlohy.
    Pokud se ve vstupním řetězci objeví slovo Konec, program skončí. V tomto řádku ale nejdříve zamění Ahoj za Cau.

"""

# The find() method finds the first occurrence of the specified value.
#   string.find(value, start, end)

# The replace() method replaces a specified phrase with another specified phrase.
#   string.replace(oldvalue, newvalue, count)

Input_str = "Ahoj jak se vede ? No ahoj. Pozdravuj doma, řekni ahoj rodince"
# Input_str = input()

Replace_str = Input_str.replace("Ahoj", "Cau")
Replace_str = Replace_str.replace("ahoj", "cau")

print(f"Input_str:   {Input_str}")
print(f"Replace_str: {Replace_str}")

