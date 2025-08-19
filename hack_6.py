"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    if not s:
        return ["0"]
    
    result = []
    for i in range(len(s)):
        if i % 2 == 0:  # posiciones 0,2,4... => 1,3,5
            result.append(str(i+1))
            if i + 2 < len(s):
                result.append("-")
    return result

print(fn_hack_6(["a", "b", "c", "d", "e"]))  # Output: ["1", "-", "3", "-", "5"]
print(fn_hack_6([]))  # Output: ["0"]