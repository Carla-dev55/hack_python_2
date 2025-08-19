"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    if len(s) > 3:
        result = s[1:-1]
    else:
        result = s
    # Si la cadena es mayor a 3, eliminar el primer y último carácter
    s = result
    # Devolver la cadena modificada
    return s

print(fn_hack_4("fooziman"))  # Output: "oozima"
print(fn_hack_4("barziman"))  # Output: "arzima"
print(fn_hack_4("qux"))       # Output: "qux"
  
