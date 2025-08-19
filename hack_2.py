"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(name): 
    _ls = []
    vocals = "aeiouAEIOU"

    for char in name:
        if char not in vocals:
            _ls.append(char)

    name = "".join(_ls)
    return name
print(fn_hack_2("fooziman"))  # Output: "fzmn"
print(fn_hack_2("barziman"))  # Output: "brzmn"
print(fn_hack_2("qux"))       # Output: "qx"
