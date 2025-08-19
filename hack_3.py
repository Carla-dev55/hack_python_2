"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    sustituciones = {
        'a': '@',
        'e': '3',
        'i': '¡',
        'o': '0',
        'u': 'v'
    }
    
    processed_chars = []
    
    # Manejar el primer carácter
    if len(s) > 0:
        first_char = s[0].lower()
        if first_char in sustituciones:
            processed_chars.append(sustituciones[first_char])
        elif first_char.isalpha():
            processed_chars.append(first_char.upper()) # Convertir a mayúscula
        else:
            processed_chars.append(first_char)
    
    # Manejar los caracteres intermedios
    for i in range(1, len(s) - 1):
        char = s[i].lower()
        if char in sustituciones:
            processed_chars.append(sustituciones[char])
        else:
            processed_chars.append(char) # Mantener en minúscula si no es sustitución
            
    # Manejar el último carácter
    if len(s) > 1: # Si la cadena tiene más de un carácter
        last_char = s[-1].lower()
        if last_char in sustituciones:
            processed_chars.append(sustituciones[last_char])
        elif last_char.isalpha():
            processed_chars.append(last_char.upper()) # Convertir a mayúscula
        else:
            processed_chars.append(last_char)
    elif len(s) == 1 and not processed_chars: # Si solo había un carácter y ya se procesó
        pass

    # Unir los caracteres procesados en una cadena final
    return "".join(processed_chars)

print(fn_hack_3('fooziman'))
print(fn_hack_3('barziman'))    
print(fn_hack_3('3q'))    
print(fn_hack_3('qu'))    
print(fn_hack_3('qux'))
